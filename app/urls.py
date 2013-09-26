#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Home
    url(
        r'^$',
        'app.views.home',
        name='home',
    ),

    # Home
    url(
        r'^request_provider$',
        'landing.views.landing',
        name='landing',
    ),

    url(
        r'^LiguAdmin/',
        include(admin.site.urls)
    ),

    url(
        r'^accounts/',
        include('userprofile.backends.default.urls')
    ),

    # TinyMCE
    url(r'^tinymce/',
        include('tinymce.urls')
    ),

    # Social auth
    url(
        r'^accounts/',
        include('social_auth.urls'),
    ),

    url(
        r'^accounts/',
        include('userprofile.urls', namespace='userprofile')
    ),

    url(
        r'^cart/',
        include('cart.urls', namespace='cart')
    ),

    url(
        r'^',
        include('store.urls', namespace='store')
    ),
)

# Static content for development
urlpatterns += staticfiles_urlpatterns()

# Serve media for development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
