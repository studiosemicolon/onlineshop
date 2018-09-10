from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name='signup'),
    # url(r'^login/$', LoginView.as_view(redirect_authenticated_user=True)),
    url(r'^detail_profile/$', views.detail_profile, name='detail_profile'),


]
