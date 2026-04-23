from principal import models
from django.db.models import Avg, Max, Exists, OuterRef, Subquery, Min, Count, Sum, F

"""Atividade para treinar queries"""

# Q1 - Liste o nome e a renda (income) de todos os clientes do sexo feminino (gender = 'F') com renda maior que 5000.
def get_female_customers_by_income():
    return models.Customer.objects.filter(
        gender='F',
        income__gt=5000
    ).values('name', 'income')

# Q2 - Mostre os funcionários admitidos após 2020-01-01 que possuem salário entre 3000 e 7000.
def get_employees_by_admission_and_salary():
    return models.Employee.objects.filter(
        admission_date__gt='2020-01-01',
        salary__range=(3000, 7000)
    ).values('name', 'admission_date', 'salary')

# Q3 - Liste os produtos cujo sale_price seja maior que 100 e cost_price menor que 80.
def list_products_by_sale_cost_price():
    return list(models.Product.objects.filter(
        sale_price__gt=100,
        cost_price__lt=80
    ).distinct().values('name', 'sale_price', 'cost_price'))

# Q4 - Mostre os fornecedores cujo legal_document comece com 12.
def get_suppliers_by_legal_document():
    return models.Supplier.objects.filter(
        legal_document__startswith='12'
    ).values('name', 'legal_document')

# Q5 - Liste os clientes que pertencem a um determinado distrito, por exemplo, id_district = 3.
def list_customers_by_district():
    return list(models.Customer.objects.filter(
        district_id=3
    ).values('name', 'district'))

# Q6 - Mostre os itens de venda com quantidade maior ou igual a 10.
def get_sale_items_by_quantity():
    return models.SaleItem.objects.filter(
        quantity__gte=10
    ).values('product__name', 'quantity')

# Q7 - Liste todos os clientes ordenados por renda em ordem decrescente.
def list_customers_ordered_by_income():
    return list(models.Customer.objects.order_by('-income')
                .values('name', 'income'))

# Q8 - Mostre os funcionários ordenados primeiro por salário decrescente e depois por nome em ordem alfabética.
def get_employees_ordered_by_income_and_name():
    return (models.Employee.objects.order_by('-salary', 'name')
            .values('name', 'salary'))

# Q9 - Liste os produtos ordenados pelo preço de venda crescente.
def list_products_by_sale_price():
    return list(models.Product.objects.order_by('sale_price')
                .values('name', 'sale_price'))

# Q10 - Mostre as vendas mais recentes primeiro, ordenadas pela coluna date da tabela sale.
def get_sale_ordered_by_date():
    return models.Sale.objects.order_by('-sold_at').values('id', 'sold_at')

# Q11 - Liste os estados ordenados pela sigla (abbreviation) em ordem alfabética.
def list_state_ordered_by_abbr():
    return list(models.State.objects.order_by('abbreviation')
                .values('name', 'abbreviation'))

# Q12 - Liste o nome dos clientes e o nome do distrito em que moram.
def list_customers_and_district():
    return list(models.Customer.objects.select_related('district')
                .values('name', 'district__name'))

# Q13 - Mostre o nome dos distritos, das cidades e dos estados correspondentes.
def get_district_city_state():
    return (models.District.objects.select_related('city__state')
            .values('name', 'city__name', 'city__state__name'))

# Q14 - Liste o nome dos funcionários junto com o nome do departamento.
def list_employees_and_department():
    return list(models.Employee.objects.select_related('department')
                .values('name', 'department__name'))

# Q15 - Mostre o nome dos produtos junto com o nome do fornecedor e do grupo de produto.
def get_product_supplier_and_product_group():
    return (models.Product.objects.select_related('supplier__product_group')
            .values('name', 'supplier__name', 'product_group__name'))

# Q16 - Liste as vendas mostrando: id da venda, data, nome do cliente, nome do funcionário e nome da filial.
def get_sales_with_details():
    return list(models.Sale.objects.select_related('customer', 'employee', 'branch_office')
                .values('id', 'sold_at', 'customer__name', 'employee__name', 'branch_office__name'))

# Q17 - Mostre os itens de venda com: id da venda, nome do produto, quantidade e preço de venda do produto.
def get_sale_items_with_product():
    return (models.SaleItem.objects.select_related('sale', 'product')
                .values('sale__id', 'product__name', 'quantity', 'sale_price'))

# Q18 - Liste os clientes com o seu estado civil, usando customer e marital_status.
def get_customers_with_marital_status():
    return list(models.Customer.objects.select_related('marital_status')
                .values('name', 'marital_status__description'))

# Q19 - Liste os funcionários com distrito, cidade e estado onde estão vinculados.
def get_employees_with_location():
    return list(models.Employee.objects.select_related('district__city__state')
                .values('name', 'district__name', 'district__city__name', 'district__city__state__name'))


