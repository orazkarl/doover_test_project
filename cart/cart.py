from django.conf import settings
from django.shortcuts import render, redirect


class Cart(object):
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, product, quantity=1, action=None):
        id = product.id
        newItem = True
        if str(product.id) not in self.cart.keys():
            self.cart[product.id] = {
                'userid': self.request.user.id,
                'product_id': id,
                'name': product.name,
                'quantity': 1,
                'price': str(product.price),
                'image': product.image.url
            }
        else:
            newItem = True
            for key, value in self.cart.items():
                if key == str(product.id):
                    value['quantity'] = value['quantity'] + 1
                    newItem = False
                    self.save()
                    break
            if newItem == True:

                self.cart[product.id] = {
                    'userid': self.request,
                    'product_id': product.id,
                    'name': product.name,
                    'quantity': 1,
                    'price': str(product.price),
                    'image': product.image.url
                }

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def decrement(self, product):
        for key, value in self.cart.items():
            if key == str(product.id):
                if value['quantity'] == 1:
                    self.clear()
                    break
                value['quantity'] = value['quantity'] - 1
                if(value['quantity'] < 1):
                    return redirect('cart:cart_detail')
                self.save()
                break
            else:
                print("Something Wrong")

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True



