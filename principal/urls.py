from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, ProductViewSet, CityViewSet, StateViewSet, ZoneViewSet, DistrictViewSet, \
    BranchOfficeViewSet, MaritalStatusViewSet, DepartmentViewSet, EmployeeViewSet, SaleViewSet, MeansPaymentViewSet, \
    SalePaymentViewSet, ProductGroupViewSet, SupplierViewSet, SaleItemViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'cities', CityViewSet)
router.register(r'states', StateViewSet)
router.register(r'zones', ZoneViewSet)
router.register(r'districts', DistrictViewSet)
router.register(r'branch-offices', BranchOfficeViewSet)
router.register(r'marital-statuses', MaritalStatusViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'means-payments', MeansPaymentViewSet)
router.register(r'sale-payments', SalePaymentViewSet)
router.register(r'product-groups', ProductGroupViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'sale-items', SaleItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
]