# Q20 - Liste os produtos com preço de venda maior que a média de preço de venda de todos os produtos.
def get_products_above_avg_price():
    avg_price = models.Product.objects.aggregate(Avg('sale_price'))['sale_price__avg']
    return list(models.Product.objects.filter(sale_price__gt=avg_price)
                .values('name', 'sale_price'))


# Q21 - Mostre os funcionários que recebem salário acima da média salarial da empresa.
def get_employees_above_avg_salary():
    avg_salary = models.Employee.objects.aggregate(Avg('salary'))['salary__avg']
    return models.Employee.objects.filter(salary__gt=avg_salary).values('name', 'salary')


# Q22 - Liste os clientes cuja renda seja maior do que a renda média dos clientes do mesmo sexo.
def get_customers_above_avg_income_by_gender():
    avg_income_by_gender = (models.Customer.objects
                            .filter(gender=OuterRef('gender'))
                            .values('gender')
                            .annotate(avg=Avg('income'))
                            .values('avg'))

    return list(models.Customer.objects
                .filter(income__gt=Subquery(avg_income_by_gender))
                .values('name', 'gender', 'income'))


# Q23 - Mostre o produto mais caro da tabela product.
def get_most_expensive_product():
    max_price = models.Product.objects.aggregate(Max('sale_price'))['sale_price__max']
    return models.Product.objects.filter(sale_price=max_price).values('name', 'sale_price')


# Q24 - Liste as filiais que realizaram pelo menos uma venda.
def get_branch_offices_with_sales():
    branches_with_sales = models.Sale.objects.values('branch_office')
    return list(models.BranchOffice.objects.filter(id__in=branches_with_sales)
                .values('name'))


# Q25 - Mostre os clientes que já realizaram compras, usando subquery com EXISTS.
def get_customers_with_purchases():
    sales = models.Sale.objects.filter(customer=OuterRef('pk'))
    return models.Customer.objects.filter(Exists(sales)).values('name')


# Q26 - Liste os funcionários que nunca participaram de uma venda.
def get_employees_without_sales():
    sales = models.Sale.objects.filter(employee=OuterRef('pk'))
    return list(models.Employee.objects.filter(~Exists(sales))
                .values('name'))


# Q27 - Mostre os fornecedores que fornecem produtos com preço de venda acima de 500.
def get_suppliers_with_expensive_products():
    suppliers_with_products = models.Product.objects.filter(
        sale_price__gt=500
    ).values('supplier')
    return models.Supplier.objects.filter(id__in=suppliers_with_products).values('name')


# Q28 - Liste os produtos cujo preço de venda seja maior que o preço médio dos produtos do mesmo grupo.
def get_products_above_avg_price_by_group():
    avg_price_by_group = (models.Product.objects
                          .filter(product_group=OuterRef('product_group'))
                          .values('product_group')
                          .annotate(avg=Avg('sale_price'))
                          .values('avg'))

    return list(models.Product.objects
                .filter(sale_price__gt=Subquery(avg_price_by_group))
                .values('name', 'product_group__name', 'sale_price'))

# Q29 - Conte quantos clientes existem por sexo.
def get_customer_count_by_gender():
    return (models.Customer.objects
            .values('gender')
            .annotate(total=Count('id')))

# Q30 - Mostre a média de renda dos clientes por sexo.
def get_avg_income_by_gender():
    return (models.Customer.objects
            .values('gender')
            .annotate(avg_income=Avg('income')))

# Q31 - Conte quantos funcionários existem em cada departamento.
def get_employee_count_by_department():
    return (models.Employee.objects
            .values('department__name')
            .annotate(total=Count('id')))

# Q32 - Mostre o maior e o menor salário dos funcionários.
def get_max_min_salary():
    return models.Employee.objects.aggregate(
        max_salary=Max('salary'),
        min_salary=Min('salary')
    )

# Q33 - Calcule a média salarial por departamento.
def get_avg_salary_by_department():
    return (models.Employee.objects
            .values('department__name')
            .annotate(avg_salary=Avg('salary')))

# Q34 - Conte quantas vendas cada filial realizou.
def get_sale_count_by_branch():
    return (models.Sale.objects
            .values('branch_office__name')
            .annotate(total=Count('id')))

# Q35 - Mostre a quantidade total vendida por produto.
def get_total_quantity_by_product():
    return (models.SaleItem.objects
            .values('product__name')
            .annotate(total_quantity=Sum('quantity')))

# Q36 - Calcule o faturamento bruto por produto, considerando quantidade * sale_price.
def get_gross_revenue_by_product():
    return (models.SaleItem.objects
            .values('product__name')
            .annotate(gross_revenue=Sum(F('quantity') * F('product__sale_price'))))

