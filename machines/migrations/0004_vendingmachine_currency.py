# Generated by Django 3.2.15 on 2022-08-25 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0003_auto_20220825_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendingmachine',
            name='currency',
            field=models.CharField(default='KES', max_length=255),
            preserve_default=False,
        ),
    ]
