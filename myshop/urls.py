from django.urls import path, include

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('orders/', include('orders.urls', namespace='orders')),

    path('admin/', admin.site.urls),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/', include('payment.urls',namespace='payment' )),

    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('', include('shop.urls', namespace='shop')),



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
