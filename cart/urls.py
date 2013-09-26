#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    'cart.views',

    # Cart list
    url(
        r'^$',
        'cart_detail',
        name='cart_detail',
    ),

    # Cart complete order
    url(
        r'^complete/$',
        'cart_complete',
        name='cart_complete',
    ),
)
