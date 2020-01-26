from django.conf.urls import url
from . import views

app_name='cart'
urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^add_q/(?P<product_id>\d+)/$', views.cart_add_q, name='cart_add_q'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),

]
