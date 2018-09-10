# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from shop.models import Product


# Create your models here.
class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'wishlist of {}'.format(self.user.username)


class WishlistItem(models.Model):

    wishlist = models.ForeignKey(
        Wishlist, related_name='wishlist_items', null=True)
    product = models.ForeignKey(Product, related_name='wishlist_item')

    def __str__(self):
        return '{}'.format(self.product.name)
