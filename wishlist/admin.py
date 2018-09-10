# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import WishlistItem, Wishlist

# Register your models here.
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
