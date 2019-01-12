from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from layanan.models import Layanan



# def home(request):
#     layanan = Layanan.objects.all()
    
#     return render(request, 'pelanggan/index.html', {'layanan': layanan })



def cari_layanan(request):
    if request.POST and request.is_ajax:
        kata_kunci = request.POST['pk']
        # print(request.POST['pesan'])
    else:
        kata_kunci = ''
 

    data = Layanan.objects.filter(pk=kata_kunci)

    # data = Pelanggan.objects.filter(nama__contains=kata_kunci)
   
    data = serializers.serialize('json', list(data))
    
    return HttpResponse(data, content_type="application/json")
  