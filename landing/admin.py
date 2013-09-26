#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.core.urlresolvers import reverse
from landing.models import LandingRegister
from landing.models import Slogan
from landing.models import MainImage
from landing.models import Testimonial
from landing.models import Function
from landing.models import Product
from landing.models import FormText

from tinymce.widgets import TinyMCE


class LandingRegisterAdmin(admin.ModelAdmin):
    model = LandingRegister
    list_display = (
        'name',
        'email',
        'was_contacted',
        'created_at',
    )

admin.site.register(LandingRegister, LandingRegisterAdmin)


class SloganAdmin(admin.ModelAdmin):
    model = Slogan
    list_display = (
        'slogan',
    )

admin.site.register(Slogan, SloganAdmin)


class MainImageAdmin(admin.ModelAdmin):
    model = MainImage
    list_display = (
        'Description',
    )

admin.site.register(MainImage, MainImageAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    model = Testimonial
    list_display = (
        'name',
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        """Using TinyMCE for description field.
        """
        if db_field.name == 'description':
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={
                    'height': '280',
                },
            ))

        return super(TestimonialAdmin, self).formfield_for_dbfield(
            db_field, **kwargs)

admin.site.register(Testimonial, TestimonialAdmin)


class FunctionAdmin(admin.ModelAdmin):
    model = Function
    list_display = (
        'name',
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        """Using TinyMCE for description field.
        """
        if db_field.name == 'description':
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={
                    'height': '280',
                },
            ))

        return super(FunctionAdmin, self).formfield_for_dbfield(
            db_field, **kwargs)

admin.site.register(Function, FunctionAdmin)


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = (
        'name',
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        """Using TinyMCE for description field.
        """
        if db_field.name == 'description':
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={
                    'height': '280',
                },
            ))

        return super(ProductAdmin, self).formfield_for_dbfield(
            db_field, **kwargs)

admin.site.register(Product, ProductAdmin)


class FormTextAdmin(admin.ModelAdmin):
    model = FormText
    list_display = (
        'title',
    )

admin.site.register(FormText, FormTextAdmin)
