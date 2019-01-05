from django.contrib import admin

from .models import DetailOrder

class DetailOrderAdmin(admin.ModelAdmin):
    list_display = ('id','order', 'layanan', 'jumlah', 'hrg_satuan','total')
    # fields  = ['order', 'layanan', 'jumlah', 'hrg_satuan','total']

admin.site.register(DetailOrder, DetailOrderAdmin)