# Q37 - Mostre o total de vendas realizadas por cada funcionário.
def get_sale_count_by_employee():
    return (models.Sale.objects
            .values('employee__name')
            .annotate(total=Count('id')))

# Q38 - Conte quantos clientes existem em cada distrito.
def get_customer_count_by_district():
    return (models.Customer.objects
            .values('district__name')
            .annotate(total=Count('id')))

# Q39 - Mostre a média de preço de venda dos produtos por grupo de produto.
def get_avg_sale_price_by_product_group():
    return (models.Product.objects
            .values('product_group__name')
            .annotate(avg_sale_price=Avg('sale_price')))

# Q40 - Exiba o maior preço de venda por fornecedor.
def get_max_sale_price_by_supplier():
    return (models.Product.objects
            .values('supplier__name')
            .annotate(max_sale_price=Max('sale_price')))


# Q41 - Liste os departamentos que possuem mais de 5 funcionários.
def get_departments_with_more_than_5_employees():
    return list(models.Department.objects
                .annotate(total=Count('employees'))
                .filter(total__gt=5)
                .values('name', 'total'))


# Q42 - Mostre os produtos cuja quantidade total vendida seja maior que 100 unidades.
def get_products_with_quantity_sold_gt_100():
    return (models.SaleItem.objects
            .values('product__name')
            .annotate(total_quantity=Sum('quantity'))
            .filter(total_quantity__gt=100))


# Q43 - Liste as filiais que realizaram mais de 50 vendas.
def get_branches_with_more_than_50_sales():
    return list(models.BranchOffice.objects
                .annotate(total=Count('sales'))
                .filter(total__gt=50)
                .values('name', 'total'))


# Q44 - Mostre os fornecedores que possuem mais de 3 produtos cadastrados.
def get_suppliers_with_more_than_3_products():
    return (models.Supplier.objects
            .annotate(total=Count('products'))
            .filter(total__gt=3)
            .values('name', 'total'))


# Q45 - Liste os grupos de produtos cuja média de preço de venda seja maior que 200.
def get_product_groups_with_avg_price_gt_200():
    return list(models.ProductGroup.objects
                .annotate(avg_price=Avg('products__sale_price'))
                .filter(avg_price__gt=200)
                .values('name', 'avg_price'))


# Q46 - Mostre os funcionários que participaram de mais de 10 vendas.
def get_employees_with_more_than_10_sales():
    return (models.Employee.objects
            .annotate(total=Count('sales'))
            .filter(total__gt=10)
            .values('name', 'total'))


# Q47 - Liste os 5 clientes com maior renda, mostrando também o distrito e a cidade onde moram.
def get_top_5_customers_by_income():
    return list(models.Customer.objects
                .select_related('district__city')
                .values('name', 'income', 'district__name', 'district__city__name')
                .order_by('-income')[:5])


# Q48 - Mostre o total vendido por filial, ordenando da filial com maior faturamento para a menor.
def get_total_revenue_by_branch():
    return (models.SaleItem.objects
            .values('sale__branch_office__name')
            .annotate(total_revenue=Sum(F('quantity') * F('product__sale_price')))
            .order_by('-total_revenue'))


# Q49 - Liste o nome do funcionário, o departamento e a quantidade de vendas realizadas, exibindo apenas funcionários com mais de 5 vendas.
def get_employees_with_department_and_sales():
    return list(models.Employee.objects
                .values('name', 'department__name')
                .annotate(total_sales=Count('sales'))
                .filter(total_sales__gt=5)
                .order_by('-total_sales'))


# Q50 - Mostre o nome do produto, grupo do produto, fornecedor e total vendido, ordenando do mais vendido para o menos vendido.
def get_products_with_group_supplier_and_total_sold():
    return (models.SaleItem.objects
            .values('product__name', 'product__product_group__name', 'product__supplier__name')
            .annotate(total_sold=Sum('quantity'))
            .order_by('-total_sold'))


# Q51 - Liste os estados com quantidade de clientes cadastrados, exibindo apenas os estados com mais de 10 clientes.
def get_states_with_more_than_10_customers():
    return list(models.Customer.objects
                .values('district__city__state__name')
                .annotate(total=Count('id'))
                .filter(total__gt=10)
                .order_by('-total'))


# Q52 - Mostre os clientes que possuem renda acima da média de renda do estado onde moram.
def get_customers_above_avg_income_by_state():
    avg_income_by_state = (models.Customer.objects
                           .filter(district__city__state=OuterRef('district__city__state'))
                           .values('district__city__state')
                           .annotate(avg=Avg('income'))
                           .values('avg'))

    return (models.Customer.objects
            .filter(income__gt=Subquery(avg_income_by_state))
            .values('name', 'income', 'district__city__state__name'))


