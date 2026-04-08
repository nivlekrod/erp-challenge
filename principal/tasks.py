from celery import shared_task


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