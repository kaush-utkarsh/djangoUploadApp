"""
Django settings for WeEdit project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zwj)v2+q#nq%#xyp$qpu($6%b_kj)_-a3x^udoouo9f7h_p#ek'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'login',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'django.contrib.auth.backends.ModelBackend',
)


SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'login.views.save_profile',  # <--- set the path to the function
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details'
)


LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'WeEdit.urls'


    

TEMPLATE_DIRS = (
   os.path.join('templates/'),
)

WSGI_APPLICATION = 'WeEdit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'weedit',
        'USER' : 'root',
        'PASSWORD' : "password",
        'HOST' : '127.0.0.1',
        'PORT' : 3306,
    }
}

SOUTH_DATABASE_ADAPTERS = {
    'default':'south.db.mysql'
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_PATH = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)


SOCIAL_AUTH_FACEBOOK_KEY ='178681532464428'
SOCIAL_AUTH_FACEBOOK_SECRET ='dc32dc72be056068a530eb68b704b14b'

SOCIAL_AUTH_FACEBOOK_KEY = '944310785629217'
SOCIAL_AUTH_FACEBOOK_SECRET = 'd2e5688437bf6de58adee80e7d3d587f'

#SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='584696154376-qndne8hmetetnompekupcn1lpkg24r81.apps.googleusercontent.com'
#SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ='eW-kBdEAzO-ffK-YNq6Z3nty'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '384129660158-gmhmadac3cpql8bfku7p7rp8cis92qic.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'JQRZqyFx8weFQr2R6NQw9nDg'

MEDIA_ROOT = "/home/ubuntu/uploads"
