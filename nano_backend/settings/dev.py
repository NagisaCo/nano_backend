# 开发阶段配置文件

"""
Django settings for meiduo project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys
import datetime

MYSQL_HOST = os.environ.get('MYSQL_HOST', '192.168.239.128')
REDIS_HOST = os.environ.get('REDIS_HOST', '192.168.239.128')
FDFS_HOST = os.environ.get('FDFS_HOST', '192.168.239.128')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))  # 新增导包路径

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-186w)w_wu3s_%_0#@v3l357hb^jy$j5sj6pc1iw0m46$)74k_*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
]

# Application definition

# 注册应用
INSTALLED_APPS = [
    'simpleui',  # admin ui

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',  # DRF
    'corsheaders',  # CORS 跨域
    'rest_framework_simplejwt',  # JWT
    'drf_spectacular',  # api 文档
    'django_filters',  # 过滤器

    'users',  # 用户
    'animes',  # 番剧
    'places',  # 地点
    'photos',  # 照片
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS 跨域(最外层)
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nano_backend.urls'

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

WSGI_APPLICATION = 'nano_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': MYSQL_HOST,  # 数据库主机
        'PORT': 3306,  # 数据库端口
        'USER': 'nano',  # 数据库用户名
        'PASSWORD': 'nano',  # 数据库用户密码
        'NAME': 'nano'  # 数据库名字
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

# Redis
CACHES = {
    "default": {  # 缓存数据
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {  # 缓存 session
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "verify_codes": {  # 存储验证码
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# Log
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'standard': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'verbose': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/nano.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
        'animes': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/animes.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
        'photos': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/photos.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
        'places': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/places.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
        'users': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/users.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
        'verifications': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "logs/verifications.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {  # 日志器
        'nano': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
        'animes': {
            'handlers': ['console', 'animes'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
        'photos': {
            'handlers': ['console', 'photos'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
        'places': {
            'handlers': ['console', 'places'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
        'users': {
            'handlers': ['console', 'users'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
        'verifications': {
            'handlers': ['console', 'verifications'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    }
}

# DRF
REST_FRAMEWORK = {
    # 异常处理
    'EXCEPTION_HANDLER': 'nano_backend.utils.exceptions.exception_handler',

    # 认证配置
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    # 全局认证 优先级高于试图类中的配置 login view中，进行用户验证时
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],

    # api 默认文档
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    # 过滤器
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),

    # 分页
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,  # 默认每页数目
    'PAGE_SIZE_QUERY_PARAM': 'page_size',  # 控制每页数目的参数
}

# CORS
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8080',
    'http://localhost:8080',
    'https://127.0.0.1:8080',
    'https://localhost:8080'
)

CORS_ALLOW_CREDENTIALS = True  # 允许携带cookie

# JWT(new)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=10),
    'ALGORITHM': 'HS256',
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION'
}

# 自定义用户类
AUTH_USER_MODEL = 'users.User'

# API 文档设置
SPECTACULAR_SETTINGS = {
    'TITLE': 'nano API接口文档',
    # 'DESCRIPTION': '',
    'VERSION': '1.0.0',
    # OTHER SETTINGS
}

# django文件存储
DEFAULT_FILE_STORAGE = 'nano_backend.utils.fastdfs.fdfs_storage.FastDFSStorage'

# FastDFS
FDFS_URL = f'http://{FDFS_HOST}:8888/'
FDFS_CLIENT_CONF = os.path.join(BASE_DIR, 'utils/fastdfs/client.conf')

# Avatar
DEFAULT_AVATAR_PATH = f'group1/M00/00/00/wKjvgGGoiV-AETMXAAAMK5bwTxs200.jpg'

# admin
SIMPLEUI_CONFIG = {
    'system_keep': False,
    'menus': [
        {
            'name': 'Nano',
            'icon': 'fas fa-server',
            'models': [
                {
                    'name': 'Anime 番剧',
                    'icon': 'fas fa-video',
                    'url': 'animes/anime/'
                },
                {
                    'name': 'Place 地点',
                    'icon': 'fas fa-map',
                    'url': 'places/place/'
                },
                {
                    'name': 'Photo 照片',
                    'icon': 'fas fa-camera',
                    'url': 'photos/photo/'
                }
            ],
        },
        {
            'name': 'User 用户',
            'icon': 'fas fa-user',
            'url': 'users/user/'
        }
    ]
}
