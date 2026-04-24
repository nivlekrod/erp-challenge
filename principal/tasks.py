from celery import shared_task


from django.core.mail import send_mail

from principal.models import Sale, SaleItem


@shared_task(queue='default')
def send_sale_email(sale_id):
    try:
        sale = Sale.objects.get(pk=sale_id)
        items = SaleItem.objects.filter(sale_id=sale_id, is_active=True)

        print(f"[DEBUG] sale_id: {sale_id}")
        print(f"[DEBUG] total: {sale.total}")
        print(f"[DEBUG] qtd itens: {items.count()}")
        for i in items:
            print(f"[DEBUG] item: {i.product.name} | qty: {i.quantity}")

        item_list = "\n".join([
            f"- {item.product.name}: {item.quantity} un. x R$ {item.product.sale_price} = R$ {item.quantity * item.product.sale_price}"
            for item in items
        ])
        subject = f"Resumo da Venda #{sale.id}"
        message = (
            f"Olá {sale.customer.name},\n\n"
            f"Sua compra na filial {sale.branch_office.name} foi registrada com sucesso!\n"
            f"Data: {sale.sold_at}\n\n"
            f"Itens:\n{item_list}\n\n"
            f"Total: R$ {sale.total}\n\n"
            "Obrigado por comprar conosco!"
        )

        send_mail(
            subject,
            message,
            '@gmail.com',
            [sale.customer.email if hasattr(sale.customer, 'email') else '@gmail.com'],
            fail_silently=False,
        )
    except Sale.DoesNotExist:
        pass

# @shared_task(queue='default')
# def create_file(state_id: int):
#     with open('c:\\tmp\\states.txt', 'w+') as file:
#         for n in range(1, 10001):
#             print(n)
#             file.write(f'{state_id} - {n}')
#
# @shared_task(queue='default')
# def create_customer_file():
#     customers = models.Customer.objects.all()
#     _now = now()
#
#     with open(f'{_now.year}-{_now.month}-{_now.day}-customers.txt', 'w+') as file:
#         for c in customers:
#             file.write(f'{c.name}\n')