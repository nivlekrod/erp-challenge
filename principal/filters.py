from django_filters import filterset
from principal import models


class StateFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr='unaccent__icontains')
    abbreviation = filterset.CharFilter(lookup_expr='unaccent__icontains')

    class Meta:
        model = models.State
        fields = ['is_active']

class CityFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr='unaccent__icontains')

    class Meta:
        model = models.City
        fields = ['state', 'is_active']

class ZoneFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr='unaccent__icontains')

    class Meta:
        model = models.Zone
        fields = ['is_active']

class DistrictFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr='unaccent__icontains')

    class Meta:
        model = models.District
        fields = ['zone', 'city', 'is_active']

class BranchOfficeFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr='unaccent__icontains')

    class Meta:
        model = models.BranchOffice
        fields = ['district', 'is_active']



class MaritalStatusFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr='unaccent__icontains')

    class Meta:
        model = models.MaritalStatus
        fields = ['is_active']

class DepartmentFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr='unaccent__icontains')

    class Meta:
        model = models.Department
        fields = ['is_active']

class CustomerFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr='unaccent__icontains')

    class Meta:
        model = models.Customer
        fields = ['marital_status', 'district', 'gender', 'is_active']

class EmployeeFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr='unaccent__icontains')

    class Meta:
        model = models.Employee
        fields = ['district', 'department', 'marital_status', 'gender', 'is_active']


class ProductGroupFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr='unaccent__icontains')

    class Meta:
        model = models.ProductGroup
        fields = ['is_active']

class SupplierFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr='unaccent__icontains')
    legal_document = filterset.CharFilter(lookup_expr='unaccent__icontains')

    class Meta:
        model = models.Supplier
        fields = ['is_active']

class ProductFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr='unaccent__icontains')

    class Meta:
        model = models.Product
        fields = ['product_group', 'supplier', 'is_active']

class MeansPaymentFilter(filterset.FilterSet):
    description = filterset.CharFilter(lookup_expr='unaccent__icontains')

    class Meta:
        model = models.MeansPayment
        fields = ['is_active']