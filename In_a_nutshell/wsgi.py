"""
WSGI config for In_a_nutshell project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
print("wsgi file before importing anything")
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "In_a_nutshell.settings")

application = get_wsgi_application()
