from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum, F
from decimal import Decimal
from principal import models

@receiver([post_save, post_delete], sender=models.SaleItem, dispatch_uid='update_total_amount')
def update_total_amount(instance, **kwargs):
	sale = instance.sale

	aggregate = sale.sale_items.filter(is_active=True).aggregate(
		total=Sum(F('quantity') * F('product__sale_price'))
	)

	new_total = aggregate['total'] or Decimal(0)

	models.Sale.objects.filter(id=sale.id).update(total_amount=new_total)