# Q53 - Liste os departamentos cuja média salarial dos funcionários seja superior à média salarial geral da empresa.
def get_departments_above_avg_salary():
    avg_salary = models.Employee.objects.aggregate(Avg('salary'))['salary__avg']
    return list(models.Department.objects
                .annotate(avg_salary=Avg('employees__salary'))
                .filter(avg_salary__gt=avg_salary)
                .values('name', 'avg_salary'))


# Q54 - Mostre as vendas com: nome do cliente, nome do funcionário, filial e quantidade total de itens da venda.
def get_sales_with_details_and_item_count():
    return (models.Sale.objects
            .select_related('customer', 'employee', 'branch_office')
            .values('id', 'customer__name', 'employee__name', 'branch_office__name')
            .annotate(total_items=Count('sale_items')))


# Q55 - Liste os produtos que nunca foram vendidos.
def get_products_never_sold():
    sold_products = models.SaleItem.objects.filter(product=OuterRef('pk'))
    return list(models.Product.objects
                .filter(~Exists(sold_products))
                .values('name', 'sale_price'))


# Q56 - Mostre o faturamento total por grupo de produto.
def get_total_revenue_by_product_group():
    return (models.SaleItem.objects
            .values('product__product_group__name')
            .annotate(total_revenue=Sum(F('quantity') * F('product__sale_price')))
            .order_by('-total_revenue'))


# Q57 - Para cada funcionário, mostre: nome, salário, média salarial do departamento e diferença entre o salário dele e a média do departamento.
def get_employees_salary_vs_department_avg():
    avg_salary_by_dept = (models.Employee.objects
                          .filter(department=OuterRef('department'))
                          .values('department')
                          .annotate(avg=Avg('salary'))
                          .values('avg'))

    return (models.Employee.objects
            .annotate(
                dept_avg_salary=Subquery(avg_salary_by_dept),
                salary_diff=F('salary') - Subquery(avg_salary_by_dept)
            )
            .values('name', 'salary', 'dept_avg_salary', 'salary_diff'))


# Q58 - Liste os clientes que fizeram compras em mais de uma filial.
def get_customers_with_purchases_in_multiple_branches():
    return list(models.Customer.objects
                .annotate(total_branches=Count('sales__branch_office', distinct=True))
                .filter(total_branches__gt=1)
                .values('name', 'total_branches'))


# Q59 - Mostre o fornecedor que possui o maior número de produtos cadastrados.
def get_supplier_with_most_products():
    return (models.Supplier.objects
            .annotate(total_products=Count('products'))
            .order_by('-total_products')
            .values('name', 'total_products')[:1])


# Q60 - Liste o produto mais vendido em quantidade.
def get_most_sold_product():
    return list(models.SaleItem.objects
                .values('product__name')
                .annotate(total_quantity=Sum('quantity'))
                .order_by('-total_quantity')
                .values('product__name', 'total_quantity')[:1])


# Q61 - Mostre, para cada filial, o cliente que mais realizou compras nela.
def get_top_customer_by_branch():
    top_customer_sales = (models.Sale.objects
                          .filter(branch_office=OuterRef('pk'))
                          .values('customer__name')
                          .annotate(total=Count('id'))
                          .order_by('-total')
                          .values('customer__name')[:1])

    return (models.BranchOffice.objects
            .annotate(top_customer=Subquery(top_customer_sales))
            .values('name', 'top_customer'))


# Q62 - Liste os estados em que não há nenhum cliente cadastrado.
def get_states_without_customers():
    states_with_customers = (models.Customer.objects
                             .values('district__city__state'))

    return list(models.State.objects
                .exclude(id__in=states_with_customers.values('district__city__state_id'))
                .values('name'))


# Q63 - Mostre os departamentos que não possuem funcionários.
def get_departments_without_employees():
    employees = models.Employee.objects.filter(department=OuterRef('pk'))
    return (models.Department.objects
            .filter(~Exists(employees))
            .values('name'))


# Q64 - Liste os clientes que nunca realizaram compras, ordenados por renda decrescente.
def get_customers_without_purchases():
    sales = models.Sale.objects.filter(customer=OuterRef('pk'))
    return list(models.Customer.objects
                .filter(~Exists(sales))
                .values('name', 'income')
                .order_by('-income'))


# Q65 - Mostre os 3 produtos com maior faturamento total.
def get_top_3_products_by_revenue():
    return (models.SaleItem.objects
            .values('product__name')
            .annotate(total_revenue=Sum(F('quantity') * F('product__sale_price')))
            .order_by('-total_revenue')[:3])