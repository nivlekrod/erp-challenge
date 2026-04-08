from rest_framework import viewsets
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

    def create(self, request, *args, **kwargs):
        instance = super(StateViewSet, self).create(request, *args, **kwargs)
        tasks.create_file.apply_async([instance.data.get('id')])
        return instance

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class ZoneViewSet(viewsets.ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class BranchOfficeViewSet(viewsets.ModelViewSet):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficeSerializer

class MaritalStatusViewSet(viewsets.ModelViewSet):
    queryset = MaritalStatus.objects.all()
    serializer_class = MaritalStatusSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class MeansPaymentViewSet(viewsets.ModelViewSet):
    queryset = MeansPayment.objects.all()
    serializer_class = MeansPaymentSerializer

class SalePaymentViewSet(viewsets.ModelViewSet):
    queryset = SalePayment.objects.all()
    serializer_class = SalePaymentSerializer

class ProductGroupViewSet(viewsets.ModelViewSet):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SaleItemViewSet(viewsets.ModelViewSet):
    queryset = SaleItem.objects.all()
    serializer_class = SaleItemSerializer




