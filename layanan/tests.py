from django.test import TestCase

from .models import Layanan


class TestLayanan(TestCase):
    def setUp(self):
        Layanan.objects.create(
            nama = 'Cuci dan Setrika',
            satuan = 'Kg',
            biaya = 7000
            )

        Layanan.objects.create(
            nama = 'Kebaya',
            satuan = 'Pcs',
            biaya = 15000
            )


    def test_get_layanan(self):
        layanan = Layanan.objects.get(satuan='Kg')