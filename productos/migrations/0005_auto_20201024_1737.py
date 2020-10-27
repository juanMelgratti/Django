# Generated by Django 3.1.2 on 2020-10-24 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_producto_descuento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descuento',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]