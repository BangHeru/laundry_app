# Generated by Django 2.1.4 on 2019-01-04 05:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layanan', '0004_auto_20190104_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layanan',
            name='biaya',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
