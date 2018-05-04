# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.http import require_POST
from shop.models import Product
from .models import Cart, CartItem
from .forms import CartAddProductForm
from django.contrib.auth.decorators import login_required
# from .forms import CartAddProductForm


@login_required
def cart_add(request, product_id, product_qty = None):

    obj, created = Cart.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    item, itemCreated = CartItem.objects.update_or_create(cart=obj, product=product)
    item.price = product.price
    import pdb; pdb.set_trace()
    if product_qty:
        item.quantity = product_qty
    obj.items.add(item)
    obj.save()




    # form = CartAddProductForm(request.POST)
    # if form.is_valid():
    #     cd = form.cleaned_data
    #     item.quantity=cd['quantity'],
        
def cart_remove(request, product_id):
    obj, created = Cart.objects.update_or_create(user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cartItems = CartItem.objects.filter(cart=obj, product= product)
    cartItems.delete()

    import pdb; pdb.set_trace()

    return redirect('cart:cart_detail')













    # cart = Cart.objects.get_object_or_404(user=request.user)
    # # cartItem = CartItem.objects.get(id=cart.pk)
    # # cart = Cart.objects.get_or_create(id=1)
    
    # 

    # import pdb; pdb.set_trace()
    
    # # cartItem.product = product
    # # cartItem.save()
    

    return redirect('cart:cart_detail')




@login_required
def cart_detail(request):

    cart = Cart.objects.get(user=request.user)

    # import pdb; pdb.set_trace()

    return render(request, 'cart/cart_detail.html', {'cart': cart})
