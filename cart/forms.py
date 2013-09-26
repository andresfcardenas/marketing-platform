#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class CartForm(forms.Form):
    """Cart form for fill with contact info
    """
    email = forms.EmailField(
        label=u'Email',
    )

    name = forms.CharField(
        max_length=100,
        label=u'Nombre completo',
    )

    address = forms.CharField(
        max_length=200,
        label=u'Dirección',
    )

    phone = forms.CharField(
        max_length=100,
        label=u'Teléfono',
    )

    message = forms.CharField(
        max_length=256,
        label=u'Información adicional',
        widget=forms.Textarea,
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'shopform'
        self.helper.form_class = 'form-inline'
        self.helper.add_input(Submit('submit', 'Comprar', css_id='submit'))

        super(CartForm, self).__init__(*args, **kwargs)