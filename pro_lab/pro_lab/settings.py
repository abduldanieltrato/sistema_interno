from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-hz5w8t1etg%=sb!_q_&$9o%qktvu0(%zt(64=+00)$x*)t3f+)"

# DEBUG = True
DEBUG = False
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "192.168.69.55"]

INSTALLED_APPS = [
        "django_countries",
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "app_lab",
        ]

MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        ]

# Configuração de logout automático após 30 minutos de inatividade
SESSION_COOKIE_AGE = 1800  # 30 minutos
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Expira quando o navegador é fechado

SESSION_ENGINE = "django.contrib.sessions.backends.db"

ROOT_URLCONF = "pro_lab.urls"

TEMPLATES = [
        {
                "BACKEND" : "django.template.backends.django.DjangoTemplates",
                "DIRS"    : [
                        BASE_DIR / "templates",  # Diretório global de templates
                        ],
                "APP_DIRS": True,
                "OPTIONS" : {
                        "context_processors": [
                                "django.template.context_processors.debug",
                                "django.template.context_processors.request",
                                "django.contrib.auth.context_processors.auth",
                                "django.contrib.messages.context_processors.messages",
                                ],
                        },
                },
        ]

WSGI_APPLICATION = "pro_lab.wsgi.application"

DATABASES = {
        "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME"  : BASE_DIR / "base_lab.sqlite3",
                }
        }

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

LANGUAGE_CODE = "pt"

TIME_ZONE = "Africa/Maputo"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "app_lab.Usuario"

STATIC_ROOT = BASE_DIR / "staticfiles"

LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"  # Redireciona após login
LOGOUT_REDIRECT_URL = "/logout/"  # Redireciona após logout
