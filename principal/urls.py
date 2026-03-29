from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProductViewSet, CityViewSet, StateViewSet, ZoneViewSet, DistrictViewSet, \
    BranchOfficeViewSet, MaritalStatusViewSet, DepartmentViewSet, EmployeeViewSet, SaleViewSet, MeansPaymentViewSet, \
    SalePaymentViewSet, ProductGroupViewSet, SupplierViewSet, SaleItemViewSet

router = DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'product', ProductViewSet)
router.register(r'city', CityViewSet)
router.register(r'state', StateViewSet)
router.register(r'zone', ZoneViewSet)
router.register(r'district', DistrictViewSet)
router.register(r'branchoffice', BranchOfficeViewSet)
router.register(r'maritalstatus', MaritalStatusViewSet)
router.register(r'department', DepartmentViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'sale', SaleViewSet)
router.register(r'meanspayment', MeansPaymentViewSet)
router.register(r'salepayment', SalePaymentViewSet)
router.register(r'productgroup', ProductGroupViewSet)
router.register(r'supplier', SupplierViewSet)
router.register(r'saleitem', SaleItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]