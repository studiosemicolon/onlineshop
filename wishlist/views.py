# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, 	get_object_or_404
from shop.models import Product
from django.contrib.auth.decorators import login_required
from .models import Wishlist, WishlistItem


@login_required
def wishlist_add(request, product_id,):

    obj, created = Wishlist.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    item, itemCreated = WishlistItem.objects.update_or_create(wishlist=obj, product=product)
    obj.wishlist_items.add(item)
    item.save()
    obj.save()
    return redirect('wishlist:wishlist_detail')

    # form = CartAddProductForm(request.POST)
    # if form.is_valid():
    #     cd = form.cleaned_data
    #     item.quantity=cd['quantity'],


def wishlist_remove(request, product_id):
    obj, created = Wishlist.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    wishlistItems = WishlistItem.objects.filter(wishlist=obj, product=product)
    wishlistItems.delete()
    return redirect('wishlist:wishlist_detail')


@login_required
def wishlist_detail(request):
    wishlist = Wishlist.objects.get(user=request.user)
    return render(request, 'wishlist/wishlist_detail.html', {'wishlist': wishlist})
