from principal.models import (State, City, Zone, District, BranchOffice, MaritalStatus, Customer, Department,
							  Employee, Sale, MeansPayment, SalePayment, ProductGroup, Supplier, Product, SaleItem)

from rest_framework import serializers


class StateSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = State
		fields = ['abbreviation', 'name', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['created_at', 'modified_at']


class CitySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = City
		fields = ['state', 'name']
		read_only_fields = ['created_at', 'modified_at']


class ZoneSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Zone
		fields = ['name', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['created_at', 'modified_at']


class DistrictSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = District
		fields = ['zone', 'city', 'name', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['created_at', 'modified_at']


class BranchOfficeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = BranchOffice
		fields = ['district', 'name', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['created_at', 'modified_at']


class MaritalStatusSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MaritalStatus
		fields = ['description', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['created_at', 'modified_at']


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Customer
		fields = ['marital_status', 'district', 'name', 'salary', 'gender', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['created_at', 'modified_at']


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Department
		fields = ['name', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['created_at', 'modified_at']


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Employee
		fields = ['manager', 'department', 'marital_status', 'name', 'salary', 'adminission', 'birth', 'is_active',
				  'created_at', 'modified_at']
		read_only_fields = ['created_at', 'modified_at']


class SaleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Sale
		fields = ['branch_office', 'employee', 'customer', 'sold_at', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['created_at', 'modified_at']


class MeansPaymentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MeansPayment
		fields = ['description', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['created_at', 'modified_at']


class SalePaymentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SalePayment
		fields = ['sale', 'means_payment', 'value', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['created_at', 'modified_at']


class ProductGroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = ProductGroup
		fields = ['description', 'commission_percentage', 'gain_percentage', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['created_at', 'modified_at']


class SupplierSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Supplier
		fields = ['district', 'name', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['created_at', 'modified_at']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = ['product_group', 'supplier', 'name', 'cost_price', 'sale_price', 'is_active', 'created_at',
				  'modified_at']
		read_only_fields = ['created_at', 'modified_at']


class SaleItemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SaleItem
		fields = ['sale', 'product', 'quantity', 'sale_price', 'subtotal', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['created_at', 'modified_at']
