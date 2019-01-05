from django.db import models
from order.models import Order
# from layanan.models import Layanan


class DetailOrder(models.Model):
    """Model definition for DetailOrder."""

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # layanan = models.ForeignKey(Layanan, on_delete=models.CASCADE)
    layanan = models.CharField(max_length=30, default='Cuci dan Setrika')
    jumlah = models.FloatField(default=0)
    hrg_satuan = models.FloatField(default=0)
    total = models.FloatField(default=0)
    keterangan = models.TextField(max_length=240, blank=True)

    
    def __str__(self):
        """Unicode representation of DetailOrder."""
        # return str(self.total)
        return str(self.id)
                # pass
