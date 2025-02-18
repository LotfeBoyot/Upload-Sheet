from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import uuid



class OwnerUnit(models.Model):
    id = models.AutoField(primary_key=True)
    actors_owner_id = models.IntegerField(null=True, blank=True)
    unit_id = models.PositiveIntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=255, null=True, blank=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'owner_units'


class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    status_id = models.PositiveIntegerField(null=True, blank=True)
    address_id = models.PositiveIntegerField()
    building_id = models.PositiveIntegerField(null=True, blank=True)
    type_id = models.PositiveIntegerField(null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    unit_no = models.CharField(max_length=45, null=True, blank=True)
    floor_no = models.CharField(max_length=45, null=True, blank=True)
    unit_price = models.DecimalField(max_digits=16, decimal_places=4, null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=255, null=True, blank=True)
    excel_batch_id = models.IntegerField(null=True, blank=True)
    bulk_excel_id = models.IntegerField(null=True, blank=True)
    deleted = models.CharField(max_length=255, default='0', null=True, blank=True)
    original_owner = models.IntegerField(null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'units'


class UnitType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=255, null=True, blank=True)
    deleted = models.CharField(max_length=255, null=True, blank=True)  # Consider BooleanField if '0'/'1'

    class Meta:
        db_table = 'unit_types'


class UnitStatus(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(null=True, blank=True)
    created_by = models.IntegerField(null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.IntegerField(null=True, blank=True)
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted = models.BooleanField(default=False)  # Converted tinyint(1) to BooleanField

    class Meta:
        db_table = 'unit_status'


class Building(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    project_id = models.ForeignKey(
        'Project', on_delete=models.CASCADE, null=True, blank=True, db_column='project_id'
    )
    sub_project = models.IntegerField(null=True, blank=True)
    address1 = models.CharField(max_length=255, null=True, blank=True)
    address_id = models.IntegerField(default=0)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    active = models.BooleanField(default=True)  # Converted tinyint(1) to BooleanField
    units_count = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=255, null=True, blank=True)
    excel_batch_id = models.IntegerField(null=True, blank=True)
    bulk_excel_id = models.IntegerField(null=True, blank=True)
    deleted = models.CharField(max_length=255, default='0')  # Keeping it as CharField since it's a string in DB
    code = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'buildings'


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    address1 = models.CharField(max_length=1000, null=True, blank=True)
    address2 = models.CharField(max_length=1000, null=True, blank=True)
    city = models.ForeignKey(
        'City', on_delete=models.CASCADE, db_column='city_id'
    )
    country_id = models.IntegerField()  # Assuming no Country model reference is provided
    postal_code = models.IntegerField(null=True, blank=True)
    building_no = models.CharField(max_length=10, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=45, null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=45, null=True, blank=True)
    deleted = models.BooleanField(default=False)  # Converted tinyint(1) to BooleanField
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=45, null=True, blank=True)
    excel_batch_id = models.IntegerField(null=True, blank=True)
    bulk_excel_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'address'


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    country = models.ForeignKey(
        'Country', on_delete=models.CASCADE, db_column='country_id'
    )

    class Meta:
        db_table = 'cities'


class OwnerPayer(models.Model):
    id = models.AutoField(primary_key=True)
    actors_owner = models.ForeignKey(
        'Actor', on_delete=models.CASCADE, db_column='actors_owner_id', related_name='owner_payers'
    )
    actors_payer = models.ForeignKey(
        'Actor', on_delete=models.CASCADE, db_column='actors_payer_id', related_name='payer_owners'
    )
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=45, null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=45, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=45, null=True, blank=True)
    bulk_excel_id = models.IntegerField(null=True, blank=True)
    excel_batch_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'owner_payers'


class UserManager(BaseUserManager):
    def create_user(self, user_name, password=None, **extra_fields):
        if not user_name:
            raise ValueError("The Username field is required")
        user = self.model(user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, password=None, **extra_fields):
        extra_fields.setdefault("role_id", 1)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(user_name, password, **extra_fields)


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    actors = models.ForeignKey(
        'Actor', on_delete=models.CASCADE, db_column='actors_id', related_name='users'
    )
    user_name = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=255)
    plain_password = models.CharField(max_length=255, null=True, blank=True)
    notification_tel = models.CharField(max_length=50)
    email_code = models.CharField(max_length=255, null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    email_verified_date = models.DateTimeField(null=True, blank=True)
    verified_date = models.DateTimeField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    user_status = models.IntegerField(default=1)
    last_login = models.DateTimeField(null=True, blank=True)
    last_reset_password = models.DateTimeField(null=True, blank=True)
    failed_password_attempt_count = models.IntegerField(null=True, blank=True)
    new_pass_needed = models.BooleanField(default=False)
    role = models.ForeignKey(
        'ERole', on_delete=models.CASCADE, db_column='role_id', related_name='users', default=1
    )
    type = models.CharField(max_length=256, null=True, blank=True)
    logo = models.CharField(max_length=255, null=True, blank=True)
    lang = models.IntegerField(default=1)
    player_id = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.IntegerField(null=True, blank=True)
    deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    bulk_excel_id = models.IntegerField(null=True, blank=True)
    excel_batch_id = models.IntegerField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "user_name"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'

class ERole(models.Model):
    type = models.CharField(max_length=45)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'e-roles'

    def __str__(self):
        return self.type



class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    prefer_lang = models.BooleanField(default=True)
    tel1 = models.CharField(max_length=20, null=True, blank=True)
    tel2 = models.CharField(max_length=20, null=True, blank=True)
    tel3 = models.CharField(max_length=255, null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    nationalid = models.CharField(max_length=50, null=True, blank=True)
    national_image = models.CharField(max_length=255, null=True, blank=True)
    suspend = models.BooleanField(default=False)
    nationalid_type = models.CharField(max_length=50, null=True, blank=True)
    type = models.ForeignKey(
        'ERole', on_delete=models.CASCADE, db_column='type_id', related_name='actors', null=True, blank=True
    )
    address = models.ForeignKey(
        'Address', on_delete=models.SET_NULL, db_column='address_id', related_name='actors', null=True, blank=True
    )
    notification_tel = models.CharField(max_length=50, null=True, blank=True)
    no_of_units = models.IntegerField(null=True, blank=True)
    tenant_type = models.IntegerField(null=True, blank=True)
    unit_name = models.CharField(max_length=255, null=True, blank=True)
    logo = models.CharField(max_length=255, null=True, blank=True)
    self_registered = models.BooleanField(default=False)
    actor_number = models.CharField(max_length=45, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=45, null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=45, null=True, blank=True)
    deleted = models.BooleanField(default=False)
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=45, null=True, blank=True)
    bulk_excel_id = models.IntegerField(null=True, blank=True)
    excel_batch_id = models.IntegerField(null=True, blank=True)
    company_user = models.ForeignKey(
        'User', on_delete=models.RESTRICT, db_column='company_user_id', related_name='sub_actors', null=True, blank=True
    )
    added_by = models.ForeignKey(
        'User', on_delete=models.CASCADE, db_column='added_by', related_name='added_actors', null=True, blank=True
    )

    class Meta:
        db_table = 'actors'


class Country(models.Model):
    id = models.AutoField(primary_key=True)
    country_code = models.CharField(max_length=20)
    country_name = models.CharField(max_length=100)
    deleted_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'countries'


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    company_id = models.IntegerField(null=True, blank=True)
    parent_id = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=255, null=True, blank=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'projects'


class BulkContractExcel(models.Model):
    id = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=255, null=True, blank=True)
    unit_type = models.CharField(max_length=255, null=True, blank=True)
    unit_status = models.CharField(max_length=255, null=True, blank=True)
    bedrooms = models.CharField(max_length=255, null=True, blank=True)
    area = models.CharField(max_length=255, null=True, blank=True)
    bathrooms = models.CharField(max_length=255, null=True, blank=True)
    floor_number = models.CharField(max_length=255, null=True, blank=True)
    unit_number = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    building_name = models.CharField(max_length=255, null=True, blank=True)
    building_status = models.CharField(max_length=255, null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    units_count = models.FloatField(null=True, blank=True)
    payer_name = models.CharField(max_length=255, null=True, blank=True)
    payer_email = models.CharField(max_length=255, null=True, blank=True)
    payer_telephone_1 = models.CharField(max_length=255, null=True, blank=True)
    payer_telephone_2 = models.CharField(max_length=255, null=True, blank=True)
    payer_telephone_3 = models.CharField(max_length=255, null=True, blank=True)
    payer_number = models.CharField(max_length=255, null=True, blank=True)
    notification_telephone = models.CharField(max_length=255, null=True, blank=True)
    national_id_type = models.CharField(max_length=255, null=True, blank=True)
    national_id = models.CharField(max_length=255, null=True, blank=True)
    payer_address = models.CharField(max_length=255, null=True, blank=True)
    contract_type = models.CharField(max_length=255, null=True, blank=True)
    contract_status = models.CharField(max_length=255, null=True, blank=True)
    notification_type = models.CharField(max_length=255, null=True, blank=True)
    notification_language = models.CharField(max_length=255, null=True, blank=True, default="0")
    contract_name = models.CharField(max_length=255, null=True, blank=True)
    invoice_name = models.CharField(max_length=255, null=True, blank=True)
    company_receipt = models.CharField(max_length=255, null=True, blank=True)
    frequency = models.CharField(max_length=255, null=True, blank=True)
    contract_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    annual_increase_type = models.CharField(max_length=255, null=True, blank=True)
    annual_increase = models.CharField(max_length=255, null=True, blank=True)
    contract_start_date = models.CharField(max_length=255, null=True, blank=True)
    contract_end_date = models.CharField(max_length=255, null=True, blank=True)
    collection_start_date = models.CharField(max_length=255, null=True, blank=True)
    advance_payment = models.CharField(max_length=255, null=True, blank=True)
    insurance = models.CharField(max_length=255, null=True, blank=True)
    comments = models.CharField(max_length=255, null=True, blank=True)
    discount_type = models.CharField(max_length=255, null=True, blank=True)
    discount = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    address_id = models.IntegerField(null=True, blank=True)
    payer_id = models.IntegerField(null=True, blank=True)
    unit_id = models.IntegerField(null=True, blank=True)
    sheet_row_number = models.IntegerField(null=True, blank=True)
    building_id = models.IntegerField(null=True, blank=True)
    validation_errors = models.TextField(null=True, blank=True)
    server_errors = models.TextField(null=True, blank=True)
    city_id = models.IntegerField(null=True, blank=True)
    country_id = models.IntegerField(null=True, blank=True)
    sheet_id = models.IntegerField(null=True, blank=True)
    project_id = models.IntegerField(null=True, blank=True)
    bank_owner_id = models.IntegerField(null=True, blank=True)
    sheet_path = models.CharField(max_length=500, null=True, blank=True)
    batch_id = models.IntegerField(null=True, blank=True)
    user_id = models.IntegerField(null=True, blank=True)
    contract_id = models.IntegerField(null=True, blank=True)
    notification_languge = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner_id = models.IntegerField(null=True, blank=True)
    owner_name = models.CharField(max_length=255, null=True, blank=True)
    unit_code = models.CharField(max_length=255, null=True, blank=True)
    building_code = models.CharField(max_length=255, null=True, blank=True)
    vat = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'bulk_contract_excel'


class OriginalOwner(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'original_owner'


class ContractType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255, null=True, blank=True)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    deleted_on = models.DateTimeField(auto_now=True)
    deleted_by = models.CharField(max_length=255, null=True, blank=True)
    deleted = models.CharField(max_length=255, default='0')
    order = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'contract_types'


class ContractConfiguration(models.Model):
    id = models.AutoField(primary_key=True)
    configuration_type = models.ForeignKey(
        'ContractConfigType', on_delete=models.CASCADE
    )
    actor_company = models.ForeignKey(
        'Actor', on_delete=models.SET_NULL, null=True, blank=True
    )
    commission_percentage = models.FloatField(null=True, blank=True)
    receiver_commission_percentage = models.FloatField(null=True, blank=True)
    payer_commission_percentage = models.FloatField(null=True, blank=True)
    payment_sms_english = models.CharField(max_length=500, null=True, blank=True)
    payment_sms_arabic = models.CharField(max_length=500, null=True, blank=True)
    payment_email_english = models.TextField(null=True, blank=True)
    payment_email_arabic = models.TextField(null=True, blank=True)
    send_sms_on_bulk_sheet_upload = models.BooleanField(default=True)
    
    contract_before_notification_1st_msg_ar = models.TextField(null=True, blank=True)
    contract_before_notification_1st_msg_eng = models.TextField(null=True, blank=True)
    contract_before_notification_1st_days = models.IntegerField(null=True, blank=True)
    contract_before_notification_1st_days_status = models.BooleanField(default=False)
    
    contract_before_notification_2nd_msg_ar = models.TextField(null=True, blank=True)
    contract_before_notification_2nd_msg_eng = models.TextField(null=True, blank=True)
    contract_before_notification_2nd_days = models.IntegerField(null=True, blank=True)
    contract_before_notification_2nd_days_status = models.BooleanField(default=False)

    contract_before_notification_3rd_msg_ar = models.TextField(null=True, blank=True)
    contract_before_notification_3rd_msg_eng = models.TextField(null=True, blank=True)
    contract_before_notification_3rd_days = models.IntegerField(null=True, blank=True)
    contract_before_notification_3rd_days_status = models.BooleanField(default=False)

    contract_before_notification_4th_msg_ar = models.TextField(null=True, blank=True)
    contract_before_notification_4th_msg_eng = models.TextField(null=True, blank=True)
    contract_before_notification_4th_days = models.IntegerField(null=True, blank=True)
    contract_before_notification_4th_days_status = models.BooleanField(default=False)

    contract_after_notification_1st_msg_ar = models.TextField(null=True, blank=True)
    contract_after_notification_1st_msg_eng = models.TextField(null=True, blank=True)
    contract_after_notification_1st_days = models.IntegerField(null=True, blank=True)
    contract_after_notification_1st_days_status = models.BooleanField(default=False)

    contract_after_notification_2nd_msg_ar = models.TextField(null=True, blank=True)
    contract_after_notification_2nd_msg_eng = models.TextField(null=True, blank=True)
    contract_after_notification_2nd_days = models.IntegerField(null=True, blank=True)
    contract_after_notification_2nd_days_status = models.BooleanField(default=False)

    contract_after_notification_3rd_msg_ar = models.TextField(null=True, blank=True)
    contract_after_notification_3rd_msg_eng = models.TextField(null=True, blank=True)
    contract_after_notification_3rd_days = models.IntegerField(null=True, blank=True)
    contract_after_notification_3rd_days_status = models.BooleanField(default=False)

    contract_after_notification_4th_msg_ar = models.TextField(null=True, blank=True)
    contract_after_notification_4th_msg_eng = models.TextField(null=True, blank=True)
    contract_after_notification_4th_days = models.IntegerField(null=True, blank=True)
    contract_after_notification_4th_days_status = models.BooleanField(default=False)

    notification_status = models.BooleanField(default=True)
    body_en = models.CharField(max_length=255, null=True, blank=True)
    body_ar = models.CharField(max_length=255, null=True, blank=True)
    title_en = models.CharField(max_length=255, null=True, blank=True)
    title_ar = models.CharField(max_length=255, null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=45, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_by = models.CharField(max_length=45, null=True, blank=True)

    deleted = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=45, null=True, blank=True)
    esh3ar_5sm = models.DecimalField(max_digits=12, decimal_places=3, default=0.000)

    class Meta:
        db_table = 'contract_configuration'



class ContractConfigType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'contract_config_types'

    def __str__(self):
        return self.name



class ServiceContract(models.Model):
    contract_type = models.ForeignKey('ContractType', on_delete=models.CASCADE, null=True, blank=True)
    contract_name = models.CharField(max_length=45)
    actors_firstparty_id = models.IntegerField()
    actors_secondparty_id = models.IntegerField()
    unit = models.ForeignKey('Unit', on_delete=models.SET_NULL, null=True, blank=True)
    active = models.BooleanField(default=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    notification_lang = models.BooleanField(default=False)
    bank_owner = models.ForeignKey('OwnerBank', on_delete=models.SET_NULL, null=True, blank=True)
    contract_configuration = models.ForeignKey('ContractConfiguration', on_delete=models.CASCADE, default=0)
    frequncy = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    start_collection_date = models.DateField()
    discount = models.FloatField(null=True, blank=True)
    annual_increase = models.FloatField(default=0)
    advance_payment = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    insurance = models.DecimalField(max_digits=12, decimal_places=4, null=True, blank=True)
    comment = models.TextField(max_length=500, null=True, blank=True)
    invoice_recurrence_date = models.DateField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=255, null=True, blank=True)
    deleted = models.CharField(max_length=255, default='0')
    excel_batch_id = models.IntegerField(null=True, blank=True)
    bulk_excel_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'service_contracts'


class NotificationType(models.Model):
    name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    deleted_on = models.DateTimeField(auto_now=True)
    deleted_by = models.CharField(max_length=255, null=True, blank=True)
    deleted = models.CharField(max_length=255, default='0')

    class Meta:
        db_table = 'notifications_types'

    def __str__(self):
        return self.name


class OwnerBank(models.Model):
    actors_owner = models.ForeignKey('Actor', on_delete=models.SET_NULL, null=True, db_column='actors_owner_id')
    bank = models.ForeignKey('Bank', on_delete=models.SET_NULL, null=True, db_column='bank_id')
    branch = models.CharField(max_length=255, null=True, blank=True)
    account_no = models.CharField(max_length=255, null=True, blank=True)
    beneficiary_ar_name = models.CharField(max_length=255, null=True, blank=True)
    beneficiary_en_name = models.CharField(max_length=255, null=True, blank=True)
    iban = models.CharField(max_length=255, null=True, blank=True)
    verified = models.IntegerField(null=True, blank=True)
    swift_code = models.CharField(max_length=100, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=255, null=True, blank=True)
    deleted = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'owner_banks'

    def __str__(self):
        return f"Bank Account {self.account_no} for Owner {self.actors_owner_id}"


class Bank(models.Model):
    name = models.CharField(max_length=255)
    swift_code = models.CharField(max_length=45, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=255, null=True, blank=True)
    deleted = models.CharField(max_length=255, default='0', null=True, blank=True)

    class Meta:
        db_table = 'banks'

    def __str__(self):
        return self.name



class ServiceContractNotificationType(models.Model):
    service_contract = models.ForeignKey('ServiceContract', on_delete=models.CASCADE)
    notification_type_id = models.IntegerField()

    class Meta:
        db_table = 'service_contracts_notification_types'


class InvoiceType(models.Model):
    name = models.CharField(max_length=45)
    name_ar = models.CharField(max_length=255, null=True, blank=True)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    key = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'invoice_type'

    def __str__(self):
        return self.name
    

class ContractInvoice(models.Model):
    TYPE_CHOICES = [
        ('CONTRACT', 'Contract'),
        ('UTILITY', 'Utility'),
        ('SINGLE_INVOICE', 'Single Invoice'),
    ]

    receipt_company_no = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    service_contract = models.ForeignKey('ServiceContract', on_delete=models.CASCADE, null=True, blank=True)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    collection_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)
    status_id = models.IntegerField(default=1)
    amount_total = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    payer_id = models.IntegerField()
    receiver_id = models.IntegerField()
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    amount_remaining = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    taxes = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    invoice_type = models.IntegerField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True, blank=True)
    utility_charge = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    reminders_only = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.CharField(max_length=255, null=True, blank=True)
    deleted_on = models.DateTimeField(null=True, blank=True)
    deleted_by = models.CharField(max_length=255, null=True, blank=True)
    excel_batch_id = models.IntegerField(null=True, blank=True)
    bulk_excel_id = models.IntegerField(null=True, blank=True)
    deleted = models.CharField(max_length=255, default='0')
    date_of_payment = models.DateField(null=True, blank=True)
    unit_id = models.IntegerField(null=True, blank=True)
    amount_original = models.DecimalField(max_digits=12, decimal_places=3, null=True, blank=True)
    vat = models.DecimalField(max_digits=12, decimal_places=3, null=True, blank=True)

    class Meta:
        db_table = 'contract_invoices'

    def __str__(self):
        return f"Invoice {self.id} - {self.name}"
    

