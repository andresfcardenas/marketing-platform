#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin
from cart.models import Order
from cart.models import CartProduct


class ProductsInline(admin.TabularInline):
    model = CartProduct


class ProductAdmin(admin.ModelAdmin):
    model = Order
    inlines = [ProductsInline]
    list_display = (
        'id',
        'get_status_display',
        'customer_name',
        'customer_email',
        'customer_phone',
        'total',
    )
    list_filter = [
        'status',
    ]


admin.site.register(Order, ProductAdmin)
