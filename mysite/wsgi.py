"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""


import os

from mongoengine import connect

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# Kết nối tới MongoDB
connect(host='mongodb+srv://nguyennhan2682007:uhxmCzqNWZcpWUgZ@cluster0.cjwkw2x.mongodb.net/')

application = get_wsgi_application()

app = application
