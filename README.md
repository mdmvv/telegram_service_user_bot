# Telegram User bot for service needs

Telegram user bot, including a set of functions for the needs of the service.

Built using the `Pyrogram`, `PyMySQL` and `OpenAI`

## Functional
- Parsing messages from personal messages, groups and channels by keywords
- Group management functions using commands - create a group, add users, delete users
- Sending a bulk message to the user database
- Chat answering machine model

## Getting Started
1. Clone this repository.
2. Install dependencies with `pip install -r requirements.txt`.
3. Create a database with `database.sql`.
4. Set up your configuration in `config.ini` and settings in `settings.ini`.
5. Set up `bulk_message.txt` and `config.ini` in `Bulk Message` to send bulk message.
6. Write your context in `context.txt` for chat model to work.
7. Run the bot using `main.py`.

Administration commands: `/create_group <Group name> <User IDs>`, `/add_members <Group ID> <User IDs>`, `/ban_members <Group ID> <User IDs>`, `/send_bulk_message`.
