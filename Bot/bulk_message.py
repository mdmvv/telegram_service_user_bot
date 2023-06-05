import re
import random
import itertools
import time
from pyrogram.errors import PeerIdInvalid
from database import bot_database


def spintax(text, single=True):
    pattern = re.compile('(\{[^\}]+\}|[^\{\}]*)')
    chunks = pattern.split(text)

    def options(s):
        if len(s) > 0 and s[0] == '{':
            return [opt for opt in s[1:-1].split('|')]
        return [s]

    parts_list = [options(chunk) for chunk in chunks]

    spins = []

    for spin in itertools.product(*parts_list):
        spins.append(''.join(spin))

    if single:
        return spins[random.randint(0, len(spins) - 1)]
    else:
        return spins


async def send_message(client, user_id, text):
    try:
        await client.send_message(chat_id=user_id, text=text)
    except PeerIdInvalid:
        username = bot_database.get_username(user_id)
        if username:
            await client.send_message(chat_id=username, text=text)


async def send_bulk_message(client, bulk_message_id, session_max):
    with open('Bulk Message/bulk_message.txt', 'r', encoding='utf-8') as file:
        message = file.read()

    user_ids = bot_database.get_all_user_ids()

    print(f"Bulk message id{bulk_message_id}")

    iteration = 0
    for user_id in user_ids:
        if bulk_message_id not in bot_database.get_sent_bulk_messages(user_id):
            await send_message(client, user_id, spintax(message))
            bot_database.add_sent_bulk_message(user_id, bulk_message_id)
            print(f"Sent to user {user_id}")

            iteration += 1
            if iteration >= session_max:
                break

            time.sleep(2)
