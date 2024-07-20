import asyncio
import string
import secrets

KeysRamdom = []


async def daily_code():
    KeysRamdom.clear()
    for i in range(100):
        alphabet = string.ascii_letters + string.digits
        KeysRamdom.append(''.join(secrets.choice(alphabet) for i in range(5)).upper())
    await asyncio.sleep(86400)
