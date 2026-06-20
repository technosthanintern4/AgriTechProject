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

ALLOWED_HOSTS = [
    host.strip()
    for host in os.getenv(
        "ALLOWED_HOSTS",
        "localhost,127.0.0.1,agritechproject-2.onrender.com,nursery.technosthan.com"
    ).split(",")
    if host.strip()
]

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv(
        "CSRF_TRUSTED_ORIGINS",
        "https://agritechproject-2.onrender.com,https://nursery.technosthan.com"
    ).split(",")
    if origin.strip()
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
    'dashboard',
    'cms',
]

# Use custom user model from accounts app
AUTH_USER_MODEL = 'accounts.User'

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
                'accounts.context_processors.user_context',
                'accounts.context_processors.dashboard_context',
                'cms.context_processors.cms_globals',
            ],
        },
    },
]

WSGI_APPLICATION = 'agritech.wsgi.application'

# DATABASE
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=600,
            ssl_require=not DEBUG
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
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
        "BACKEND": os.getenv(
            "STATICFILES_STORAGE_BACKEND",
            "whitenoise.storage.CompressedStaticFilesStorage"
        ),
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
STATICFILES_STORAGE = STORAGES["staticfiles"]["BACKEND"]
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

# =====================================
# JAZZMIN SETTINGS
# =====================================

JAZZMIN_SETTINGS = {
    "site_title": "AgroSthan Admin",
    "site_header": "AgroSthan",
    "site_brand": "AgroSthan",
    "welcome_sign": "Welcome to AgroSthan Command Center",
    "copyright": "AgroSthan",

    # Logo
    "site_logo": "images/logo.png",
    "login_logo": "images/logo.png",
    "login_logo_dark": "images/logo.png",
    "site_logo_classes": "brand-image elevation-1",
    "site_icon": "images/logo.png",

    # Sidebar
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],

    # Disable UI Builder
    "show_ui_builder": False,

    # Search Models
    "search_model": [
        "accounts.User",
        "products.Product",
        "categories.Category",
        "orders.Order",
        "consultations.Consultation",
        "doctors.Doctor",
        "cms.Blog",
        "cms.Employee",
        "cms.Task",
    ],

    # Top Menu
    "topmenu_links": [
        {
            "name": "Visit Website",
            "url": "/",
            "new_window": True,
        },
        {
            "model": "accounts.User",
        },
        {
            "app": "cms",
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
        "auth": "fas fa-shield-alt",
        "auth.Group": "fas fa-users-cog",
        "auth.group": "fas fa-users-cog",
        "accounts": "fas fa-users",
        "accounts.User": "fas fa-user",
        "accounts.UserProfile": "fas fa-address-card",
        "accounts.AdminRegistrationCode": "fas fa-key",

        "categories": "fas fa-layer-group",
        "categories.Category": "fas fa-sitemap",
        "products": "fas fa-seedling",
        "products.Product": "fas fa-seedling",
        "products.ProductCategory": "fas fa-tags",
        "products.ProductImage": "fas fa-images",
        "products.ProductVariant": "fas fa-boxes",
        "services": "fas fa-concierge-bell",
        "services.Service": "fas fa-hands-helping",
        "services.ServiceCategory": "fas fa-stream",
        "categories.Category": "fas fa-list",
        "orders": "fas fa-receipt",
        "orders.Order": "fas fa-shopping-cart",
        "orders.OrderItem": "fas fa-box",
        "cart": "fas fa-cart-plus",
        "cart.Cart": "fas fa-cart-plus",
        "consultations.Consultation": "fas fa-stethoscope",
        "consultations.NotificationLog": "fas fa-bell",
        "doctors": "fas fa-user-md",
        "doctors.Doctor": "fas fa-user-md",
        "doctors.DoctorCategory": "fas fa-notes-medical",
        "doctors.DoctorAvailability": "fas fa-calendar-alt",
        "gardeners": "fas fa-leaf",
        "gardeners.Gardener": "fas fa-leaf",
        "gardeners.GardenerBooking": "fas fa-calendar-check",
        "reviews": "fas fa-star-half-alt",
        "reviews.Review": "fas fa-star",
        "wishlist": "fas fa-heart",
        "wishlist.Wishlist": "fas fa-heart",
        "cms": "fas fa-briefcase",
        "cms.WebsiteSettings": "fas fa-cogs",
        "cms.MenuItem": "fas fa-bars",
        "cms.HomePageContent": "fas fa-home",
        "cms.FooterContent": "fas fa-shoe-prints",
        "cms.Blog": "fas fa-blog",
        "cms.MediaAsset": "fas fa-photo-video",
        "cms.Employee": "fas fa-id-badge",
        "cms.Attendance": "fas fa-calendar-check",
        "cms.Task": "fas fa-tasks",
        "cms.Department": "fas fa-building",
        "cms.Designation": "fas fa-user-tie",
        "cms.TaskComment": "fas fa-comments",
        "cms.TaskAttachment": "fas fa-paperclip",
        "cms.CMSPage": "fas fa-file-alt",
        "cms.DynamicSection": "fas fa-th-large",
        "cms.BlogCategory": "fas fa-folder-open",
        "cms.Tag": "fas fa-tag",
        "cms.CMSPage": "fas fa-file-alt",
        "cms.Report": "fas fa-chart-line",
    },

    # Navigation order: ERP-style flow without changing apps, models, or permissions.
    "order_with_respect_to": [
        "cms.WebsiteSettings",
        "cms.MenuItem",
        "cms.HomePageContent",
        "cms.FooterContent",
        "cms.CMSPage",
        "cms.DynamicSection",
        "cms.BlogCategory",
        "cms.Blog",
        "cms.Tag",
        "cms.MediaAsset",
        "products.ProductCategory",
        "products.Product",
        "products.ProductImage",
        "products.ProductVariant",
        "services.ServiceCategory",
        "services.Service",
        "accounts.User",
        "accounts.UserProfile",
        "orders.Order",
        "orders.OrderItem",
        "consultations.Consultation",
        "consultations.NotificationLog",
        "doctors.DoctorCategory",
        "doctors.Doctor",
        "doctors.DoctorAvailability",
        "gardeners.Gardener",
        "gardeners.GardenerBooking",
        "cms.Department",
        "cms.Designation",
        "cms.Employee",
        "cms.Attendance",
        "cms.Task",
        "cms.Report",
        "auth.Group",
        "accounts.AdminRegistrationCode",
    ],

    # Remove extra links
    "show_ui_builder": False,

    # Theme
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "custom_css": "css/admin-premium.css",
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-success",
    "accent": "accent-success",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": True,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-success",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    "button_classes": {
        "primary": "btn-success",
        "secondary": "btn-outline-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
    "actions_sticky_top": True,
}
