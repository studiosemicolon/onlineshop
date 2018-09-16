# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.http import require_POST
from shop.models import Product
from .models import Cart, CartItem
# from .forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
# from .forms import CartAddProductForm


@login_required
def cart_add(request, product_id, product_qty=None):
    obj, created = Cart.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    item, itemCreated = CartItem.objects.update_or_create(
        cart=obj, product=product)
    item.price = product.price
    if(itemCreated == False):
        item.quantity = item.quantity+1
    # if item.quantity = request.GET['q']

    obj.items.add(item)
    item.save()
    obj.save()
    return redirect('cart:cart_detail')


@login_required
def cart_add_q(request, product_id, product_qty=None):
    obj, created = Cart.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    item, itemCreated = CartItem.objects.update_or_create(
        cart=obj, product=product)
    item.price = product.price

    # if item.quantity = request.GET['q']
    item.quantity = request.GET['q']
    if request.GET['q'] == "0":
        item.delete()
    else:
        obj.items.add(item)
        item.save()
        obj.save()
    return redirect('cart:cart_detail')

    # form = CartAddProductForm(request.POST)
    # if form.is_valid():
    #     cd = form.cleaned_data
    #     item.quantity=cd['quantity'],

def cart_remove(request, product_id):
    obj, created = Cart.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cartItems = CartItem.objects.filter(cart=obj, product=product)
    cartItems.delete()
    return redirect('cart:cart_detail')


@login_required
def cart_detail(request):

    cart = Cart.objects.get(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})
