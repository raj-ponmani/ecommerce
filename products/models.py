from django.db import models
from djmoney.models.fields import MoneyField


# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='INR',
        max_digits=10,
    )
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)
