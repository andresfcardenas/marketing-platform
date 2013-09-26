#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG
GOOGLETOOLS_ENABLED = True

ADMINS = (
    (u'Andrés F. Cárdenas', 'akardenasjimenez@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

ALLOWED_HOSTS = ['ligu.com.co', 'real.quijost.com', 'localhost']

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    # MEDIA_ROOT,
)


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

SECRET_KEY = '*h@dkp)c%vi29s@s5dn+su!3x-t8i0@3sm(#^2j*)#^b86@x6_'

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)

# HTTPS MIDDLEWARE CONFIG
HTTPS_SUPPORT = True
SECURE_REQUIRED_PATHS = (
    '/accounts'
    '/LiguAdmin/',
    # you can add in more path here if you want the path to use https
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'app.middleware.SecureRequiredMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Django-registration config
AUTH_PROFILE_MODULE = 'userprofile.UserProfile'
ACCOUNT_ACTIVATION_DAYS = 7

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

OWN_APPS = (
    'app',
    'userprofile',
    'store',
    'cart',
    'landing',
)

INSTALLED_APPS = OWN_APPS + (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django_extensions',
    'easy_thumbnails',
    'googletools',
    'registration',
    'crispy_forms',
    'social_auth',
    'south',
    'tinymce',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request'
)


# Email Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'Ligu.co <contactanos@ligu.com.co>'
SERVER_EMAIL = 'ligu@ligu.co'
EMAIL_REPLY_TO = ('',)
CONTACT_EMAIL = 'contactanos@ligu.com.co'

# Social auth
SOCIAL_AUTH_SESSION_EXPIRATION = False
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'userprofile.login_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

FACEBOOK_EXTENDED_PERMISSIONS = [
    'email',
    'user_location',
    'publish_stream',
    'offline_access',
]
SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'userprofile.pipeline.update_user_social_data',
)

# Better password storage
PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)

# Easy Thumbnails
THUMBNAIL_MEDIA_URL = STATIC_URL
THUMBNAIL_MEDIA_ROOT = STATIC_ROOT
THUMBNAIL_BASEDIR = 'thumbnails'
THUMBNAIL_ALIASES = {
    '': {
        'avatar_78': {
            'size': (78, 78), 'crop': ',', 'upscale': False,
        },

        'avatar_140': {
            'size': (140, 140), 'crop': ',', 'upscale': False,
        },

        'avatar_169': {
            'size': (169, 168), 'crop': ',', 'upscale': False,
        },

        'avatar_273': {
            'size': (273, 142), 'crop': ',', 'upscale': False,
        },

        'avatar_316': {
            'size': (316, 316), 'crop': ',', 'upscale': False,
        },

        'avatar_355': {
            'size': (618, 355), 'crop': ',', 'upscale': False,
        },

        'avatar_400': {
            'size': (770, 400), 'crop': ',', 'upscale': False,
        },
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
            'filters': ['require_debug_false'],
             # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },
        # Log to a text file that can be rotated by logrotate
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': '/var/log/django/ligu.log'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propagate': False,
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'app': {
            'handlers': ['logfile'],
            'level': 'WARNING', # Or maybe INFO or DEBUG
            'propogate': False
        },
    }
}

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# TinyMCE
TINYMCE_JS_ROOT = '/static/tiny_mce/'
TINYMCE_JS_URL = os.path.join(STATIC_URL, "tiny_mce/tiny_mce_src.js")

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
}

# Local settings
settings_file = __import__('app.local_settings').local_settings
for setting_value in dir(settings_file):
    locals()[setting_value] = getattr(settings_file, setting_value)
