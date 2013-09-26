#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

from uuid import uuid4

from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

from userprofile.models import UserProfile
from userprofile.forms import UserRegistrationForm

from registration import signals
from registration.models import RegistrationProfile
from registration.views import ActivationView as BaseActivationView
from registration.views import RegistrationView as BaseRegistrationView

def generate_unique_username(username):
    """Generates unique username. Based on work done by django-social-auth
    """
    maxlen = 22
    uuid_length = 8
    clean_username_regex = re.compile(r'[^\w.@+-_]+')

    initial_username = clean_username_regex.sub('', u'{0}'.format(username))
    username = initial_username[:maxlen + uuid_length]

    while User.objects.filter(username=username).count() > 0:
        username = initial_username[:maxlen] + uuid4().get_hex()[:uuid_length]

    return username


class RegistrationView(BaseRegistrationView):
    """
    The backend for django registration.    
    """
    def register(self, request, **cleaned_data):
        username =  generate_unique_username('{0}.{1}'.format(cleaned_data['name'], cleaned_data['lastname']))
        name, lastname = cleaned_data['name'], cleaned_data['lastname']
        email, password = cleaned_data['email'], cleaned_data['password1']

        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)

        new_user = RegistrationProfile.objects.create_inactive_user(
            username,
            email,
            password,
            site,
        )
        new_user.first_name = name
        new_user.last_name = lastname
        new_user.save()

        UserProfile.objects.create(
            user=new_user
        ).save()

        signals.user_registered.send(
            sender=self.__class__,
            user=new_user,
            request=request,
        )

        return new_user

    def get_form_class(self, request):
        """Return the form to show at registration page
        """
        return UserRegistrationForm

    def registration_allowed(self, request):
        """
        Indicate whether account registration is currently permitted,
        based on the value of the setting ``REGISTRATION_OPEN``. This
        is determined as follows:

        * If ``REGISTRATION_OPEN`` is not specified in settings, or is
          set to ``True``, registration is permitted.

        * If ``REGISTRATION_OPEN`` is both specified and set to
          ``False``, registration is not permitted.
        
        """
        return getattr(settings, 'REGISTRATION_OPEN', True)

    def get_success_url(self, request, user):
        """
        Return the name of the URL to redirect to after successful
        user registration.
        
        """
        return ('registration_complete', (), {})


class ActivationView(BaseActivationView):
    def activate(self, request, activation_key):
        """
        Given an an activation key, look up and activate the user
        account corresponding to that key (if possible).

        After successful activation, the signal
        ``registration.signals.user_activated`` will be sent, with the
        newly activated ``User`` as the keyword argument ``user`` and
        the class of this backend as the sender.
        
        """
        activated_user = RegistrationProfile.objects.activate_user(activation_key)
        if activated_user:
            signals.user_activated.send(sender=self.__class__,
                                        user=activated_user,
                                        request=request)
        return activated_user

    def get_success_url(self, request, user):
        return ('registration_activation_complete', (), {})

def login_on_activation(user, request, **kwargs):
    """Log the user in after link activation
    """
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)

signals.user_activated.connect(login_on_activation)
