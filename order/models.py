from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


class Order(models.Model):
    STATUS_CHOICES = [
        ['not paid', 'not paid'],
        ['paid', 'paid'],
        ['delivered', 'delivered'],
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)

    def __str__(self):
        return "Order {}".format(self.id)

    def get_total_cost(self):
        cost = sum(item.get_cost() for item in self.items.all())
        return cost


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def get_cost(self):
        return self.price * self.quantity
