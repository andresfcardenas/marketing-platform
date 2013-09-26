#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from userprofile.models import ProviderRequest


class UserRegistrationForm(forms.Form):
    """Form to allow the registration of users
    """
    name = forms.CharField(
        max_length=75,
        label='',
    )

    lastname = forms.CharField(
        max_length=75,
        label='',
    )

    email = forms.EmailField(
        max_length=75,
        label='',
    )

    password1 = forms.CharField(
        max_length=75,
        widget=forms.PasswordInput(render_value=False),
        label='',
    )

    def clean_email(self):
        """Check the uniqueness of the email address
        """
        if User.objects.filter(email=self.cleaned_data['email']):
            raise forms.ValidationError(
                "Are you sure you are not registered?")
        return self.cleaned_data['email']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['lastname'].widget.attrs['placeholder'] = 'Lastname'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'

        self.helper.add_input(
            Submit(
                'submit',
                'Create account',
            ),
        )


class ProviderRequestForm(forms.Form):
    """This model represent a form for provider's request.
    """
    name = forms.CharField(
        max_length=200,
        label='',
    )

    email = forms.EmailField(
        max_length=100,
        label='',
    )

    product = forms.CharField(
        max_length=200,
        label='',
    )

    phone = forms.CharField(
        max_length=10,
        label='',
    )

    more_info = forms.CharField(
        max_length=500,
        widget=forms.Textarea,
        label='',
    )

    def __init__(self, *args, **kwargs):
        super(ProviderRequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['name'].widget.attrs['placeholder'] = 'Tu nombre completo'
        self.fields['email'].widget.attrs['placeholder'] = 'Correo electrónico'
        self.fields['product'].widget.attrs['placeholder'] = '¿Qué producto ofreces?'
        self.fields['phone'].widget.attrs['placeholder'] = 'Teléfono'
        self.fields['more_info'].widget.attrs['placeholder'] = 'Danos más información de tu producto. :)'

        self.helper.add_input(
            Submit(
                'submit',
                'Aplicar como proveedor',
            )
        )

