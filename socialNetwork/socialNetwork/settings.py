from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-vnoh_k7z4%xutnzu#mdjv23843d#dq$h-tc++y&!f^vdw1u%24"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]




INSTALLED_APPS = [
    # Application definition
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",

    # These are apps    
    "friends.apps.FriendsConfig",

    "logAndReg.apps.LogandregConfig",

    "commentPost.apps.CommentpostConfig",

    "postsUsers.apps.PostsusersConfig",

    "chat.apps.ChatConfig",

    "postsSort.apps.PostssortConfig",

    # Тhese are for the swagge
    "crispy_forms",
    "drf_yasg",

    # Тhese are for the google account
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
]

SWAGGER_SETTINGS = {
    'DEFAULT_INFO': 'chat_app.urls.openapi_info',
    'SECURITY_DEFINITIONS': {},
    'VALIDATOR_URL': None,
}

AUTHENTICATION_BACKENDS = (
    # used for default signin such as loggin into admin panel
    "django.contrib.auth.backends.ModelBackend",

    # used for social authentications
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

LOGIN_REDIRECT_URL ="" 

CRISPY_TEMPLATE_PACK = "bootstrap4"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "socialNetwork.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "/Users/serojisahakyan/Desktop/social-network/socialNetwork/templates"
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "socialNetwork.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

SOCIALACCOUNT_PROVIDERS = {
    "googl": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

APPEND_SLASH = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
env = environ.Env()
environ.Env.read_env()

# GMAIL_API_CREDENTIALS = env("GMAIL_API_CREDENTIALS")
# GMAIL_API_TOKEN = env("GMAIL_API_TOKEN")
# GMAIL_API_SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
STATIC_ROOT = os.path.join (BASE_DIR, 'socialNetwork/static')
# MEDIA_URL = '/static/'