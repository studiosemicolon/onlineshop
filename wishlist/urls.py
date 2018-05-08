from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^/$', views.wishlist_detail, name='wishlist_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.wishlist_add, name='wishlist_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.wishlist_remove, name='wishlist_remove'),
]
