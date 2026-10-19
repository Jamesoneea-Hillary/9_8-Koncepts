from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: set DJANGO_SECRET_KEY in every deployed environment.
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "django-insecure-local-development-only")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "true").lower() in {"1", "true", "yes"}

ALLOWED_HOSTS = [
    '127.0.0.1', 
    'localhost', 
    '.ngrok-free.app', 
    '.ngrok-free.dev'
]

CSRF_TRUSTED_ORIGINS = ['https://*.ngrok-free.dev', 'https://*.ngrok-free.app']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party
    'django_ckeditor_5',
    "crispy_forms",
    "crispy_bootstrap5",

    # Local Apps
    "core",
    "services",
    "portfolio",
    "contact",
    "blog",
    "team",
    "testimonials",
    "careers",
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "core.context_processors.site_settings",
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Optional server-side assistant configuration. Set an API-compatible endpoint,
# key, and model in the deployment environment to enable generated answers.
ASSISTANT_API_KEY = os.environ.get("ASSISTANT_API_KEY", "")
ASSISTANT_API_URL = os.environ.get("ASSISTANT_API_URL", "https://api.openai.com/v1/chat/completions")
ASSISTANT_MODEL = os.environ.get("ASSISTANT_MODEL", "gpt-4o-mini")
WHATSAPP_NUMBER = os.environ.get("WHATSAPP_NUMBER", "")
ASSISTANT_RATE_LIMIT = int(os.environ.get("ASSISTANT_RATE_LIMIT", "12"))
ASSISTANT_HISTORY_MESSAGES = 12
