from configparser import ConfigParser
import openai
from openai.error import APIError


class ChatbotEngine:
    def __init__(self):
        config = ConfigParser()
        config.read('config.ini')

        openai.api_key = config.get('OpenAI', 'api_key')

    def generate_response(self, prompt, context=''):
        try:
            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[
                    {'role': 'system', 'content': context},
                    {'role': 'user', 'content': prompt}
                ]
            )
            return response.choices[0].message['content'].strip()
        except APIError:
            print("Error")


chatbot_engine = ChatbotEngine()
