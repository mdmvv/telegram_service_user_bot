from configparser import ConfigParser
import time
from pyrogram.errors import ChatWriteForbidden
from pyrogram.errors import UserNotParticipant
from pyrogram.errors import PeerIdInvalid
import bulk_message


async def create_group(client, group_name, user_ids):
    """
    Creates a group with the specified name and user IDs.
    """
    try:
        chat = await client.create_group(
            title=group_name,
            users=user_ids
        )
        print(f"Group created with ID: {chat.id}")
        time.sleep(5)
        return chat.id
    except Exception as e:
        print(f"Failed to create group. Error: {e}")
        return None


async def add_members_to_group(client, chat_id, user_ids):
    """
    Adds members to a group with the specified chat ID.
    """
    for user_id in user_ids:
        try:
            await client.add_chat_members(chat_id, user_id)
            print(f"Added member {user_id} to group {chat_id}")
            time.sleep(1)
        except PeerIdInvalid:
            print(f"User {user_id} not found")
        except UserNotParticipant:
            print(f"Bot is not a member of group {chat_id}")
        except ChatWriteForbidden:
            print(f"Cannot send messages to group {chat_id}")
        except Exception as e:
            print(f"Failed to add members to group {chat_id}. Error: {e}")


async def ban_group_members(client, chat_id, user_ids):
    """
    Bans members from a group with the specified chat ID.
    """
    for user_id in user_ids:
        try:
            await client.ban_chat_member(chat_id, user_id)
            print(f"Banned member {user_id} in group {chat_id}")
            time.sleep(2)
        except PeerIdInvalid:
            print(f"User {user_id} not found")
        except UserNotParticipant:
            print(f"Bot is not a member of group {chat_id}")
        except ChatWriteForbidden:
            print(f"Cannot send messages to group {chat_id}")
        except Exception as e:
            print(f"Failed to ban members from group {chat_id}. Error: {e}")


async def send_bulk_message(client):
    """
    Sends a bulk message to users
    """
    bulk_message_config = ConfigParser()
    bulk_message_config.read('Bulk Message/config.ini')

    bulk_message_id = int(bulk_message_config.get('Parameters', 'bulk_message_id'))
    session_max = int(bulk_message_config.get('Parameters', 'session_max'))

    await bulk_message.send_bulk_message(client, bulk_message_id, session_max)
