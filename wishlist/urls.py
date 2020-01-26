from django.urls import path
from wishlist import views

app_name = 'wishlist'
urlpatterns = [

    path(
        'add/(?P<product_id>\d+)/$',
        views.wishlist_add,
        name='wishlist_add'
    ),

    path(
        'remove/(?P<product_id>\d+)/',
        views.wishlist_remove,
        name='wishlist_remove'
    ),

    path('', views.wishlist_detail, name='wishlist_detail')
]
