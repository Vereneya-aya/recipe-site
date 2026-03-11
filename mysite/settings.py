import os
import logging.config
from pathlib import Path
from dotenv import load_dotenv
from django.urls import reverse_lazy
import dj_database_url

# Загрузка .env
load_dotenv()

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Основные настройки
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "your-default-secret")
DEBUG = os.getenv("DJANGO_DEBUG", "0") == "1"

# Разрешённые хосты
ALLOWED_HOSTS = [
    "127.0.0.1",
    "0.0.0.0",
    "recipe-site-production.up.railway.app",
]

# Если DJANGO_ALLOWED_HOSTS задан и не пуст, добавляем их
extra_hosts = os.getenv("DJANGO_ALLOWED_HOSTS")
if extra_hosts:
    ALLOWED_HOSTS += [host.strip() for host in extra_hosts.split(",") if host.strip()]

# Установленные приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Сторонние
    'rest_framework',
    'django_filters',
    'drf_yasg',
    'debug_toolbar',

    # Собственные
    'recipe_app',
    'user_app',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# URL-конфигурация
ROOT_URLCONF = 'mysite.urls'  # Убедись, что у тебя папка называется mysite. Иначе замени.

# Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# WSGI-приложение
WSGI_APPLICATION = 'mysite.wsgi.application'  # проверь, что wsgi.py лежит именно в mysite

# База данных
if os.getenv("DATABASE_URL"):  # Railway
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600)
    }
else:  # Локальная SQLite
    DATABASE_DIR = BASE_DIR / "database"
    DATABASE_DIR.mkdir(exist_ok=True)
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': DATABASE_DIR / 'db.sqlite3',
        }
    }

# Валидаторы паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Интернационализация
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# Статические и медиа-файлы
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Настройки входа/выхода
LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = reverse_lazy("user_app:profile")
LOGOUT_REDIRECT_URL = '/users/login/'

# Настройки DRF
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
}

# Логирование
LOGLEVEL = os.getenv("DJANGO_LOGLEVEL", "INFO").upper()
logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "[{levelname}] {asctime} {name} - {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    "loggers": {
        "": {
            "level": LOGLEVEL,
            "handlers": ["console"],
        },
    },
})

# IP для debug_toolbar
INTERNAL_IPS = ['127.0.0.1']

# Поле ID по умолчанию
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CSRF_TRUSTED_ORIGINS = [
    "https://recipe-site-production.up.railway.app",
]