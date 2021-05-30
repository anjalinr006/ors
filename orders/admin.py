from django.contrib import admin
from orders.models import *


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'phone_number']


class OrderProductsAdmin(admin.TabularInline):
    model = OrderProducts
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_per_page = 100
    list_display = ('customer',)
    inlines = [OrderProductsAdmin, ]


admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product)
