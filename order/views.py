from django.shortcuts import render
from layanan.models import Layanan

# Create your views here.
def home(request):
    layanan = Layanan.objects.all()
    
    return render(request, 'order/order.html', {'layanan': layanan })