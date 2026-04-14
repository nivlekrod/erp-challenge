from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from principal.filters import StateFilter, CityFilter, DistrictFilter, ZoneFilter, BranchOfficeFilter, \
    MaritalStatusFilter, CustomerFilter, DepartmentFilter, ProductGroupFilter, ProductFilter, MeansPaymentFilter, \
    EmployeeFilter, SupplierFilter

from .filters import StateFilter
from .models import Customer, Product, City, State, Zone, District, BranchOffice, MaritalStatus, Department, Employee, \
    Sale, MeansPayment, SalePayment, ProductGroup, Supplier, SaleItem
from .serializers import CustomerSerializer, ProductSerializer, CitySerializer, StateSerializer, ZoneSerializer, \
    DistrictSerializer, BranchOfficeSerializer, MaritalStatusSerializer, DepartmentSerializer, EmployeeSerializer, \
    SaleSerializer, MeansPaymentSerializer, SalePaymentSerializer, ProductGroupSerializer, SupplierSerializer, \
    SaleItemSerializer
from principal import tasks

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filterset_class = StateFilter

    def create(self, request, *args, **kwargs):
        instance = super(StateViewSet, self).create(request, *args, **kwargs)
        tasks.create_file.apply_async([instance.data.get('id')])
        return instance

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filterset_class = CityFilter

class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    filterset_class = ZoneFilter

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    filterset_class = DistrictFilter

class BranchOfficeViewSet(viewsets.ModelViewSet):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficeSerializer
    filterset_class = BranchOfficeFilter

class MaritalStatusViewSet(viewsets.ModelViewSet):
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer
    filterset_class = MaritalStatusFilter

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_class = CustomerFilter

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filterset_class = DepartmentFilter

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilter

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filterset_fields = ['branch_office', 'employee', 'customer', 'is_active']

class MeansPaymentViewSet(viewsets.ModelViewSet):
    queryset = MeansPayment.objects.all()
    serializer_class = MeansPaymentSerializer
    filterset_class = MeansPaymentFilter

class SalePaymentViewSet(viewsets.ModelViewSet):
    queryset = SalePayment.objects.all()
    serializer_class = SalePaymentSerializer
    filterset_fields = ['sale', 'means_payment','is_active']

class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer
    filterset_class = ProductGroupFilter

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filterset_class = SupplierFilter

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

class SaleItemViewSet(viewsets.ModelViewSet):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer
    filterset_fields = ['sale', 'product', 'is_active']




