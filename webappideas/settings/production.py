from webappideas.settings.common import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS")

SECRET_KEY = os.getenv("SECRET_KEY")
