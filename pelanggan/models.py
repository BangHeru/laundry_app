from django.db import models

class Pelanggan(models.Model):
    """Model definition for Pelanggan."""

    nama = models.CharField(max_length=50)
    telepon = models.CharField(max_length=15, null=True)
    alamat = models.TextField(max_length=200)

    class Meta:
        """Meta definition for Pelanggan."""

        verbose_name = 'Pelanggan'
        verbose_name_plural = 'Pelanggans'

    def __str__(self):
        """Unicode representation of Pelanggan."""
        return self.nama
