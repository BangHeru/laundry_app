from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='pelanggan_home'),
    path('cari/', views.cari_pelanggan, name='pelanggan_cari'),
    # path('secret2/', views.SecretPage.as_view(), name='secret2'),
    # path('accounts/', include('django.contrib.auth.urls')),

]
