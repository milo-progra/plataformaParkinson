import os
from pathlib import Path
from django.urls import reverse_lazy 
#bibloteca pip install python-decouple que te permite utilizar variables de entorno
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-rom+yn2rgvh7y8oqf4zuhkk3_!hb7tuyal_1dykkbb45q1wwje'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

MESSAGE_STORAGE="django.contrib.messages.storage.cookie.CookieStorage"


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
    'rest_framework',
    'usuario',
    'paciente',
    'medico_y_enfermera',
    'medicamento',
    'fonoaudiologo',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #logout
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
]

ROOT_URLCONF = 'sitioweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'sitioweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE'    : config('ENGINE'),
        'NAME'      : config('NAME'),
        'USER'      : config('USER'),
        'PASSWORD'  : config('PASSWORD'),
        'HOST'      : config('HOST'),
        'PORT'      : config('PORT'),
    }
}


#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql',
#        'NAME': 'vozparkinson$default',
#        'USER': 'vozparkinson',
#        'PASSWORD': 'MYSQL12345',
#        'HOST': 'vozparkinson.mysql.pythonanywhere-services.com',
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators



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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'app/static'),)
#STATIC_ROOT = STATIC_URL
MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

LOGIN_REDIRECT_URL='/post_login/'
LOGOUT_REDIRECT_URL ='/'

AUTH_USER_MODEL = 'usuario.Usuario'






#Es recomendable crear variables de entorno para guardar tu informacion de correo
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend" 
#EMAIL_HOST    = "smtp.office365.com" 
EMAIL_HOST     = config('EMAIL_HOST')
EMAIL_USE_TLS = True 
EMAIL_PORT    = config('EMAIL_PORT') 
EMAIL_HOST_USER = config('EMAIL') 
EMAIL_HOST_PASSWORD = config('EMAIL_PASSWORD')
SERVER_EMAIL = EMAIL_HOST_USER

#configuracion timeout
SESSION_EXPIRE_SECONDS = 600  # 10 minutos
SESSION_TIMEOUT_REDIRECT = '/'
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True