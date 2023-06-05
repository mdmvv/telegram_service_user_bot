from configparser import ConfigParser

from pyrogram import Client

from handlers import command_create_group_handler
from handlers import command_add_members_handler
from handlers import command_ban_members_handler
from handlers import command_send_bulk_message_handler
from handlers import private_message_handler
from handlers import group_message_handler
from handlers import channel_message_handler


config = ConfigParser()
config.read('config.ini')

api_id = config.get('Telegram', 'api_id')
api_hash = config.get('Telegram', 'api_hash')

app = Client('bot', api_id, api_hash)

app.add_handler(command_create_group_handler)
app.add_handler(command_add_members_handler)
app.add_handler(command_ban_members_handler)
app.add_handler(command_send_bulk_message_handler)
app.add_handler(private_message_handler)
app.add_handler(group_message_handler)
app.add_handler(channel_message_handler)


if __name__ == '__main__':
    app.run()
