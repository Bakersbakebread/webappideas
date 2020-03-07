from webappideas.settings.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["localhost"]

SECRET_KEY = os.getenv("SECRET_KEY")