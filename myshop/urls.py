from django.urls import path, include

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('orders/', include('orders.urls', )),
    
    path('admin/', admin.site.urls),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/', include('payment.urls', )),
    
    path('accounts/', include('accounts.urls', )),
    path('wishlist/', include('wishlist.urls', )),
    path('cart/', include('cart.urls', )),
    path('', include('shop.urls')),
    
    

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
