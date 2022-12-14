"""
Django settings for emp_management project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from pickle import TRUE
import mimetypes

mimetypes.add_type("text/javascript", ".js", True)
mimetypes.add_type("text/css", ".css", True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_URL = '/media/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = '/static/'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, "static"),
# )
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# SECURITY WARNING: keep the secret key used in production secret!
STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
FILE_UPLOAD_MAX_MEMORY_SIZE = 5000000000 # 50 MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 5000000000 # 50 MB
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--jluq9g9%(-yfi@^*61$3p@&5k+j*pzua-ua+%1#ddl&zs1nb4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['*']
# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:4200',
# ]
ALLOWED_HOSTS = ['*']
#CORS_ALLOWED_ORIGINS = [
 #    'http://localhost:4200',
#]
# CORS_ALLOWED_ORIGINS = [
#     'http://localhost:4200',
# ]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    "corsheaders",
    'emps',
    'core'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
     'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
   
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
ROOT_URLCONF = 'emp_management.urls'


CORS_ALLOW_METHODS = [
'DELETE',
'GET',
'OPTIONS',
'PATCH',
'POST',
'PUT',
]

CORS_ALLOW_HEADERS = [
'accept',
'accept-encoding',
'authorization',
'content-type',
'dnt',
'origin',
'user-agent',
'x-csrftoken',
'x-requested-with',
'responseType',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS':[os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'whitenoise.middleware.WhiteNoiseMiddleware',
            ],
        },
    },
]

WSGI_APPLICATION = 'emp_management.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': 'TruckIndDB',
        #'NAME': os.getenv('db_name'),
        #'NAME': 'UsicDatabase',
        'NAME':'falcondbnew2022',
        #'NAME': 'dd21t9dbu9d5fc',
        #'NAME':'d31kkhodt6k2pd',
        #'USER':'dexwdojwynhgbo',
        #'USER':'gtyntnnumyrhdt',
        #'NAME': 'ins',
        #'USER':'postgres',
        'USER':'falconadmin',
        #'USER': os.getenv('db_user'),
        #'PASSWORD': '46e15532c5843dafdb7faeec89e7715389ae5693ddd434f95bcd596adfc05bc3',
        #'PASSWORD': '518c492a5860be50c7a26790229dc5a4d5017dbc2724ded6fdf76200e62fe4ea',
        #'PASSWORD': 'light9494',
        'PASSWORD':'Nta@2022$$!',
        #'PASSWORD': os.getenv('db_password'),
        #'HOST': 'ec2-3-224-157-224.compute-1.amazonaws.com',
        #'HOST':'ec2-3-229-8-233.compute-1.amazonaws.com',
       # 'HOST': 'localhost',
        'HOST':'falcondbnew2022.postgres.database.azure.com',
        #'HOST': os.getenv('db_host'),
        #'OPTIONS':{
        #    'sslmode':'require'},
        #'PORT':os.getenv('db_port')
        'PORT': '5432',
        
    }
}



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
