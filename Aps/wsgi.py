"""
WSGI config for Aps project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
import threading

from django.core.wsgi import get_wsgi_application

from aps_api.signals.method_generator import daily_code

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Aps.settings')
application = get_wsgi_application()

import asyncio


def start_background_tasks():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(daily_code())
    loop.run_forever()


threading.Thread(target=start_background_tasks, daemon=True).start()
