from django.db import models
from django.core.validators import MinValueValidator
import decimal

class Customer(models.Model):
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=12, blank=True, default="")
    address = models.TextField(blank=True, default="")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    features = models.TextField()
    inventory = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    discount_percentage = models.FloatField(blank=True, validators=[MinValueValidator(0.0)], default=0.0)


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)


