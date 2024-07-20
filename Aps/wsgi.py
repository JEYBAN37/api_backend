import os
import threading
import asyncio
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Aps.settings')
application = get_wsgi_application()

from aps_api.signals.method_generator import daily_code


def start_background_tasks():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(daily_code())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.close()


threading.Thread(target=start_background_tasks, daemon=True).start()
