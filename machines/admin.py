from django.contrib import admin

from machines.models import CoinsAvailable, Product, VendingMachine, VendingMachineManager

# Register your models here.
admin.site.register(VendingMachine)
admin.site.register(VendingMachineManager)
admin.site.register(Product)
admin.site.register(CoinsAvailable)
