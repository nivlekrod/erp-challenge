from django.db import transaction
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from principal.models import SaleItem
from principal.actions import recalculate_sale_total

from principal.models import Sale
from principal.tasks import send_sale_email

@receiver(post_save, sender=SaleItem, dispatch_uid='sale_item_post_save_recalculate')
def on_sale_item_saved(sender, instance: SaleItem, **kwargs) -> None:
    recalculate_sale_total(instance.sale)


@receiver(post_delete, sender=SaleItem, dispatch_uid='sale_item_post_delete_recalculate')
def on_sale_item_deleted(sender, instance: SaleItem, **kwargs) -> None:
    recalculate_sale_total(instance.sale)


@receiver(post_save, sender=Sale, dispatch_uid='sale_post_save_send_email')
def on_sale_saved(sender, instance, created, **kwargs) -> None:
    if created:
        transaction.on_commit(lambda: send_sale_email.delay(instance.id))