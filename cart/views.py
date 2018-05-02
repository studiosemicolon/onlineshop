# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .models import Cart

# from .forms import CartAddProductForm



@require_POST
def cart_add(request, product_id):

	pass 


def cart_remove(request, product_id):
    pass
    # cart = Cart(request)
    # product = get_object_or_404(Product, id=product_id)
    # cart.remove(product)
    # return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart.objects.get(id=3)
    import pdb; pdb.set_trace()

    return render(request, 'cart/cart_detail.html', {'cart': cart})
