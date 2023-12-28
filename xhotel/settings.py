"""
Django settings for xhotel project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from datetime import timedelta
import os
from pathlib import Path

# ...

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-97=wl=xs*0^zo8=p6=kpnq&)d$(r+1_)z9%d4k(%!##*jn8*a$'
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your_default_secret_key')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']  # For testing purposes; update with your domain in production


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'media',
    'event',
    'contactus',
    'bookings',   
    'review',   
    'payment',
    'django_rest_passwordreset',
    'accounts.apps.AccountsConfig',
    'corsheaders',
    'profiel',
    'dj_rest_auth',
    'admin_user',

]


CORS_ALLOW_CREDENTIALS = True

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'allauth.account.middleware.AccountMiddleware',

]

ROOT_URLCONF = 'xhotel.urls'





DEBUG = True
# ALLOWED_HOSTS = ['127.0.0.1','.vercel.app','.now.sh','localhost']
CORS_ALLOW_HEADERS = ['Access-Control-Allow-Headers',    'Origin',    'X-Requested-With',    'Content-Type',    'Accept',    'Authorization']
CSRF_TRUSTED_ORIGINS = ['http://', 'https://']
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

CORS_ALLOWED_ORIGINS = [
    # add the domains that you want to allow
    # for example:
    'http://localhost:3000',
    'https://localhost:3000'
    # ...
]


CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)



# CSRF_COOKIE_SECURE = False
# CSRF_COOKIE_SAMESITE = 'Lax'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates/',],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'xhotel.wsgi.application'

# Add the following ASGI setting
ASGI_APPLICATION = 'xhotel.asgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "xcv",
#         "USER": "postgres",
#         "PASSWORD":"147147147",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'A1Fd*ddbdcGae4d5egEgDdbGAB*BgcGd',
        'HOST': 'roundhouse.proxy.rlwy.net',
        'PORT': '28112',
    }
}

# Authentication backends
AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Use the following configuration for the authentication classes
AUTHENTICATION_CLASSES = [
    'dj_rest_auth.authentication.AllAuthJWTAuthentication',
]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'defaultdb',
#         'USER': 'avnadmin',
#         'PASSWORD': 'AVNS_Nye0_kgCiDGw2QzGi8b',
#         'HOST': 'pg-x-abdow88988-c44a.a.aivencloud.com',
#         'PORT': '22471',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

# settings.py
STATIC_URL = '/static_root/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root','staticfiles_build')



# STATIC_URL = '/static/'

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'accounts.CustomUser'
# Authentication classes
AUTHENTICATION_CLASSES = (
    # ...
    'djoser.backends.jwt.JWTAuthentication',
    # ... other authentication classes ...
)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7), 
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'JTI_CLAIM': 'jti',
    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(days=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# mydrfproject/settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'   # Replace with your preferred backend

EMAIL_PORT = 587  # Replace with your email port
EMAIL_USE_TLS = True  # Set to False if your email server doesn't use TLS
EMAIL_HOST = 'smtp.gmail.com'  # Replace with your email host for gmail -> 'smtp.gmail.com'
EMAIL_HOST_USER = 'xhotel90@gmail.com'  # Replace with your email username
EMAIL_HOST_PASSWORD = 'mnvvnqnmnaelknwz'  # Replace with your email password



# settings.py

# Allauth settings
ACCOUNT_EMAIL_VERIFICATION = 'MANDATORY' 
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = '/'
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = '/'
# ACCOUNT_EMAIL_CONFIRMATION_MODEL = 'custom_auth.CustomEmailConfirmation'

# Email confirmation templates
ACCOUNT_EMAIL_CONFIRMATION_SIGNUP_MESSAGE = 'accounts/email/confirmation_signup_message.txt'
ACCOUNT_EMAIL_CONFIRMATION_URL = 'account-confirm-email'
ACCOUNT_EMAIL_CONFIRMATION_HMAC = True

# Ensure that SECURE_SSL_REDIRECT is set to False in development
SECURE_SSL_REDIRECT = False

