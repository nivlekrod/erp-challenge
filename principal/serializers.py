from principal.models import (State, City, Zone, District, BranchOffice, MaritalStatus, Customer, Department,
                              Employee, Sale, MeansPayment, SalePayment, ProductGroup, Supplier, Product, SaleItem)

from rest_framework import serializers


class StateSerializer(serializers.HyperlinkedModelSerializer):
    model = State
    fields = ['abbreviation', 'name', 'is_active', 'created_at', 'modified_at']


class CitySerializer(serializers.HyperlinkedModelSerializer):
    model = City
    fields = ['state', 'name']


class ZoneSerializer(serializers.HyperlinkedModelSerializer):
    model = Zone
    fields = ['name', 'is_active', 'created_at', 'modified_at']


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
    model = District
    fields = ['zone', 'city', 'name', 'is_active', 'created_at', 'modified_at']


class BranchOfficeSerializer(serializers.HyperlinkedModelSerializer):
    model = BranchOffice
    fields = ['district', 'name', 'is_active', 'created_at', 'modified_at']


class MaritalStatusSerializer(serializers.HyperlinkedModelSerializer):
    model = MaritalStatus
    fields = ['description', 'is_active', 'created_at', 'modified_at']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    model = Customer
    fields = ['marital_status', 'district', 'name', 'salary', 'gender', 'is_active', 'created_at', 'modified_at']


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    model = Department
    fields = ['name', 'is_active', 'created_at', 'modified_at']


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    model = Employee
    fields = ['manager', 'department', 'marital_status', 'name', 'salary', 'adminission', 'birth', 'is_active',
              'created_at', 'modified_at']


class SaleSerializer(serializers.HyperlinkedModelSerializer):
    model = Sale
    fields = ['branch_office', 'employee', 'customer', 'sold_at', 'is_active', 'created_at', 'modified_at']


class MeansPaymentSerializer(serializers.HyperlinkedModelSerializer):
    model = MeansPayment
    fields = ['description', 'is_active', 'created_at', 'modified_at']


class SalePaymentSerializer(serializers.HyperlinkedModelSerializer):
    model = SalePayment
    fields = ['sale', 'means_payment', 'value', 'is_active', 'created_at', 'modified_at']


class ProductGroupSerializer(serializers.HyperlinkedModelSerializer):
    model = ProductGroup
    fields = ['description', 'commission_percentage', 'gain_percentage', 'is_active', 'created_at', 'modified_at']


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
    model = Supplier
    fields = ['district', 'name', 'is_active', 'created_at', 'modified_at']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    model = Product
    fields = ['product_group', 'supplier', 'name', 'cost_price', 'sale_price', 'is_active', 'created_at',
              'modified_at']


class SaleItemSerializer(serializers.HyperlinkedModelSerializer):
    model = SaleItem
    fields = ['sale', 'product', 'quantity', 'sale_price', 'name', 'is_active', 'created_at', 'modified_at']
