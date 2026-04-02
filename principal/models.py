from django.db import models

# Create your models here.
class State(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        blank=False,
    )

    abbreviation = models.CharField(
        db_column='abbreviation',
        max_length=2,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'state'
        verbose_name = 'State'
        verbose_name_plural = 'States'
        managed = True

    def __str__(self):
        return f"State {self.id} - {self.name}"

class City(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    state = models.ForeignKey(
        to='State',
        on_delete=models.CASCADE,
        db_column='id_state',
        null=False,
        blank=False,
        related_name='cities'
    )

    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'city'
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        managed = True
        unique_together = ('state', 'name')

    def __str__(self):
        return f"City {self.id} - State: {self.state.name}"

class Zone(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'zone'
        verbose_name = 'Zone'
        verbose_name_plural = 'Zones'
        managed = True

    def __str__(self):
        return f"Zone {self.id} {self.name}"

class District(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    zone = models.ForeignKey(
        to='Zone',
        on_delete=models.CASCADE,
        db_column='id_zone',
        null=False,
        blank=False,
        related_name='districts'
    )

    city = models.ForeignKey(
        to='City',
        on_delete=models.CASCADE,
        db_column='id_city',
        null=False,
        blank=False,
        related_name='districts'
    )

    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'district'
        verbose_name = 'District'
        verbose_name_plural = 'Districts'
        managed = True
        unique_together = ('zone', 'city', 'name')

    def __str__(self):
        return f"District {self.id} - City: {self.city.name} - Zone: {self.zone.name}"

class BranchOffice(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    district = models.ForeignKey(
        to='District',
        on_delete=models.CASCADE,
        db_column='id_district',
        null=False,
        blank=False,
        related_name='branch_offices'
    )

    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'branch'
        verbose_name = 'Branch Office'
        verbose_name_plural = 'Branch Offices'
        managed = True

    def __str__(self):
        return f"Branch Office {self.id} {self.name}"

class MaritalStatus(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'marital_status'
        verbose_name = 'Marital Status'
        verbose_name_plural = 'Marital Statuses'
        managed = True

    def __str__(self):
        return f"Marital Status {self.id} {self.name}"

class Customer(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    marital_status = models.ForeignKey(
        to='MaritalStatus',
        on_delete=models.PROTECT,
        db_column='id_marital_status',
        null=False,
        blank=False,
        related_name='customers'
    )

    district = models.ForeignKey(
        to='District',
        on_delete=models.CASCADE,
        db_column='id_district',
        null=False,
        blank=False,
        related_name='customers'
    )

    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        blank=False
    )

    income = models.DecimalField(
        db_column='income',
        max_digits=16,
        decimal_places=2,
        null=False,
        blank=False
    )

    GENDER_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    ]
    gender = models.CharField(
        db_column='gender',
        max_length=1,
        choices=GENDER_CHOICES,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'customer'
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        managed = True

    def __str__(self):
        return f"Customer {self.id}: {self.name}"

class Department(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'department'
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        managed = True

    def __str__(self):
        return f"Department {self.id}"

class Employee(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    district = models.ForeignKey(
        to='District',
        on_delete=models.CASCADE,
        db_column='id_district',
        null=False,
        blank=False,
        related_name='employees'
    )

    department = models.ForeignKey(
        to='Department',
        on_delete=models.CASCADE,
        db_column='id_department',
        null=False,
        blank=False,
        related_name='employees'
    )

    marital_status = models.ForeignKey(
        to='MaritalStatus',
        on_delete=models.PROTECT,
        db_column='id_marital_status',
        null=False,
        blank=False,
        related_name='employees'
    )

    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        blank=False
    )

    salary = models.DecimalField(
        db_column='salary',
        max_digits=16,
        decimal_places=2,
        null=False,
        blank=False,
    )

    admission = models.DateField(
        db_column='admission_date',
        null=False,
        blank=False
    )

    birth = models.DateField(
        db_column='birth_date',
        null=False,
        blank=False
    )

    GENDER_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    ]
    gender = models.CharField(
        db_column='gender',
        max_length=1,
        choices=GENDER_CHOICES,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'employee'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        managed = True

    def __str__(self):
        return f"Employee {self.name}"

class Sale(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    branch_office = models.ForeignKey(
        to='BranchOffice',
        on_delete=models.CASCADE,
        db_column='id_branch',
        null=False,
        blank=False,
        related_name='sales'
    )

    employee = models.ForeignKey(
        to='Employee',
        on_delete=models.CASCADE,
        db_column='id_employee',
        null=False,
        blank=False,
        related_name='sales'
    )

    customer = models.ForeignKey(
        to='Customer',
        on_delete=models.CASCADE,
        db_column='id_customer',
        null=False,
        blank=False,
        related_name='sales'
    )

    sold_at = models.DateTimeField(
        db_column='date',
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'sale'
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
        managed = True

    def __str__(self):
        return f"Sale {self.id} - Customer: {self.customer.name}"

class MeansPayment(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    description = models.CharField(
        db_column='description',
        max_length=64,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'means_payment'
        verbose_name = 'Means Payment'
        verbose_name_plural = 'Means Payments'
        managed = True

    def __str__(self):
        return f"Means Payment {self.id} {self.description}"

class SalePayment(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    sale = models.ForeignKey(
        to='Sale',
        on_delete=models.CASCADE,
        db_column='id_sale',
        null=False,
        blank=False,
        related_name='sale_payments'
    )

    means_payment = models.ForeignKey(
        to='MeansPayment',
        on_delete=models.PROTECT,
        db_column='id_means_payment',
        null=False,
        blank=False,
        related_name='sale_payments'
    )

    value = models.DecimalField(
        db_column='value',
        max_digits=16,
        decimal_places=2,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'means_payment_sale'
        verbose_name = 'Sale Payment'
        verbose_name_plural = 'Sale Payments'
        managed = True

    def __str__(self):
        return f"Sale Payment {self.id} {self.means_payment}"

class ProductGroup(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        blank=False
    )

    commission_percentage = models.DecimalField(
        db_column='commission_percentage',
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False
    )

    gain_percentage = models.DecimalField(
        db_column='gain_percentage',
        max_digits=5,
        decimal_places=2,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'product_group'
        verbose_name = 'Product Group'
        verbose_name_plural = 'Product Groups'
        managed = True

    def __str__(self):
        return f"Product Group {self.id} {self.name}"

class Supplier(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        blank=False
    )

    legal_document = models.CharField(
        db_column='legal_document',
        max_length=20,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'supplier'
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        managed = True

    def __str__(self):
        return f"Supplier {self.id} - {self.name} - {self.legal_document}"

class Product(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    product_group = models.ForeignKey(
        to='ProductGroup',
        on_delete=models.PROTECT,
        db_column='id_product_group',
        null=False,
        blank=False,
        related_name='products'
    )

    supplier = models.ForeignKey(
        to='Supplier',
        on_delete=models.CASCADE,
        db_column='id_supplier',
        null=False,
        blank=False,
        related_name='products'
    )

    name = models.CharField(
        db_column='name',
        max_length=64,
        null=False,
        blank=False
    )

    cost_price = models.DecimalField(
        db_column='cost_price',
        max_digits=16,
        decimal_places=2,
        null=False,
        blank=False
    )

    sale_price = models.DecimalField(
        db_column='sale_price',
        max_digits=16,
        decimal_places=2,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        managed = True

    def __str__(self):
        return f"Product {self.id} - {self.name}"

class SaleItem(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    sale = models.ForeignKey(
        to='Sale',
        on_delete=models.CASCADE,
        db_column='id_sale',
        null=False,
        blank=False,
        related_name='sale_items'
    )

    product = models.ForeignKey(
        to='Product',
        on_delete=models.CASCADE,
        db_column='id_product',
        null=False,
        blank=False,
        related_name='sale_items'
    )

    quantity = models.DecimalField(
        db_column='quantity',
        max_digits=16,
        decimal_places=3,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'sale_item'
        verbose_name = 'Sale Item'
        verbose_name_plural = 'Sale Items'
        managed = True

    def __str__(self):
        return f"Sale Item {self.id} - {self.sale}"