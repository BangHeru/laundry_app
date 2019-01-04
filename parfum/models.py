from django.db import models


class Parfum(models.Model):
    """Model definition for Parfum."""
    
    STATUS = (
        ('A', 'Ada'), 
        ('K', 'Kosong')
        )

    nama = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=STATUS)

    