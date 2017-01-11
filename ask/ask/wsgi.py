"""
WSGI config for ask project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ask.settings")

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, os.path.abspath(os.path.join(PROJECT_ROOT, "..")))
sys.path.append(PROJECT_ROOT)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
