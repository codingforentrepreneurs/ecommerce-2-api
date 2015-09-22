# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0009_cart_tax_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.DecimalField(default=0.0, max_digits=50, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='cart',
            name='tax_total',
            field=models.DecimalField(default=0.0, max_digits=50, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.DecimalField(default=0.0, max_digits=50, decimal_places=2),
        ),
    ]
