#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    """Allow a user to be authenticated using an email address
    """
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
        except:
            pass

        return None