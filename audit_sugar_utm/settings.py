import os
from configurations import Configuration, values

from .settings_private import DatabaseDevMixin


class Base(Configuration):
    """Базовый класс конфигурации"""
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Перед запуском задайте переменную окружения DJANGO_SECRET_KEY
    # В linux надо обратить внимание на команду export
    SECRET_KEY = values.SecretValue()

    DEBUG = False

    ALLOWED_HOSTS = []

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'django_extensions',

        'utm_billing.apps.UtmbillingConfig',
        'sugar_crm.apps.SugarCrmConfig',
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'audit_sugar_utm.urls'

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

    WSGI_APPLICATION = 'audit_sugar_utm.wsgi.application'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

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

    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    STATIC_URL = '/static/'
    LOGIN_REDIRECT_URL = '/'
    LOGIN_URL = 'login'


class Dev(DatabaseDevMixin, Base):
    DEBUG = True
    INSTALLED_APPS = Base.INSTALLED_APPS + ['debug_toolbar']
    MIDDLEWARE = Base.MIDDLEWARE + [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]
    INTERNAL_IPS = ['127.0.0.1', '172.18.0.1']
    ALLOWED_HOSTS = Base.ALLOWED_HOSTS + ['127.0.0.1', 'testserver']
    STATIC_ROOT = os.path.join(Base.BASE_DIR, 'static')
