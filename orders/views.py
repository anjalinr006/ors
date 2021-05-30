from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from orders.models import *
from orders.forms import *
from django.urls import reverse
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core import serializers
import json
import itertools
import decimal

# import openpyxl
# wb = openpyxl.load_workbook('products.xlsx')
# worksheet = wb["Sheet1"]
# excel_data = list()
# worksheet_iter = worksheet.iter_rows()
# next(worksheet_iter)
# for row in worksheet_iter:
#     row_data = list()
#     for cell in row:
#         if cell.value == None:
#             cell.value = 0.0
#         row_data.append(str(cell.value))
    # Product.objects.create(
    #     name=row_data[0],
    #     code=row_data[1],
    #     price=row_data[2],
    #     features=row_data[3],
    #     inventory=row_data[4]
    # )


def order_list(request):
    object_list = Order.objects.all()
    context = {'object_list': object_list}
    if request.is_ajax and request.GET:
        ajax_type = request.GET.get('ajax_type', None)
        if ajax_type == 'order_summery':
            id = request.GET.get('order_id', None)
            object = object_list.get(id=int(id))
            context = {'object': object}
            html = render_to_string('orders/order_summery.html', context)
        return HttpResponse(html, content_type="application/html")

    return render(request, 'orders/order_list.html', context)


def order_create(request):
    customer_obj = Customer.objects.all()
    product_objs = Product.objects.all()
    html = ''
    if request.is_ajax and request.GET:
        ajax_type = request.GET.get('ajax_type', None)
        if ajax_type == 'choose_price':
            product_id = request.GET.get('product_id', 'None')
            product_obj = product_objs.get(id=int(product_id))
            html = product_obj.price

        if ajax_type == 'get_user_data':
            customer_id = request.GET.get('customer_id', None)
            customer = customer_obj.get(id=int(customer_id))
            context = {'phone_number': customer.phone_number, 'address': customer.address}
            html = render_to_string('orders/edit_user_details.html', context)

        if ajax_type == 'save_user_data':
            customer_id = request.GET.get('customer_id', None)
            customer = customer_obj.get(id=int(customer_id))
            customer.phone_number = request.GET.get('phone_number', None)
            customer.address = request.GET.get('address', None)
            customer.save()
            context = {'phone_number': customer.phone_number, 'address': customer.address}
            html = render_to_string('orders/edit_user_details.html', context)

        if ajax_type == 'customer':
            search_text = request.GET.get('search_text', None)
            objects = customer_obj.filter(Q(name__contains=search_text) | Q(phone_number__contains=search_text))
            context = {'objects': objects}
            html = render_to_string('orders/option_list.html', context)

        if ajax_type == 'product':
            search_text = request.GET.get('search_text', None)
            objects = product_objs.filter(Q(name__contains=search_text) | Q(features__contains=search_text)| Q(code__contains=search_text))
            context = {'objects': objects}
            html = render_to_string('orders/option_list.html', context)

        return HttpResponse(html, content_type="application/html")

    if request.POST:
        form = OrderForm(request.POST)
        order_products = OrderProductsFormset(request.POST)
        if form.is_valid() and order_products.is_valid():
            order_instance = form.save()
            order_products.instance = order_instance
            order_obj = order_products.save()
            amount = 0
            for obj in order_obj:
                product = obj.product
                product_amount = obj.quantity * obj.product.price
                amount = amount + product_amount
                product.inventory = product.inventory - obj.quantity
                product.save()
                obj.amount = product_amount
                obj.save()
            order_instance.amount = amount
            discount_amount = amount*decimal.Decimal(order_instance.discount_percentage/100)
            order_instance.discount_amount = discount_amount
            order_instance.total = round(amount-discount_amount, 2)
            order_instance.save()
            return redirect('create_order')
        else:
            print(form.errors)
            print(order_products.errors)
    else:
        form = OrderForm()
        order_products = OrderProductsFormset()
    return render(request, 'orders/create_order.html', {'form': form, 'order_products': order_products})
