#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    'userprofile.views',

    # login
    url(
        r'^ajax-login/$',
        'ajax_login',
        name='ajax_login',
    ),

    # Ajax register
    url(
        r'^ajax-register/$',
        'ajax_register',
        name='ajax_register',
    ),

    # Ajax register
    url(
        r'^ajax-provider-request/$',
        'ajax_provider_request',
        name='ajax_provider_request',
    ),

    # dashboard
    url(
        r'^dashboard/$',
        'dashboard',
        name='dashboard',
    ),
)
