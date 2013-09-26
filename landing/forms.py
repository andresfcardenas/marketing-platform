#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from landing.models import LandingRegister


class LandingForm(forms.ModelForm):
    class Meta:
        model = LandingRegister
        fields = (
            'name',
            'email',
        )

    def __init__(self, *args, **kwargs):
        super(LandingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

        self.helper.add_input(
            Submit(
                'submit',
                'Solicitar Información',
                css_class='button'
            ),
        )
