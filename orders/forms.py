from django.forms.models import inlineformset_factory
from orders.models import Order, OrderProducts
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('amount', 'discount_amount', 'total',)


class OrderProductsForm(forms.ModelForm):
    class Meta:
        model = OrderProducts
        exclude = ('amount',)


OrderProductsFormset = inlineformset_factory(
    Order, OrderProducts, form=OrderProductsForm, extra=0,  can_delete=True)

