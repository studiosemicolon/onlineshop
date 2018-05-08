# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import *
from cart.models import Cart

from django.contrib.auth.models import User
from accounts.models import Profile
# Create your views here.


def order_create(request):

    # return redirect(reverse('payment:process'))

    profile = get_object_or_404(Profile, user=request.user)
    cart = Cart.objects.get(user=request.user)
    # import pdb; pdb.set_trace()
    return render(request, 'orders/order_list.html', {'cart': cart,'profile': profile})
