from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name='pelanggan_home'),
    path('cari/', views.cari_layanan, name='pelanggan_layanan'),
 

]
