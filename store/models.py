#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

from autoslug import AutoSlugField


class Store(models.Model):
    """This model represent a store in platform
    """
    name = models.CharField(
        max_length=50,
    )

    description = models.TextField(
        max_length=250,
    )

    logo = models.ImageField(
        upload_to='uploads/logos',
        default='img/logo_default.png',
        blank=True,
    )

    phone = models.CharField(
        max_length=10,
    )

    address = models.CharField(
        max_length=50,
    )

    slug = AutoSlugField(
        unique=True,
        always_update=True,
        populate_from=lambda instance: instance.name,
    )

    created_by = models.ForeignKey(
        'auth.User',
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('store:store-detail', [self.slug])

    def __unicode__(self):
        return u'{0}'.format(self.name)


class Product(models.Model):
    """This model represent a product in a store.
    """
    name = models.CharField(
        max_length=50,
    )

    category = models.ForeignKey(
        'store.Category',
        null=True,
    )

    quantity = models.PositiveIntegerField(
        default=1,
    )

    description = models.TextField(
        max_length=250,
    )

    image = models.ImageField(
        upload_to='uploads/product_images',
        default='img/logo_default.png',
        blank=True,
    )

    store = models.ForeignKey(
        'store.Store',
        blank=True,
        null=True,
    )

    price = models.PositiveIntegerField(
        verbose_name=u'Price',
    )

    tags = models.ManyToManyField(
        'store.ProductTag',
        blank=True,
        null=True,
    )

    slug = AutoSlugField(
        unique=True,
        always_update=True,
        populate_from=lambda instance: instance.name,
    )

    created_by = models.ForeignKey(
        'auth.User',
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    @models.permalink
    def get_absolute_url(self):
        return ('store:product-detail', [self.store.slug, self.slug])

    def __unicode__(self):
        return u'{0}'.format(self.name)


class Category(models.Model):
    """This model represent a category for product.
    """
    name = models.CharField(
        max_length=50,
    )

    image = models.ImageField(
        upload_to='uploads/category_images',
        default='img/logo_default.png',
        blank=True,
    )

    slug = AutoSlugField(
        unique=True,
        always_update=True,
        populate_from=lambda instance: instance.name,
    )

    def __unicode__(self):
        return u'{0}'.format(self.name)


class ProductTag(models.Model):
    """This model represent a product tag.
    Only the administrator can manage tags.
    """
    name = models.CharField(
        max_length=20,
    )

    parent = models.ForeignKey(
        'store.ProductTag',
        null=True,
        blank=True,
    )

    slug = AutoSlugField(
        unique=True,
        always_update=True,
        populate_from='name',
    )

    def __unicode__(self):
        return u'{0}'.format(self.name)
