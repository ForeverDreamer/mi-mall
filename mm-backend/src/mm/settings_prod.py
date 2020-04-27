"""
Django settings for mm project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

# # settings_prod.py

import os
import json
from datetime import timedelta

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open(os.path.join(BASE_DIR, 'mm', 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

# SERVER_EMAIL = 'root@localhost'
#
# ADMINS = [('admin', '499361328@qq.com')]

# MANAGERS = [('admin', '499361328@qq.com')]

ALLOWED_HOSTS = ['.itman.icu']

PROJECT_NAME = 'mm'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    # Third apps
    'corsheaders',
    'rest_framework',
    'django_filters',
    'django_oss_storage',
    # Local apps
    'account',
    'analysis',
    'product',
    'order',
    'cart',
    'pay',
    'vue_admin',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

# # 避免跨域访问删除token cookies，不用也暂时没发现问题
# SESSION_COOKIE_SAMESITE = None

# import re
#
# IGNORABLE_404_URLS = [
#     re.compile(r'^/apple-touch-icon.*\.png$'),
#     re.compile(r'^/favicon\.ico$'),
#     re.compile(r'^/robots\.txt$'),
# ]

ROOT_URLCONF = 'mm.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'mm', 'templates')],
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

WSGI_APPLICATION = 'mm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mmdb',
        'USER': 'root',
        'PASSWORD': 'MyNewPass4!',
        'HOST': 'db',
        'PORT': 3306,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATICFILES_STORAGE = 'django_oss_storage.backends.OssStaticStorage'

DEFAULT_FILE_STORAGE = 'django_oss_storage.backends.OssMediaStorage'

# AliCloud access key ID
with open(os.path.join(BASE_DIR, 'mm', 'AccessKeyID.txt')) as f:
    OSS_ACCESS_KEY_ID = f.read().strip()

# AliCloud access key secret
with open(os.path.join(BASE_DIR, 'mm', 'AccessKeySecret.txt')) as f:
    OSS_ACCESS_KEY_SECRET = f.read().strip()

OSS_EXPIRE_TIME = 30

# The name of the bucket to store files in
OSS_BUCKET_NAME = 'itman-nuxt-app'

# The URL of AliCloud OSS endpoint
# Refer https://www.alibabacloud.com/help/zh/doc-detail/31837.htm for OSS Region & Endpoint
OSS_ENDPOINT = 'oss-cn-qingdao.aliyuncs.com'

# The default location for your files
MEDIA_URL = '/media/'

# The default location for your static files
# STATIC_URL = '/'
STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     os.path.join(os.path.dirname(BASE_DIR), "frontend"),
# ]


CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://cache_db:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework.parsers.JSONParser',
    # ],
    'EXCEPTION_HANDLER': 'mm.utils.custom_exception_handler',
    'DEFAULT_PAGINATION_CLASS': 'product.pagination.ProductPagination',
    'SEARCH_PARAM': 'q',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

# DEFAULT_FROM_EMAIL = 'webmaster@localhost'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {pathname} {funcName} {lineno} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {asctime} {pathname} {funcName} {lineno} {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'mm_file': {
            'level': 'WARNING',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "log", "mm.log"),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'delay': True,
            'formatter': 'verbose'
        },
        'django_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "log", "django.log"),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'delay': True,
            'formatter': 'simple'
        },
        'django_console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
    },
    'loggers': {
        'mm': {
            'handlers': ['mm_file'],
            # 'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'level': 'WARNING',
            'propagate': True,
        },
        'django': {
            'handlers': ['django_file'],
            'level': 'ERROR',
            # 'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': True,
        },
    },
}

# 其实不需要用json文件，直接创建email_info.py，使用dict就行
with open(os.path.join(BASE_DIR, 'mm', 'email_info.json')) as f:
    email_info = json.load(f)
# 设置邮件域名
EMAIL_HOST = email_info['EMAIL_HOST']
# 设置端口号，为数字
EMAIL_PORT = email_info['EMAIL_PORT']
# 设置发件人邮箱
EMAIL_HOST_USER = email_info['EMAIL_HOST_USER']
# 设置发件人密码
EMAIL_HOST_PASSWORD = email_info['EMAIL_HOST_PASSWORD']
# 设置是否启用安全链接
EMAIL_USER_TLS = bool(email_info['EMAIL_USER_TLS'])