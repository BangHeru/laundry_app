from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.core import serializers

from .models import Pelanggan
# Create your views here.


def home(request):
    return render(request, 'pelanggan/index.html', { })



def cari_pelanggan(request):
    # if request.method == 'POST':
    if request.POST and request.is_ajax:
        kata_kunci = request.POST['search']
    else:
        kata_kunci = ''
 

    # hasil_cari = Pelanggan.objects.filter(nama__contains=kata_kunci, 
    #             alamat__contains=kata_kunci, telepon__contain=kata_kunci)

    data = Pelanggan.objects.filter(nama__contains=kata_kunci)
    
    # return HttpResponse(kata_kunci)
    data = serializers.serialize('json', list(data))
    # print(data)
    return HttpResponse(data, content_type="application/json")
    
    # print(hasil_cari)
    # return JsonResponse({'data':data})