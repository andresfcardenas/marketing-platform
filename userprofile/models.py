#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models

from autoslug import AutoSlugField


class UserProfile(models.Model):
    """This model represent a user profile
    """
    user = models.OneToOneField(
        'auth.User',
    )

    is_provider = models.BooleanField(
        default=False,
    )

    facebook_uid = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u'Facebook'
    )

    twitter = models.CharField(
        max_length=256,
        blank=True,
    )

    slug = AutoSlugField(
        unique=True,
        always_update=True,
        populate_from=lambda instance: instance.user.get_full_name(),
    )

    @property
    def get_twitter_association(self):
        """Return the social auth association with twitter
        """
        sa_list = self.user.social_auth.filter(provider='twitter')
        if sa_list:
            return sa_list[0]

        return None

    @property
    def get_facebook_association(self):
        """Return the social auth association with facebook
        """
        sa_list = self.user.social_auth.filter(provider='facebook')
        if sa_list:
            return sa_list[0]

        return None

    def __unicode__(self):
        return u'{0} {1}'.format(self.user.first_name, self.user.last_name)


class ProviderRequest(models.Model):
    """This model represent a provider request for join to Ligu.
    """
    name = models.CharField(
        max_length=200,
    )

    email = models.EmailField(
    )

    product = models.CharField(
        max_length = 200,
    )

    phone = models.CharField(
        max_length = 10,
    )

    more_info = models.TextField(
        max_length=500,
    )

    def __unicode__(self):
        return u'{0}'.format(self.name)
