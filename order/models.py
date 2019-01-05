from django.db import models
from django.core.validators import MinValueValidator
import datetime
from datetime import timedelta
from django.contrib.auth.models import User
from parfum.models import Parfum
from pelanggan.models import Pelanggan

class Order(models.Model):
    """Model definition for Order."""

    LAMA_PROSES = 3
    
    ORDER = (
        ('R', 'Reguler'),
        ('E', 'Express')
    )

    POSISI = (
        ('T', 'Tagging'),
        ('C', 'Cuci'),
        ('S', 'Setrika'),
        ('R', 'Rak'),
        ('A', 'Ambil')
    )

    # fungsi untuk memperoleh tanggal selesai order 
    def get_next_day(day):
        now = datetime.date.today()
        next = now + + timedelta(days=day)
        return next

    nomor = models.CharField(max_length=6, default='000001', unique=True)
    tanggalTerima = models.DateField(auto_now=True)
    tanggalSelesai = models.DateField(default=get_next_day(LAMA_PROSES))
    tanggalAmbil = models.DateField(null=True,default=get_next_day(LAMA_PROSES))
    jenis = models.CharField(max_length = 1, choices=ORDER, default='R')
    posisi = models.CharField(max_length = 1, choices=POSISI, default='T')
    totalBiaya = models.PositiveIntegerField(validators=[MinValueValidator(0)], default=0)
    catatan = models.TextField(null=True, blank=True)
    parfum = models.ForeignKey(Parfum, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)


    # class Meta:
    #     """Meta definition for Order."""

    #     verbose_name = 'Order'
    #     verbose_name_plural = 'Orders'

    def __str__(self):
        """Unicode representation of Order."""
        return self.nomor
