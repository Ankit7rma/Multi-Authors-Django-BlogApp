import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']  # Configure this based on your Render URL

# Add this for handling static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Add whitenoise middleware
MIDDLEWARE = [
    # ...other middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ...
]

# Database configuration for Render
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
    }
}

# Update database configuration from DATABASE_URL
import dj_database_url # type: ignore
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)