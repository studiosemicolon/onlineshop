# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from cart.models import Cart
# Create your views here.


def order_create(request):

    # return redirect(reverse('payment:process'))
    cart = Cart.objects.get(user=request.user)
    return render(request, 'orders/order_list.html', {'cart': cart})
