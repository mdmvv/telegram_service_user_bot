from configparser import ConfigParser
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
import utils
from chatbot_engine import chatbot_engine
from chat_parser import parser


async def handle_command_create_group(client: Client, message: Message):
    """
    Handles the command to create a group with the specified name and user IDs.
    /create_group <Group name> <User IDs>
    """
    group_name = message.command[1]
    user_ids = [int(user_id) for user_id in message.command[2:]]
    await utils.create_group(client, group_name, user_ids)


async def handle_command_add_members(client: Client, message: Message):
    """
    Handles the command to add members to a group with the specified chat ID and user IDs.
    /add_members <Group ID> <User IDs>
    """
    chat_id = int(message.command[1])
    user_ids = [int(user_id) for user_id in message.command[2:]]
    await utils.add_members_to_group(client, chat_id, user_ids)


async def handle_command_ban_members(client: Client, message: Message):
    """
    Handles the command to ban members from a group with the specified chat ID and user IDs.
    /ban_members <Group ID> <User IDs>
    """
    chat_id = int(message.command[1])
    user_ids = [int(user_id) for user_id in message.command[2:]]
    await utils.ban_group_members(client, chat_id, user_ids)


async def handle_command_send_bulk_message(client: Client, message: Message):
    """
    Handles the command to send a bulk message.
    /send_bulk_message
    """
    await utils.send_bulk_message(client)


async def handle_private_message(client: Client, message: Message):
    """
    Handles private messages received by the bot. It generates a response using a chatbot engine and sends it back to
    the user.
    """
    with open('context.txt', 'r', encoding='utf-8') as file:
        context = file.read()

    response = chatbot_engine.generate_response(message.text, context=context)

    if response:
        await client.send_message(chat_id=message.chat.id, text=response)
    else:
        await client.send_message(chat_id=message.chat.id, text="Помилка. Повторіть пізніше.")

    await parser.parse_private_message(message)


async def handle_group_message(client: Client, message: Message):
    """
    Handles group messages received by the bot. It parses the group message using a parser.
    """
    await parser.parse_group_message(message)


async def handle_channel_message(client: Client, message: Message):
    """
    Handles channel messages received by the bot. It parses the channel message using a parser.
    """
    await parser.parse_channel_message(message)


settings = ConfigParser()
settings.read('settings.ini')

admin = int(settings.get('Administration', 'admin_user_id'))


command_create_group_handler = MessageHandler(
    handle_command_create_group,
    filters=(filters.user(admin) & filters.command('create_group'))
)
command_add_members_handler = MessageHandler(
    handle_command_add_members,
    filters=(filters.user(admin) & filters.command('add_members'))
)
command_ban_members_handler = MessageHandler(
    handle_command_ban_members,
    filters=(filters.user(admin) & filters.command('ban_members'))
)
command_send_bulk_message_handler = MessageHandler(
    handle_command_send_bulk_message,
    filters=(filters.user(admin) & filters.command('send_bulk_message'))
)
private_message_handler = MessageHandler(handle_private_message, filters=filters.private)
group_message_handler = MessageHandler(handle_group_message, filters=filters.group)
channel_message_handler = MessageHandler(handle_channel_message, filters=filters.channel)
