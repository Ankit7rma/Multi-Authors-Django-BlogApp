import os

from src.settings import BASE_DIR

SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
