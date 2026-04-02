from django.contrib import admin

from principal import models

# Register your models here.
@admin.register(models.State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'abbreviation', 'is_active', 'created_at', 'modified_at']
    search_fields = ['name', 'abbreviation']


@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'state', 'name', 'is_active', 'created_at', 'modified_at']
    search_fields = ['name', 'state__name']


@admin.register(models.Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_at', 'modified_at']
    search_fields = ['name']


@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['id', 'zone', 'city', 'name', 'is_active', 'created_at', 'modified_at']
    search_fields = ['name', 'zone__name', 'city__name']


@admin.register(models.BranchOffice)
class BranchOfficeAdmin(admin.ModelAdmin):
    list_display = ['id', 'district', 'name', 'is_active', 'created_at', 'modified_at']
    search_fields = ['name', 'district__name']


@admin.register(models.MaritalStatus)
class MaritalStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_at', 'modified_at']
    search_fields = ['name']


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'marital_status', 'district', 'income', 'gender', 'is_active', 'created_at', 'modified_at']
    search_fields = ['name', 'gender', 'district__name', 'marital_status__name']


@admin.register(models.Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_at', 'modified_at']
    search_fields = ['name']


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'district', 'department', 'marital_status', 'salary', 'admission', 'birth', 'is_active', 'created_at', 'modified_at']
    search_fields = ['name', 'department__name', 'marital_status__name', 'district__name']


@admin.register(models.Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['id', 'branch_office', 'employee', 'customer', 'sold_at', 'is_active', 'created_at', 'modified_at']
    search_fields = ['customer__name', 'employee__name', 'branch_office__name']


@admin.register(models.MeansPayment)
class MeansPaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'description', 'is_active', 'created_at', 'modified_at']
    search_fields = ['description']


@admin.register(models.SalePayment)
class SalePaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'sale', 'means_payment', 'value', 'is_active', 'created_at', 'modified_at']
    search_fields = ['sale__customer__name', 'means_payment__description']


@admin.register(models.ProductGroup)
class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'commission_percentage', 'gain_percentage', 'is_active', 'created_at', 'modified_at']
    search_fields = ['name']


@admin.register(models.Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'legal_document', 'is_active', 'created_at', 'modified_at']
    search_fields = ['name', 'legal_document']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'product_group', 'supplier', 'cost_price', 'sale_price', 'is_active', 'created_at', 'modified_at']
    search_fields = ['name', 'product_group__name', 'supplier__name']


@admin.register(models.SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'sale', 'product', 'quantity', 'is_active', 'created_at', 'modified_at']
    search_fields = ['sale__customer__name', 'product__name']