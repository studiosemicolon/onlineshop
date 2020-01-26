# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from shop.models import Product
from accounts.models import User


class Cart(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    is_in_order = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'cart {}'.format(self.user.email)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items',
    null=True,
    on_delete=models.CASCADE,
    )
    product = models.ForeignKey(Product,
    related_name='cart_items',
    on_delete=models.CASCADE,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.product.name)

    def get_cost(self):
        return self.price * self.quantity
