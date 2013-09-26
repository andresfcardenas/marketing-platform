#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib import admin

from userprofile.models import UserProfile
from userprofile.models import ProviderRequest


class UserProfileAdmin(admin.ModelAdmin):
    """Admin for UserProfile model.
    """

    list_display = [
        'user',
    ]

admin.site.register(UserProfile, UserProfileAdmin)


class ProviderRequestAdmin(admin.ModelAdmin):
    """Admin for UserProfile model.
    """

    list_display = [
        'name',
        'email',
        'product',
        'phone',
    ]

admin.site.register(ProviderRequest, ProviderRequestAdmin)