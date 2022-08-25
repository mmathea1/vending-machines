
import random
import string
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin
# Create your models here.
ORDER_STATUS = (
    ('INCOMPLETE', 'Incomplete'),
    ('COMPLETE', 'Complete'),
)


def generate_random_code():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))


class UserManager(BaseUserManager):
    def create_user(self, username, password, email=None):
        if email is None:
            raise ValueError('Email is required.')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            code=generate_random_code()
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, username, password, email=None):
        if not username:
            raise ValueError('The given username must be set')
        user = self.model(username=username, code=generate_random_code())
        user.is_staff = True
        user.set_password(password)
        # user.
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, email=None):
        user = self.create_user(
            username=username,
            password=password,
            code=generate_random_code(),
            is_superuser=True
        )
        user.is_staff = True
        user.is_admin = True
        user.set_password(password)
        # user.
        user.save(using=self._db)
        return user

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_staff

    @property
    def is_superuser(self):
        return self.is_superuser


class MachineUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='vending machine user email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        max_length=255, blank=False, null=False, unique=True)
    code = models.CharField(max_length=5, blank=False, null=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['code']
    objects = UserManager()

    def __str__(self):
        return self.username


class VendingMachine(models.Model):
    name = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    location = models.CharField(max_length=255, blank=False, null=False)
    currency = models.CharField(max_length=255, blank=False, null=False)
    date_installed = models.DateTimeField(null=True, blank=True, auto_now=True)
    manager = models.ForeignKey(
        MachineUser, related_name='vending_machine_manager', null=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        return '{} - {}'.format(self.name, self.location)


class CoinsAvailable(models.Model):
    coin = models.IntegerField(null=False, blank=False)
    total_available = models.IntegerField(null=False, blank=False, default=1)
    vending_machine = models.ForeignKey(
        to=VendingMachine, blank=False, null=False, on_delete=models.DO_NOTHING, default=1)

    class Meta:
        unique_together = (('coin', 'vending_machine'))
        ordering = ('coin', 'vending_machine')

    def __str__(self):
        return '{} - {}'.format(self.coin, self.vending_machine)


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(
        max_digits=9, decimal_places=2, blank=False, null=False)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    code = models.CharField(max_length=255, blank=False,
                            null=False, unique=True)
    vending_machine = models.ForeignKey(
        to=VendingMachine, blank=False, null=False, on_delete=models.DO_NOTHING, default=1)

    class Meta:
        unique_together = (('name', 'price', 'vending_machine'))
        ordering = ('name', 'quantity')


class Order(models.Model):
    product = models.ForeignKey(
        Product, related_name='product_purchased', on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(
        MachineUser, on_delete=models.DO_NOTHING, null=False)
    amount_paid = models.DecimalField(
        null=False, blank=False, max_digits=9, decimal_places=2,)
    change_given = models.DecimalField(
        null=False, blank=False, max_digits=9, decimal_places=2,)
    order_status = models.CharField(
        max_length=255, blank=False, null=False, choices=ORDER_STATUS)
    order_date = models.DateTimeField(null=False, blank=False, auto_now=True)
