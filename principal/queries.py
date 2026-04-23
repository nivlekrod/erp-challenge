from principal import models
from django.db.models import Subquery, Avg, F, Value, ExpressionWrapper, FloatField, Sum, Case, When
from datetime import date


def list_states():
	return models.State.objects.all()


def get_funcionario_by_name(name: str):
	return models.Employee.objects.filter(name__icontains=name)


def get_salary_by_gender():
	return models.Employee.objects.values("gender").annotate(gender_description=Case(
		When(gender="M", then=Value("Male")), When(gender="F", then=Value("Female")),
	)).annotate(
		total_salaries=Sum(
			"salary"))


def q1():
	return models.Employee.objects.values("gender", "salary").filter(salary__gte=5000)


def q2():
	return models.Employee.objects.all().filter(salary__gte=3000, salary__lte=5000,
	                                            admission__gte=date(2020, 1, 1))


def q3():
	return models.Product.objects.all().filter(sale_price__gte=100, cost_price__gte=80)


def q4():
	return models.Supplier.objects.all().filter(legal_document__istartswith=92)


def q5():
	return models.Customer.objects.all().filter(district__id=3)


def q6():
	return models.SaleItem.objects.all().filter(quantity__gte=10)


def q7():
	return models.Customer.objects.all().order_by("salary")


def q8():
	return models.Employee.objects.all().order_by("-salary", "name")


def q9():
	return models.Product.objects.all().order_by("sale_price")


def q12():
	return models.Customer.objects.select_related("district").values("name", "district__name")


def q20():
	subquery = models.Product.objects.all().values(avg=Avg("sale_price"))[:1]
	query = models.Product.objects.filter(sale_price__gte=Subquery(subquery))

	return query
