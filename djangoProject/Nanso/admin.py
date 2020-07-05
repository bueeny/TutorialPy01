from django.contrib import admin
from .models import ProductClassification, Product, CurrencyList

# Register your models here.
admin.site.register(ProductClassification)
admin.site.register(CurrencyList)
admin.site.register(Product)
