# Custom settings for production environment

from .base import *

DEBUG = False

ADMINS = [
    ("Django Admin", "email@mydomain.com"),
]

ALLOWED_HOSTS = ["*"]

DATABASES = {"default": {}}
