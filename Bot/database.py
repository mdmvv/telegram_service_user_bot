from configparser import ConfigParser
import pymysql


class BotDatabase:
    def __init__(self, host, user, password, database):
        self.connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def add_private_message(self, user_id, date, text, keywords):
        query = "INSERT INTO private_messages (`user_id`, `date`, `text`, `keywords`) VALUES (%s, %s, %s, %s)"
        values = (user_id, date, text, keywords)
        self.cursor.execute(query, values)
        self.connection.commit()

    def add_group_message(self, group_id, user_id, date, text, keywords):
        query = "INSERT INTO group_messages (`group_id`, `user_id`, `date`, `text`, `keywords`) VALUES (%s, %s, %s, %s, %s)"
        values = (group_id, user_id, date, text, keywords)
        self.cursor.execute(query, values)
        self.connection.commit()

    def add_channel_message(self, channel_id, date, text, keywords):
        query = "INSERT INTO channel_messages (`channel_id`, `date`, `text`, `keywords`) VALUES (%s, %s, %s, %s)"
        values = (channel_id, date, text, keywords)
        self.cursor.execute(query, values)
        self.connection.commit()

    def get_all_user_ids(self):
        query = f"SELECT user_id FROM users"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        ids = [row[0] for row in rows]
        return(ids)

    def get_username(self, user_id):
        query = f"SELECT username FROM users WHERE user_id = {user_id}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        username = rows[0][0]
        return(username)

    def get_sent_bulk_messages(self, user_id):
        query = f"SELECT bulk_message_id FROM sent_bulk_messages WHERE user_id = {user_id}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        ids = [row[0] for row in rows]
        return(ids)

    def add_sent_bulk_message(self, user_id, bulk_message_id):
        query = f"INSERT INTO sent_bulk_messages VALUES ({user_id}, {bulk_message_id})"
        self.cursor.execute(query)
        self.connection.commit()


config = ConfigParser()
config.read('config.ini')

host = config.get('Database', 'host')
user = config.get('Database', 'user')
password = config.get('Database', 'password')
database = config.get('Database', 'database')


bot_database = BotDatabase(host, user, password, database)
