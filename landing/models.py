#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models


class LandingRegister(models.Model):
    """This model represent a register in landing page.
    """
    name = models.CharField(
        max_length=50,
    )

    email = models.EmailField(
        max_length=250,
    )

    details = models.TextField(
        max_length=600,
        null=True,
    )

    was_contacted = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __unicode__(self):
        return u'{0}'.format(self.name)


class Slogan(models.Model):
    """This model represent the slogan text.
    """
    slogan = models.CharField(
        max_length=100,
    )

    def __unicode__(self):
        return u'{0}'.format(self.slogan)


class MainImage(models.Model):
    """This model represent the main image.
    """
    Description = models.TextField(
        max_length=200,
    )

    image = models.ImageField(
        upload_to='uploads/landing/main',
        null=True,
        blank=True,
    )


class Testimonial(models.Model):
    """This model represent a testimonial.
    """
    name = models.CharField(
        max_length=50,
    )

    description = models.TextField(
        max_length=200,
    )

    image = models.ImageField(
        upload_to='uploads/landing/testimonial',
        null=True,
        blank=True,
    )

    def __unicode__(self):
        return u'{0}'.format(self.name)


class Function(models.Model):
    """This model represent a description for functions.
    """
    name = models.CharField(
        max_length=50,
    )

    description = models.TextField(
        max_length=200,
    )

    image = models.ImageField(
        upload_to='uploads/landing/function',
        null=True,
        blank=True,
    )

    def __unicode__(self):
        return u'{0}'.format(self.name)


class Product(models.Model):
    """This model represent a description for functions.
    """
    name = models.CharField(
        max_length=50,
    )

    description = models.TextField(
        max_length=200,
    )

    image = models.ImageField(
        upload_to='uploads/landing/product',
        null=True,
    )

    def __unicode__(self):
        return u'{0}'.format(self.name)


class FormText(models.Model):
    """Represet a title and text in form"""
    title = models.CharField(
        max_length=50,
    )

    text = models.TextField(
        max_length=200,
    )

    def __unicode__(self):
        return u'{0}'.format(self.title)
