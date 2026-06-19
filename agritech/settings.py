# agritech/settings.py

import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url
import cloudinary

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

# SECURITY
SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-change-this"
)

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "localhost,127.0.0.1,agritechproject-2.onrender.com,nursery.technosthan.com"
).split(",")

CSRF_TRUSTED_ORIGINS = [
    "https://agritechproject-2.onrender.com",
    "https://nursery.technosthan.com",
]

# APPLICATIONS
INSTALLED_APPS = [
    "jazzmin",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cloudinary',
    'cloudinary_storage',

    'accounts',
    'core',
    'categories',
    'products',
    'cart',
    'orders',
    'consultations',
    'doctors',
    'gardeners',
    'services',
    'reviews',
    'wishlist',
]

# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'agritech.urls'

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

                'core.context_processors.site_settings',
                'services.context_processors.navbar_services',
             
                'products.context_processors.navbar_categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'agritech.wsgi.application'

# DATABASE
DATABASES = {
    "default": dj_database_url.parse(
        os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}

# CLOUDINARY
CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")
CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")

# Configure cloudinary
if CLOUDINARY_URL:
    cloudinary.config(cloudinary_url=CLOUDINARY_URL)
    DEFAULT_STORAGE_BACKEND = "cloudinary_storage.storage.MediaCloudinaryStorage"
    CLOUDINARY_STORAGE = {}
    # allow cloudinary_storage to pick credentials from CLOUDINARY_URL
    CLOUDINARY_STORAGE.update({
        'CLOUDINARY_URL': CLOUDINARY_URL
    })
    USE_CLOUDINARY = True
elif CLOUDINARY_CLOUD_NAME and CLOUDINARY_API_KEY and CLOUDINARY_API_SECRET:
    cloudinary.config(
        cloud_name=CLOUDINARY_CLOUD_NAME,
        api_key=CLOUDINARY_API_KEY,
        api_secret=CLOUDINARY_API_SECRET,
    )
    DEFAULT_STORAGE_BACKEND = "cloudinary_storage.storage.MediaCloudinaryStorage"
    CLOUDINARY_STORAGE = {
        'CLOUD_NAME': CLOUDINARY_CLOUD_NAME,
        'API_KEY': CLOUDINARY_API_KEY,
        'API_SECRET': CLOUDINARY_API_SECRET,
    }
    USE_CLOUDINARY = True
else:
    # Fallback to local file storage
    DEFAULT_STORAGE_BACKEND = "django.core.files.storage.FileSystemStorage"
    CLOUDINARY_STORAGE = {}
    USE_CLOUDINARY = False

# STORAGES
STORAGES = {
    "default": {
        "BACKEND": DEFAULT_STORAGE_BACKEND,
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# MEDIA
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

# STATIC FILES
STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# EMAIL SETTINGS
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# STATIC AND STORAGE
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
DEFAULT_FILE_STORAGE = DEFAULT_STORAGE_BACKEND

# Security settings for production
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_REFERRER_POLICY = 'no-referrer-when-downgrade'
else:
    # development-friendly defaults
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_SSL_REDIRECT = False

# Trim whitespace from ALLOWED_HOSTS entries
ALLOWED_HOSTS = [h.strip() for h in ALLOWED_HOSTS]


# =====================================
# JAZZMIN SETTINGS
# =====================================

JAZZMIN_SETTINGS = {
    "site_title": "AgriTech Administration",
    "site_header": "AgriTech Administration",
    "site_brand": "AgriTech Administration",
    "welcome_sign": "Welcome to AgriTech Administration",

    # Logo
    "site_logo": "images/logo.png",
    "site_logo_classes": "img-circle",

    # Sidebar
    "show_sidebar": True,
    "navigation_expanded": True,

    # Disable UI Builder
    "show_ui_builder": False,

    # Search Models
    "search_model": [
        "auth.User",
        "products.Product",
        "categories.Category",
        "orders.Order",
        "consultations.Consultation",
    ],

    # Top Menu
    "topmenu_links": [
        {
            "name": "Visit Website",
            "url": "/",
            "new_window": True,
        },
    ],

    # User Menu
    "usermenu_links": [
        {
            "name": "Visit Website",
            "url": "/",
            "new_window": True,
        },
    ],

    # Icons
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.group": "fas fa-users",

        "products.Product": "fas fa-seedling",
        "categories.Category": "fas fa-list",
        "orders.Order": "fas fa-shopping-cart",
        "consultations.Consultation": "fas fa-stethoscope",
        "doctors.Doctor": "fas fa-user-md",
        "gardeners.Gardener": "fas fa-leaf",
        "reviews.Review": "fas fa-star",
        "wishlist.Wishlist": "fas fa-heart",
    },

    # Remove extra links
    "show_ui_builder": False,

    # Theme
    "theme": "darkly",
}