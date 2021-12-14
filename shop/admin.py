from django.contrib import admin
from . models import Order, Product, Contact


admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)

# Register your models here.
