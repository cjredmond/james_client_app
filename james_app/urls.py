from django.conf.urls import url, include
from django.contrib import admin
from user_auth.views import UserCreateView, AccountDetailView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^account/(?P<pk>\d+)/$', AccountDetailView.as_view(), name='account_detail_view'),

]
