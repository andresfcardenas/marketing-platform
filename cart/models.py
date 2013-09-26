#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models


class Order(models.Model):
    """Represent a customer order.
    """
    STATUS = (
        (1, 'Solicitado'),
        (2, 'Cancelado'),
        (3, 'Entregado'),
    )

    customer_name = models.CharField(
        max_length=100,
        verbose_name=u'Nombre',
    )

    customer_email = models.EmailField(
        verbose_name=u'Correo electrónico',
    )

    customer_phone = models.CharField(
        max_length=10,
        verbose_name=u'Teléfono',
    )

    customer_address = models.CharField(
        max_length=50,
        verbose_name=u'Dirección',
    )

    status = models.SmallIntegerField(
        default=1,
        choices=STATUS,
        verbose_name=u'Estado del pedido',
    )

    total = models.CharField(
        max_length=12,
    )

    more_info = models.TextField(
        max_length=100,
        verbose_name=u'Información adicional'
    )

    def __unicode__(self):
        return u'{0}'.format(self.customer_name)


class CartProduct(models.Model):
    """Represent a product in order.
    """
    order = models.ForeignKey(
        'cart.Order',
        verbose_name=u'Pedido',
    )

    amount = models.SmallIntegerField(
        verbose_name=u'Cantidad',
    )

    product = models.ForeignKey(
        'store.Product',
        verbose_name=u'Producto',
    )

    def __unicode__(self):
        return u'{0}'.format(self.id)
