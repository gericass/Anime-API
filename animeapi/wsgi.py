"""
WSGI config for animeapi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import time
#import api.resident こいつインポートするとバグる
import threading

from django.core.wsgi import get_wsgi_application


def process():
    while True:
        print("LOG!!!!!!!!!!!!!!!!!!!!")
        time.sleep(5)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "animeapi.settings")

application = get_wsgi_application()

t = threading.Thread(target=process)
t.start()



