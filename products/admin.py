from django.contrib import admin
from products.models import Products


# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    pass
