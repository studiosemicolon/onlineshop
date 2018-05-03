# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required
# from .forms import CartAddProductForm
from shop.models import Product

@login_required
def cart_add(request, product_id):
    cart = Cart.objects.get(user=request.user)
    cartItem = CartItem.objects.get(pk=cart.pk)
    


    
    product = get_object_or_404(Product, id=product_id, available=True)
    print product
    print cartItem
    cartItem.product=product
    cartItem.save()
    cart.save()

    
    
    
    
    return redirect('cart:cart_detail')


@login_required
def cart_remove(request, product_id):
    pass
    # cart = Cart(request)
    # product = get_object_or_404(Product, id=product_id)
    # cart.remove(product)
    # return redirect('cart:cart_detail')


@login_required
def cart_detail(request):

    cart = Cart.objects.get(user=request.user)

    # import pdb; pdb.set_trace()

    return render(request, 'cart/cart_detail.html', {'cart': cart})
