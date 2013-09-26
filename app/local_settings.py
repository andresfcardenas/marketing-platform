#! /usr/bin/env python
# -*- coding: utf-8 -*-
from settings import *

DEBUG = True
TEMPLATE_DEBUG = True

DATABASES['default']['NAME'] = 'market'
DATABASES['default']['USER'] = 'market'
DATABASES['default']['PASSWORD'] = 'market'
DATABASES['default']['HOST'] = 'localhost'

EMAIL_USE_TLS = False
EMAIL_HOST = 'mail.real.quijost.com'
EMAIL_HOST_USER = 'ligu_register@real.quijost.com'
EMAIL_HOST_PASSWORD = 'LJ%Lt)1Sq,5='
EMAIL_PORT = 25

FACEBOOK_APP_ID = '171975006323659'
FACEBOOK_API_SECRET = 'c0a879a159e842a91a874d8b126db829'

TWITTER_CONSUMER_KEY = 'mhXHG0eCgYC10iQAGRySg'
TWITTER_CONSUMER_SECRET = 'Lxip3vy7oVL7ZncR9IIaFelcQtmy4WkOWaF9Lkd1k'
