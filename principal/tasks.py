from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from principal import models
from django.utils.timezone import now


@shared_task(queue='default')
def create_file(state_id: int):
	with open('c:\\tmp\\states.txt', 'w+') as file:
		for n in range(1, 10001):
			print(n)
			file.write(f'{state_id} - {n}')


@shared_task(queue='default')
def create_customer_file():
	customers = models.Customer.objects.all()
	_now = now()

	with open(f'{_now.year}-{_now.month}-{_now.day}-customers.txt', 'w+') as file:
		for c in customers:
			file.write(f'{c.name}\n')


@shared_task(queue='default')
def send_sales_email(sale_id):
	try:
		sale = models.Sale.objects.select_related('customer', 'employee').get(id=sale_id)
		items = sale.sale_items.all()

		subject = f"Confirmação de Venda #{sale.id} - ERP Challenge"

		item_list = "\n".join([
			f"- {item.product.name}: {item.quantity} x R$ {item.product.sale_price}"
			for item in items
		])

		message = (
			f"Olá, {sale.customer.name}!\n\n"
			f"Sua venda foi processada com sucesso.\n"
			f"Vendedor: {sale.employee.name}\n"
			f"Total: R$ {sale.total_amount}\n\n"
			f"Itens:\n{item_list}\n\n"
			f"Obrigado por comprar conosco!"
		)

		# Envio real
		# send_mail(
		# 	subject=subject,
		# 	message=message,
		# 	from_email=settings.DEFAULT_FROM_EMAIL,
		# 	recipient_list=[sale.customer.email],
		# 	fail_silently=False,
		# )
		# Envio fake
		print(message)

		return f"E-mail da venda {sale_id} enviado com sucesso!"

	except models.Sale.DoesNotExist:
		return f"Erro: Venda {sale_id} não encontrada."
