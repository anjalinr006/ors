# Generated by Django 3.2.3 on 2021-05-29 21:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_order_discount_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount_amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='discount_percentage',
            field=models.FloatField(blank=True, default=0.0, validators=[django.core.validators.MinValueValidator(0.9)]),
        ),
    ]