class InvoicesLog(models.Model):
    invoice = models.ForeignKey('ContractInvoice', on_delete=models.CASCADE)
    invoice_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    invoice_short_uuid = models.CharField(max_length=255)
    invoice_url = models.URLField(max_length=255)
    active = models.BooleanField(default=True)
    url_open_date = models.DateTimeField(null=True, blank=True)
    last_notification_date = models.DateTimeField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    excel_batch_id = models.IntegerField(null=True, blank=True)
    bulk_excel_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'invoices_log'

    def __str__(self):
        return f"Log {self.id} - Invoice {self.invoice_id}"
    

class CompanyProjectUser(models.Model):
    actors_company = models.ForeignKey('Actor', on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'company_project_users'

    def __str__(self):
        return f"User {self.user_id} in Project {self.project_id}"
    

class EngineTemp(models.Model):
    ACTION_TYPE_CHOICES = [
        ('SEND_NOTIFICATION', 'Send Notification'),
        ('DATABASE_CHANGE', 'Database Change'),
    ]

    LANGUAGE_CHOICES = [
        ('ENGLISH', 'English'),
        ('ARABIC', 'Arabic'),
    ]

    SUBJECT_TYPE_CHOICES = [
        ('INVOICE', 'Invoice'),
        ('CONTRACT', 'Contract'),
        ('MESSAGE', 'Message'),
        ('CONTRACT_CONFIGURATION', 'Contract Configuration'),
        ('UNIT', 'Unit'),
    ]

    NOTIFY_TYPE_CHOICES = [
        ('B_4', 'Before 4'),
        ('B_3', 'Before 3'),
        ('B_2', 'Before 2'),
        ('B_1', 'Before 1'),
        ('A_4', 'After 4'),
        ('A_3', 'After 3'),
        ('A_2', 'After 2'),
        ('A_1', 'After 1'),
        ('TODAY', 'Today'),
        ('EXPIRED', 'Expired'),
        ('SOON', 'Soon'),
        ('FUTURE', 'Future'),
        ('EXPIRE_SOON', 'Expire Soon'),
        ('EXPIRED_CONTRACT', 'Expired Contract'),
    ]

    action_type = models.CharField(max_length=20, choices=ACTION_TYPE_CHOICES, default='SEND_NOTIFICATION')
    command = models.CharField(max_length=255, null=True, blank=True)
    query = models.TextField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=7, choices=LANGUAGE_CHOICES)
    subject_type = models.CharField(max_length=25, choices=SUBJECT_TYPE_CHOICES)
    subject_id = models.BigIntegerField(null=True, blank=True)
    client_name = models.CharField(max_length=255, null=True, blank=True)
    client_email = models.CharField(max_length=255, null=True, blank=True)
    client_phone = models.CharField(max_length=255, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_email = models.CharField(max_length=255, null=True, blank=True)
    company_phone = models.CharField(max_length=255, null=True, blank=True)
    trials = models.IntegerField(default=1)
    notify_day = models.IntegerField(default=0)
    notify_type = models.CharField(max_length=20, choices=NOTIFY_TYPE_CHOICES, null=True, blank=True)
    invoice_id = models.BigIntegerField(null=True, blank=True)
    contract_id = models.IntegerField(null=True, blank=True)
    notification_type_id = models.BigIntegerField(null=True, blank=True)
    sender_id = models.BigIntegerField(null=True, blank=True)
    receiver_id = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    company_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'engine_temp'

    def __str__(self):
        return f"{self.subject_type} - {self.client_name}"
    

class TriggerUploadSheet(models.Model):
    id = models.AutoField(primary_key=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'trigger_upload_sheet'

    def __str__(self):
        return f"TriggerUploadSheet(id={self.id}, active={self.active})"