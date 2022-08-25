from django.contrib import admin

from machines.models import CoinsAvailable, MachineUser, Product, VendingMachine

# Register your models here.
admin.site.register(VendingMachine)
admin.site.register(Product)
admin.site.register(CoinsAvailable)
admin.site.register(MachineUser)
