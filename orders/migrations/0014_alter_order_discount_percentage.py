# Generated by Django 3.2.3 on 2021-05-29 22:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_alter_orderproducts_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='discount_percentage',
            field=models.FloatField(blank=True, default=0.0, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]