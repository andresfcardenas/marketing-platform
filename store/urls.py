#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    'store.views',

    # Create store
    url(
        r'^store_create/$',
        'store_create',
        name='store-create',
    ),

    # Store detail
    url(
        r'^(?P<slug>[-\w]+)/$',
        'store_detail',
        name='store-detail',
    ),

    # Update store
    url(
        r'^(?P<slug>[-\w]+)/edit/$',
        'store_update',
        name='store-update',
    ),

    # Update store image
    url(
        r'^image_store/(?P<slug>[-\w]+)/$',
        'upload_store_image',
        name='upload-store-image',
    ),

    # Create product
    url(
        r'^(?P<slug>[-\w]+)/product/create/$',
        'product_create',
        name='product-create',
    ),

    # Update product
    url(
        r'^(?P<slug>[-\w]+)/product/(?P<product_slug>[-\w]+)/edit/$',
        'product_update',
        name='product-update',
    ),

    # Update product image
    url(
        r'^image_product/(?P<slug>[-\w]+)/$',
        'upload_product_image',
        name='upload-product-image',
    ),

    # Product detail
    url(
        r'^(?P<slug>[-\w]+)/product/(?P<product_slug>[-\w]+)/$',
        'product_detail',
        name='product-detail',
    ),

    # Products by category
    url(
        r'^category/(?P<category>[-\w]+)/$',
        'products_by_category',
        name='products_by_category',
    ),

    # Delete a product
    url(
        r'^(?P<slug>[-\w]+)/product/(?P<product_slug>[-\w]+)/delete/$',
        'delete_product',
        name='delete_product',
    ),

    # Search tags
    url(
        r'^search/tags/$',
        'ajax_search_tags',
        name='ajax_search_tags',
    ),
)
