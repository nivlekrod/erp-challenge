from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from principal.models import SaleItem
from principal.actions import recalculate_sale_total


@receiver(post_save, sender=SaleItem)
def on_sale_item_saved(sender, instance: SaleItem, **kwargs) -> None:
    recalculate_sale_total(instance.sale)


@receiver(post_delete, sender=SaleItem)
def on_sale_item_deleted(sender, instance: SaleItem, **kwargs) -> None:
    recalculate_sale_total(instance.sale)