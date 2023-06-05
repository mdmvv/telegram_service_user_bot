from configparser import ConfigParser
from database import bot_database


class ChatParser:
    def __init__(self, keywords):
        self.keywords = keywords

    async def parse_private_message(self, message):
        if not message.text:
            return

        keywords_in_message = []
        for keyword in self.keywords:
            if keyword in message.text.lower():
                keywords_in_message.append(keyword)

        if keywords_in_message:
            keywords_in_message_str = ', '.join(keywords_in_message)
            print(f"Parsed {message.date} Private {message.from_user.id}")
            bot_database.add_private_message(
                user_id=message.chat.id,
                date=message.date,
                text=message.text,
                keywords=keywords_in_message_str
            )

    async def parse_group_message(self, message):
        if not message.text:
            return

        keywords_in_message = []
        for keyword in self.keywords:
            if keyword in message.text.lower():
                keywords_in_message.append(keyword)

        if keywords_in_message:
            keywords_in_message_str = ', '.join(keywords_in_message)
            print(f"Parsed {message.date} Group {message.chat.id} User {message.from_user.id}")
            bot_database.add_group_message(
                group_id=message.chat.id,
                user_id=message.from_user.id,
                date=message.date,
                text=message.text,
                keywords=keywords_in_message_str
            )

    async def parse_channel_message(self, message):
        if not message.text:
            return

        keywords_in_message = []
        for keyword in self.keywords:
            if keyword in message.text.lower():
                keywords_in_message.append(keyword)

        if keywords_in_message:
            keywords_in_message_str = ', '.join(keywords_in_message)
            print(f"Parsed {message.date} Channel {message.chat.id}")
            bot_database.add_channel_message(
                channel_id=message.chat.id,
                date=message.date,
                text=message.text,
                keywords=keywords_in_message_str
            )


settings = ConfigParser()
settings.read('settings.ini')
keywords = [word.strip() for word in settings.get('Parsing', 'keywords').split(',')]

parser = ChatParser(keywords)
