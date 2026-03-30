from django.db import models

# Create your models here.
class State(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    name = models.CharField(
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False,
    )

    abbreviation = models.CharField(
        db_column='tx_abbreviation',
        max_length=2,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
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
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
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
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'zone'
        verbose_name = 'Zone'
        verbose_name_plural = 'Zones'
        managed = True

    def __str__(self):
        return f"Zone {self.id} {str(self.name)}"

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
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
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
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'branch_office'
        verbose_name = 'Branch Office'
        verbose_name_plural = 'Branch Offices'
        managed = True

    def __str__(self):
        return f"Branch Office {self.id} {self.name}"

class MaritalStatus(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    description = models.CharField(
        db_column='tx_description',
        max_length=54,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'marital_status'
        verbose_name = 'Marital Status'
        verbose_name_plural = 'Marital Statuses'
        managed = True

    def __str__(self):
        return f"Marital Status {self.id} {self.description}"

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
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False
    )

    salary = models.DecimalField(
        db_column='nb_salary',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False,
    )

    gender = models.CharField(
        db_column='cs_gender',
        max_length=1,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
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
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
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

    manager = models.ForeignKey(
        to='self',
        on_delete=models.SET_NULL,
        db_column='id_manager',
        null=True,
        blank=True,
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
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False
    )

    salary = models.DecimalField(
        db_column='nb_salary',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False,
    )

    adminission = models.DateField(
        db_column='dt_adminission',
        null=False,
        blank=False
    )

    birth = models.DateField(
        db_column='dt_birth',
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
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
        db_column='id_branch_office',
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
        db_column='dt_sale',
        null=True,
        blank=True
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
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
        db_column='tx_description',
        max_length=54,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'means_payment'
        verbose_name = 'Means Payment'
        verbose_name_plural = 'Means Payments'
        managed = True

    def __str__(self):
        return f"Means Payment {self.id} {str(self.description)}"

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
        db_column='nb_value',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False,
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'means_payment_sale'
        verbose_name = 'Sale Payment'
        verbose_name_plural = 'Sale Payments'
        managed = True

    def __str__(self):
        return f"Sale Payment {self.id} {str(self.means_payment)}"

class ProductGroup(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    description = models.CharField(
        db_column='tx_description',
        max_length=54,
        null=False,
        blank=False
    )

    commission_percentage = models.DecimalField(
        db_column='nb_commission_percentage',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False
    )

    gain_percentage = models.DecimalField(
        db_column='nb_gain_percentage',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'product_group'
        verbose_name = 'Product Group'
        verbose_name_plural = 'Product Groups'
        managed = True

    def __str__(self):
        return f"Product Group {self.id} {str(self.description)}"

class Supplier(models.Model):
    id = models.AutoField(primary_key=True, null=False)

    district = models.ForeignKey(
        to='District',
        on_delete=models.CASCADE,
        db_column='id_district',
        null=False,
        blank=False,
        related_name='suppliers'
    )

    name = models.CharField(
        db_column='tx_name',
        max_length=54,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'supplier'
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
        managed = True

    def __str__(self):
        return f"Supplier {self.id} - {str(self.name)} - {str(self.district)}"

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
        db_column='tx_name',
        max_length=104,
        null=False,
        blank=False
    )

    cost_price = models.DecimalField(
        db_column='nb_cost_price',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False
    )

    sale_price = models.DecimalField(
        db_column='nb_sale_price',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        managed = True

    def __str__(self):
        return f"Product {self.id} - {str(self.name)}"

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
        db_column='nb_quantity',
        max_digits=10,
        decimal_places=3,
        null=False,
        blank=False
    )

    sale_price = models.DecimalField(
        db_column='nb_sale_price',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False
    )

    subtotal = models.DecimalField(
        db_column='nb_subtotal',
        max_digits=10,
        decimal_places=4,
        null=False,
        blank=False
    )

    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        null=False,
        blank=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column='dt_created_at',
        null=False,
        blank=False
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        db_column='dt_modified_at',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'sale_item'
        verbose_name = 'Sale Item'
        verbose_name_plural = 'Sale Items'
        managed = True

    def __str__(self):
        return f"Sale Item {self.id} - {str(self.sale)}"