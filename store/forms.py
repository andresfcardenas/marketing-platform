#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from store.models import Store
from store.models import Product


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = (
            'name',
            'description',
            'logo',
            'phone',
            'address',
        )

    def __init__(self, *args, **kwargs):
        super(StoreForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(
            Submit(
                'submit',
                'Create store',
            ),
        )


class ProductForm(forms.ModelForm):
    tags = forms.CharField(
        max_length=256,
        required=False,
    )

    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'quantity',
            'category',
            'image',
            'price',
        )

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(
            Submit(
                'submit',
                'Create product',
            ),
        )


class StoreUpdateForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = (
            'name',
            'description',
            'phone',
            'address',
        )

    def __init__(self, *args, **kwargs):
        super(StoreUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(
            Submit(
                'submit',
                'Update store',
            ),
        )


class ProductUpdateForm(forms.ModelForm):
    tags = forms.CharField(
        max_length=256,
        required=False,
    )

    class Meta:
        model = Product
        fields = (
            'name',
            'description',
            'quantity',
            'category',
            'price',
        )

    def __init__(self, *args, **kwargs):
        super(ProductUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.add_input(
            Submit(
                'submit',
                'Update product',
            ),
        )

class UploadImageProductForm(forms.ModelForm):
    """Form to handle the upload of product images
    """
    class Meta:
        model = Product
        fields = ('image',)


class UploadImageStoreForm(forms.ModelForm):
    """Form to handle the upload of product images
    """
    class Meta:
        model = Store
        fields = ('logo',)
