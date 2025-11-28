from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ws*l8ez%xqw46__u0tx7hv-$*n2&_x_m%%xa=2f5mw95ifz0w%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app',
]

MIDDLEWARE = [
    # CSP Middleware added at top for security
    # Enforces Content Security Policy to reduce XSS risks
    'csp.middleware.CSPMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    # Built-in CSRF middleware (protects against cross-site request forgery)
    'django.middleware.csrf.CsrfViewMiddleware',

    # Handles authentication and ensures session integrity
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    # Protects against clickjacking attacks
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Custom User Model
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------
# Security Settings 
# -----------------------------
SECURE_BROWSER_XSS_FILTER = True          # Enables basic XSS protection in browsers
X_FRAME_OPTIONS = 'DENY'                  # Prevents clickjacking by disabling iframe embedding
SECURE_CONTENT_TYPE_NOSNIFF = True        # Prevents MIME-type sniffing
CSRF_COOKIE_SECURE = True                 # Ensures CSRF cookie only sent over HTTPS
SESSION_COOKIE_SECURE = True              # Ensures session cookie only sent over HTTPS

# -----------------------------
# Content Security Policy 
# Restricts sources for scripts, styles, images, etc.
# Helps mitigate XSS by preventing loading untrusted content
# -----------------------------
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "https://trusted-cdn.com")
CSP_STYLE_SRC = ("'self'", "https://fonts.googleapis.com")

# Using Django ORM to avoid SQL injection by parameterizing queries
# CSRF protection automatically applied through Django middleware and form templates
# CSP enforced globally via django-csp to mitigate XSS attacks
