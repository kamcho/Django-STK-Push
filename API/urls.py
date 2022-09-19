from django.urls import path

from . import views

urlpatterns = [
    path('access/token', views.getAccessToken, name='get_mpesa_access_token'),
    path('', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),
    path('success/',views.Success,name='success')
]