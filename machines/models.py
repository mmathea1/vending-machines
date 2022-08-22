from django.db import models

# Create your models here.
ORDER_STATUS = (
    ('INCOMPLETE', 'Incomplete'),
    ('COMPLETE', 'Complete'),
)


class VendingMachine(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    location = models.CharField(max_length=255, blank=False, null=False)
    coins_available = models.IntegerField(null=False, blank=False)
    date_installed = models.DateTimeField(null=True, blank=True, auto_now=True)


class VendingMachineManager(models.Model):
    vending_machine = models.ForeignKey(
        VendingMachine, related_name='vending_machine', on_delete=models.DO_NOTHING)
    manager = models.ForeignKey(
        'users.User', related_name='vending_machine_manager', null=False, on_delete=models.DO_NOTHING)


class CoinsAvailable(models.Model):
    coin = models.IntegerField(null=False, blank=False)
    total_available = models.IntegerField(null=False, blank=False)


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(
        max_digits=9, decimal_places=2, blank=False, null=False)
    stock = models.IntegerField(null=False, blank=False, default=0)
    code = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)


class Order(models.Model):
    product = models.ForeignKey(
        Product, related_name='product_purchased', on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(
        'users.User', on_delete=models.DO_NOTHING, null=False)
    amount_paid = models.DecimalField(
        null=False, blank=False, max_digits=9, decimal_places=2,)
    change_given = models.DecimalField(
        null=False, blank=False, max_digits=9, decimal_places=2,)
    order_status = models.CharField(
        max_length=255, blank=False, null=False, choices=ORDER_STATUS)
    date = models.DateTimeField(null=False, blank=False, auto_now=True)
