from rest_framework import serializers
from .models import *

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'  # Include all fields from the table


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'  # Include all fields from the table


class UnitTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitType
        fields = '__all__'  # Include all fields from the table


class UnitStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitStatus
        fields = '__all__'  # Include all fields from the table


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'  # Include all fields from the table


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'  # Include all fields from the table


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'  # Include all fields from the table


class OwnerPayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerPayer
        fields = '__all__'  # Include all fields from the table

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Include all fields from the table

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'  # Include all fields from the table

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'  # Include all fields from the table


class BulkContractExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkContractExcel
        fields = '__all__'  # Include all fields from the table


class OriginalOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = OriginalOwner
        fields = '__all__'  # Include all fields from the table


class ContractTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractType
        fields = '__all__'  # Include all fields from the table


class ContractConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractConfiguration
        fields = '__all__'  # Include all fields from the table


class ServiceContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceContract
        fields = '__all__'  # Include all fields from the table


class ServiceContractNotificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceContractNotificationType
        fields = '__all__'  # Include all fields from the table

class InvoiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceType
        fields = '__all__'  # Include all fields from the table

class ContractInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractInvoice
        fields = '__all__'  # Include all fields from the table



class InvoicesLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoicesLog
        fields = '__all__'  # Include all fields from the table


class OwnerUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnerUnit
        fields = '__all__'  # Include all fields from the table


class CompanyProjectUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProjectUser
        fields = '__all__'  # Include all fields from the table