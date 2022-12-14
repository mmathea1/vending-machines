# Generated by Django 3.2.15 on 2022-08-25 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0002_auto_20220825_0833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coinsavailable',
            options={'ordering': ('coin', 'vending_machine')},
        ),
        migrations.AlterField(
            model_name='coinsavailable',
            name='total_available',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='coinsavailable',
            name='vending_machine',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='machines.vendingmachine'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vending_machine',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='machines.vendingmachine'),
        ),
        migrations.AlterUniqueTogether(
            name='coinsavailable',
            unique_together={('coin', 'vending_machine')},
        ),
    ]
