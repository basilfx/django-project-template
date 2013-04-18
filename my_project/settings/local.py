from . import *

#
# YOU DO NOT WANT THIS FILE TO APPEAR IN YOUR VCS!
#

# Default settings, overrides generic.py
DEBUG                   = True
TEMPLATE_DEBUG          = True 

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': ''
    }
}
