from django.db import models


class SaleItemQuerySet(models.QuerySet):
    
    def total_by_sale(self, sale_id: int):
        return (
                self.filter(sale_id=sale_id, is_active=True)
                .aggregate(
                    total=models.Sum(
                        models.F('quantity') * models.F('product__sale_price'),
                        output_field=models.DecimalField()
                    )
                )
                .get('total') or 0
        )


class SaleItemManager(models.Manager):

    def get_queryset(self) -> SaleItemQuerySet:
        return SaleItemQuerySet(self.model, using=self._db)

    def total_by_sale(self, sale_id: int):
        return self.get_queryset().total_by_sale(sale_id)