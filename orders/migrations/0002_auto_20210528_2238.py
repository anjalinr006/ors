# Generated by Django 3.2.3 on 2021-05-28 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='discount_percentage',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]