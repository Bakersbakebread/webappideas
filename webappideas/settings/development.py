from webappideas.settings.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

SECRET_KEY = os.getenv("SECRET_KEY")
