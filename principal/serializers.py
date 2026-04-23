from principal.models import (State, City, Zone, District, BranchOffice, MaritalStatus, Customer,
                              Department,
                              Employee, Sale, MeansPayment, SalePayment, ProductGroup, Supplier,
                              Product, SaleItem)

from rest_framework import serializers
from django.db import transaction


class StateSerializer(serializers.ModelSerializer):
	class Meta:
		model = State
		fields = ['id', 'abbreviation', 'name', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['id', 'created_at', 'modified_at']


class CitySerializer(serializers.ModelSerializer):
	class Meta:
		model = City
		fields = ['id', 'state', 'name', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['id', 'created_at', 'modified_at']


class ZoneSerializer(serializers.ModelSerializer):
	class Meta:
		model = Zone
		fields = ['id', 'name', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['id', 'created_at', 'modified_at']


class DistrictSerializer(serializers.ModelSerializer):
	class Meta:
		model = District
		fields = ['id', 'zone', 'city', 'name', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['id', 'created_at', 'modified_at']


class BranchOfficeSerializer(serializers.ModelSerializer):
	class Meta:
		model = BranchOffice
		fields = ['id', 'district', 'name', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['id', 'created_at', 'modified_at']


class MaritalStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = MaritalStatus
		fields = ['id', 'name', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['id', 'created_at', 'modified_at']


class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ['id', 'marital_status', 'district', 'name', 'income', 'gender', 'is_active',
		          'created_at', 'modified_at']
		read_only_fields = ['id', 'created_at', 'modified_at']


class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields = ['id', 'name', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['id', 'created_at', 'modified_at']


class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employee
		fields = ['id', 'district', 'department', 'marital_status', 'name', 'salary', 'admission',
		          'birth', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['id', 'created_at', 'modified_at']

class SaleItemReadSerializer(serializers.ModelSerializer):
	class Meta:
		model = SaleItem
		fields = ['product', 'quantity']
		read_only_fields = ['id', 'created_at', 'modified_at']

class SaleSerializer(serializers.ModelSerializer):
	items_data = serializers.JSONField(write_only=True)
	sale_items = SaleItemReadSerializer(many=True, read_only=True)

	class Meta:
		model = Sale
		fields = ['branch_office', 'employee', 'customer', 'sold_at', 'items_data', 'sale_items']
		read_only_fields = ['id', 'created_at', 'modified_at']

	def create(self, validated_data):
		items_data = validated_data.pop('items_data')
		print(items_data)

		with transaction.atomic():
			sale = Sale.objects.create(**validated_data)

			for item in items_data:
				SaleItem.objects.create(
					sale=sale,
					product_id=item['product_id'],
					quantity=item['quantity'],

				)
			sale.refresh_from_db()
			return sale


class MeansPaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model = MeansPayment
		fields = ['id', 'description', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['id', 'created_at', 'modified_at']


class SalePaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model = SalePayment
		fields = ['id', 'sale', 'means_payment', 'value', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['id', 'created_at', 'modified_at']


class ProductGroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductGroup
		fields = ['id', 'name', 'commission_percentage', 'gain_percentage', 'is_active',
		          'created_at', 'modified_at']
		read_only_fields = ['id', 'created_at', 'modified_at']


class SupplierSerializer(serializers.ModelSerializer):
	class Meta:
		model = Supplier
		fields = ['id', 'name', 'legal_document', 'is_active', 'created_at', 'modified_at']
		read_only_fields = ['id', 'created_at', 'modified_at']


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id', 'product_group', 'supplier', 'name', 'cost_price', 'sale_price',
		          'is_active', 'created_at', 'modified_at']
		read_only_fields = ['id', 'created_at', 'modified_at']


class SaleItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = SaleItem
		fields = '__all__'
		read_only_fields = ['id', 'created_at', 'modified_at']
