# Generated by Django 3.2.15 on 2022-08-24 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MachineUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='vending machine user email address')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('code', models.CharField(max_length=5, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VendingMachine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('location', models.CharField(max_length=255)),
                ('date_installed', models.DateTimeField(auto_now=True, null=True)),
                ('manager', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='vending_machine_manager', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('stock', models.IntegerField(default=0)),
                ('code', models.CharField(max_length=255, unique=True)),
                ('vending_machine', models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='machines.vendingmachine')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=9)),
                ('change_given', models.DecimalField(decimal_places=2, max_digits=9)),
                ('order_status', models.CharField(choices=[('INCOMPLETE', 'Incomplete'), ('COMPLETE', 'Complete')], max_length=255)),
                ('order_date', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_purchased', to='machines.product')),
            ],
        ),
        migrations.CreateModel(
            name='CoinsAvailable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.IntegerField()),
                ('total_available', models.IntegerField()),
                ('vending_machine', models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='machines.vendingmachine')),
            ],
        ),
    ]
