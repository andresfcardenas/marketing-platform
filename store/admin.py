#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from store.models import Store
from store.models import Product
from store.models import Category
from store.models import ProductTag


class StoreAdmin(admin.ModelAdmin):
    """Admin for UserProfile model.
    """

    list_display = [
        'name',
    ]

admin.site.register(Store, StoreAdmin)


class ProductAdmin(admin.ModelAdmin):
    """Admin for UserProfile model.
    """

    list_display = [
        'name',
    ]

admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    """Admin for UserProfile model.
    """

    list_display = [
        'name',
    ]

admin.site.register(Category, CategoryAdmin)

class ProductTagAdmin(admin.ModelAdmin):
    """Admin for UserProfile model.
    """

    list_display = [
        'name',
    ]

admin.site.register(ProductTag, ProductTagAdmin)
