from django.core.management.base import BaseCommand
from bulkexcel.models import *
from django.db.models import Q
from django.db import transaction

import random
import string
import hashlib
from django.utils.timezone import now
import time
import os
from dotenv import load_dotenv
from decimal import Decimal

class Command(BaseCommand):
    def storeOwner(self, valid_row):
        owner = Actor.objects.filter(deleted=0, name=valid_row.owner_name).first()
        user = User.objects.filter(id=valid_row.user_id).first()

        if not owner:
            owner = Actor.objects.create(
                prefer_lang=0 if valid_row.notification_language == 'Arabic' else 1,
                company_user=user,
                name=valid_row.owner_name,
                address_id=None,
                type_id=1,
                deleted=0,
                bulk_excel_id=valid_row.id,
                excel_batch_id=valid_row.batch_id
            )

            chars = "@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            email_code = hashlib.sha256(''.join(random.choice(chars) for _ in range(15)).encode()).hexdigest()

            User.objects.create(
                user_name=valid_row.owner_name,
                notification_tel=0,
                actors_id=owner.id,
                password=hashlib.sha256('123456'.encode()).hexdigest(),
                email_code=email_code,
                new_pass_needed=0,
                verified=True,
                email_verified=True,
                email_verified_date=now(),
                lang=0 if valid_row.notification_language == 'Arabic' else 1,
                role_id=1,
                bulk_excel_id=valid_row.id,
                excel_batch_id=valid_row.batch_id,
            )
        return owner

    def storePayer(self, row):
        payer = Actor.objects.filter(deleted=0, actor_number=row.payer_number, company_user=row.user_id).first()
        user = User.objects.filter(id=row.user_id).first()

        if not payer:
            payer = Actor.objects.create(
                prefer_lang=0 if row.notification_language == 'Arabic' else 1,
                company_user=user,
                name=row.payer_name,
                email=row.payer_email,
                tel1=row.payer_telephone_1,
                tel2=row.payer_telephone_2,
                tel3=row.payer_telephone_3,
                notification_tel=row.notification_telephone,
                actor_number=row.payer_number,
                type_id=2,
                nationalid=row.national_id,
                nationalid_type=row.national_id_type,
                deleted=0,
                bulk_excel_id=row.id,
                excel_batch_id=row.batch_id
            )

            OwnerPayer.objects.create(
                actors_owner_id=row.user_id,
                actors_payer_id=payer.id,
                bulk_excel_id=row.id,
                excel_batch_id=row.batch_id
            )

            password = '279319'
            notification_tel = row.payer_telephone_1 or row.payer_telephone_2 or row.payer_telephone_3
            email_code = hashlib.sha256(''.join(random.choices(string.ascii_letters + string.digits, k=15)).encode()).hexdigest()

            User.objects.create(
                user_name=row.payer_telephone_1 or ' ',
                actors_id=payer.id,
                notification_tel=notification_tel,
                password=hashlib.sha256(password.encode()).hexdigest(),
                email_code=email_code,
                new_pass_needed=0,
                verified=True,
                email_verified=True,
                email_verified_date=now(),
                lang=0 if row.notification_language == 'Arabic' else 1,
                role_id=2,
                type='TENANT',
                bulk_excel_id=row.id,
                excel_batch_id=row.batch_id
            )
        return payer

    def storeBuilding(self, row):
        city = City.objects.filter(name=row.city).first()
        country = Country.objects.filter(country_name=row.country).first()
        address = Address.objects.filter(name=row.location, deleted=0, city=city, country_id=country.id).first()

        if not address:
            address = Address.objects.create(
                name=row.location,
                deleted=0,
                city=city,
                country_id=country.id,
                bulk_excel_id=row.id,
                excel_batch_id=row.batch_id
            )

        building = Building.objects.filter(code=row.building_code).first()
        if building:
            building.name = row.building_name
            building.project_id = Project.objects.filter(id=row.project_id).first()
            building.address_id = address.id
            building.region = row.region
            building.area = row.area
            building.units_count = row.units_count
            building.active = True
            building.deleted = 0
            building.bulk_excel_id = row.id
            building.excel_batch_id = row.batch_id
            building.save()
        else:
            building = Building.objects.create(
                name=row.building_name,
                project_id=Project.objects.filter(id=row.project_id).first(),
                address_id=address.id,
                region=row.region,
                area=row.area,
                units_count=row.units_count,
                active=True,
                deleted=0,
                code=row.building_code,
                bulk_excel_id=row.id,
                excel_batch_id=row.batch_id
            )
        return building

    def storeUnit(self, row, building):
        unit_status = UnitStatus.objects.filter(deleted=0, name=row.unit_status).first()
        unit_type = UnitType.objects.filter(deleted=0, name=row.unit_type).first()
        unit = Unit.objects.filter(code=row.unit_code).first()

        if unit:
            unit.name=row.unit_name
            unit.building_id = building.id
            unit.address_id = building.address_id
            unit.bedrooms = 0
            unit.bathrooms = 0
            unit.size = 0
            unit.unit_no = row.unit_number
            unit.floor_no = row.floor_number
            unit.status_id = unit_status.id if unit_status else unit.status_id
            unit.type_id = unit_type.id if unit_type else unit.type_id
            unit.deleted = 0
            unit.bulk_excel_id = row.id
            unit.excel_batch_id = row.batch_id
            unit.save()
        else:
            unit = Unit.objects.create(
                name=row.unit_name,
                code=row.unit_code,
                building_id=building.id,
                address_id=building.address_id,
                bedrooms=0,
                bathrooms=0,
                size=0,
                unit_no=row.unit_number,
                floor_no=row.floor_number,
                status_id=unit_status.id if unit_status else None,
                type_id=unit_type.id if unit_type else None,
                deleted=0,
                bulk_excel_id=row.id,
                excel_batch_id=row.batch_id
            )
        return unit

    def storeContract(self, row, payer, unit):
        notification_type = NotificationType.objects.filter(name=row.notification_type).first()
        service_contract_type = ContractType.objects.filter(name=row.contract_type).first()
        config = ContractConfiguration.objects.filter(active=True, actor_company_id=row.user_id).first()
        contract = ServiceContract.objects.filter(contract_name=row.contract_name, actors_secondparty_id=payer.id, actors_firstparty_id=row.user_id).first()
        print(f"Service Contract {service_contract_type.id}")
        frequncy = 3 if row.frequency == 'Monthly' else 6 if row.frequency == 'Annually' else None

        if contract:
            contract.start_date = row.contract_start_date
            contract.end_date = row.contract_end_date
            contract.start_collection_date = row.collection_start_date
            contract.amount = row.contract_amount
            contract.unit = unit
            contract.frequncy = frequncy
            contract.save()
        else:
            contract = ServiceContract.objects.create(
                contract_type=service_contract_type,
                contract_name=row.contract_name,
                unit=unit,
                actors_firstparty_id=row.user_id,
                actors_secondparty_id=payer.id,
                active=True,
                amount=row.contract_amount,
                notification_lang=0,
                bank_owner=OwnerBank.objects.filter(id=row.bank_owner_id).first(),
                frequncy=frequncy,
                start_date=row.contract_start_date,
                end_date=row.contract_end_date,
                start_collection_date=row.collection_start_date,
                discount=0,
                contract_configuration=config,
                comment=row.comments,
                advance_payment=0,
                insurance=0,
                invoice_recurrence_date=row.collection_start_date,
                annual_increase=0,
                bulk_excel_id=row.id,
                excel_batch_id=row.batch_id
            )
            ServiceContractNotificationType.objects.create(service_contract=contract, notification_type_id=notification_type.id)
        return contract
    
    def storeInvoice(self, row, contract):
        invoice = ContractInvoice.objects.filter(
            service_contract=contract,
            date_from=row.contract_start_date,
            date_to=row.contract_end_date,
            payer_id=contract.actors_secondparty_id,
            receiver_id=contract.actors_firstparty_id,
        ).first()

        if not invoice:
            if row.vat:
                amount_total = row.contract_amount + Decimal(row.vat)
            else:
                amount_total = row.contract_amount

            invoice = ContractInvoice.objects.create(
                name=row.invoice_name,
                receipt_company_no=row.company_receipt,
                service_contract=contract,
                date_from=row.contract_start_date,
                date_to=row.contract_end_date,
                payer_id=contract.actors_secondparty_id,
                receiver_id=contract.actors_firstparty_id,
                invoice_type=InvoiceType.objects.filter(key='contract').first().id,
                type='CONTRACT',
                collection_date=row.collection_start_date,
                active=True,
                discount=0,
                status_id=1,
                amount_total=amount_total,
                amount_remaining=amount_total,
                amount_paid=0,
                vat= row.vat if row.vat else 0,
                amount_original=row.contract_amount,
                reminders_only=0,
                bulk_excel_id=row.id,
                excel_batch_id=row.batch_id
            )

            while True:
                invoice_uuid = str(uuid.uuid4())
                invoice_short_uuid = invoice_uuid[:7]
                
                inv_count = InvoicesLog.objects.filter(invoice_short_uuid=invoice_short_uuid).count()
                if inv_count == 0:
                    break
            load_dotenv()
            invoice_log = InvoicesLog.objects.create(
                    invoice=invoice,
                    invoice_uuid=invoice_uuid,
                    invoice_short_uuid=invoice_short_uuid,
                    invoice_url=f"{os.getenv('APP_URL')}{invoice_short_uuid}",
                    active=1,
                    bulk_excel_id=row.id,
                    excel_batch_id=row.batch_id
                )
            
            return invoice

    def createInvoiceSendReminder(self, invoice, payer, contract):
        # $paymentMessage = str_replace('@CustomerName', $invoice->payer->name, $paymentMessage);
        contractConfig = ContractConfiguration.objects.filter(id=contract.contract_configuration.id).first()
        paymentMessage = contractConfig.payment_sms_arabic
        month = invoice.date_from
        payer_name = payer.name
        contract_type = contract.contract_type.name
        invoice_amount = invoice.amount_total
        invoice_url = InvoicesLog.objects.filter(invoice=invoice).first().invoice_url
        
        # Format the payment message
        payment_message = paymentMessage.replace('@CustomerName', payer_name) \
                                                .replace('@ContractType', contract_type) \
                                                .replace('@Month', str(month)) \
                                                .replace('@InvoiceAmount', str(invoice_amount)) \
                                                .replace('@InvoiceUrl', invoice_url)

        systemUser = User.objects.filter(type='SYSTEM').first()

        EngineTemp.objects.create(
            message=payment_message,
            command='SendBulkInvoiceReminder',
            subject_id=invoice.id,
            subject_type='INVOICE',
            trials=0,
            action_type='SEND_NOTIFICATION',
            company_id=invoice.receiver_id,
            company_email=payer.email,
            client_email=payer.email,
            receiver_id=payer.id,
            sender_id=systemUser.id,
            language='ARABIC',
            notification_type_id=2,
            notify_type='TODAY',
            invoice_id=invoice.id,
            client_phone=payer.notification_tel
        )


    def handle(self, *args, **kwargs):
        latest_entry = BulkContractExcel.objects.latest('id')
        self.batch_id = latest_entry.batch_id if latest_entry else None

        valid_rows_list = BulkContractExcel.objects.filter(Q(validation_errors__isnull=True), batch_id=self.batch_id, status='PENDING').all()

        start_time = time.time()
        for valid_row in valid_rows_list:
            try:
                with transaction.atomic():
                    owner = self.storeOwner(valid_row)
                    payer = self.storePayer(valid_row)
                    building = self.storeBuilding(valid_row)
                    unit = self.storeUnit(valid_row, building)
                    contract = self.storeContract(valid_row, payer, unit)
                    invoice = self.storeInvoice(valid_row, contract)

                    if payer.notification_tel:
                        self.createInvoiceSendReminder(invoice, payer, contract)

                    valid_row.status = 'SUCCESS'
                    valid_row.validation_errors = None
                    valid_row.save()
            except Exception as e:
                valid_row.validation_errors = str(e)
                valid_row.status = 'FAILED'
                valid_row.save()

        end_time = time.time()
        duration_seconds = end_time - start_time
        duration_minutes = duration_seconds / 60
        print(f"⏱️ Execution Time: {duration_minutes:.2f} minutes")
