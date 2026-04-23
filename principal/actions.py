from principal.models import Sale


def recalculate_sale_total(sale: Sale) -> None:
    from principal.models import SaleItem

    total = SaleItem.objects.total_by_sale(sale_id=sale.pk)
    Sale.objects.filter(pk=sale.pk).update(total=total)