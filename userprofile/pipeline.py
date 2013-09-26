#! /usr/bin/env python
# -*- coding: utf-8 -*-
from userprofile.models import UserProfile

from social_auth.backends.facebook import FacebookBackend
from social_auth.backends.twitter import TwitterBackend


def update_user_social_data(backend, details, response, social_user, uid,
                            user, *args, **kwargs):
    """Update the information for the user profile
    """
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if created:
        if backend.__class__ == FacebookBackend:
            user_profile.facebook_uid = response['id']

        elif backend.__class__ == TwitterBackend:
            user_profile.twitter = response['screen_name']

        user_profile.save()
