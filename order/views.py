from django.shortcuts import render, HttpResponse
from cart.cart import Cart
from .models import Order, OrderItem
from shop.models import Product
from django.views import generic


def order_checkout(request):
    cart = Cart(request)
    user = request.user

    order = Order.objects.create(user=user, status='not paid')
    for item in cart.cart.values():
        product = Product.objects.get(id=int(item['product_id']))
        OrderItem.objects.create(order=order, product=product, price=item['price'], quantity=item['quantity'])
    cart.clear()
    return HttpResponse('Заказ принят')


class OrderListView(generic.ListView):
   model = Order

   def get(self, request, *args, **kwargs):
       self.queryset = Order.objects.filter(user=request.user)
       return super().get(request, *args, **kwargs)