from django.db import models
from django.core.validators import MinValueValidator

class Layanan(models.Model):
    """Model definition for Layanan."""

    STATUS = (
        ('A', 'Ada'),
        ('K', 'Kosong')
    )

    SATUAN = (
        ('Pcs', 'Potong'),
        ('Kg', 'Kilo')
    )

    nama = models.CharField(max_length=100)
    satuan = models.CharField(max_length=3, choices=SATUAN, default='Kg')
    biaya = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    status = models.CharField(max_length=1, choices=STATUS, default='A')



    # class Meta:
    #     """Meta definition for Layanan."""

    #     verbose_name = 'Layanan'
    #     verbose_name_plural = 'Layanans'

    def __str__(self):
        """Unicode representation of Layanan."""
        return self.nama
