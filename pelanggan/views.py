from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.db.models import Q

from .models import Pelanggan



def home(request):
    return render(request, 'pelanggan/index.html', { })



def cari_pelanggan(request):
    if request.POST and request.is_ajax:
        kata_kunci = request.POST['search']
    else:
        kata_kunci = ''
 
    lookups = Q(nama__startswith=kata_kunci) | Q(alamat__startswith=kata_kunci) | Q(telepon__startswith=kata_kunci)

    data = Pelanggan.objects.filter(lookups)

    # data = Pelanggan.objects.filter(nama__contains=kata_kunci)
   
    data = serializers.serialize('json', list(data))
    
    return HttpResponse(data, content_type="application/json")
  