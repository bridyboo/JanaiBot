import os
from twitchio.ext import commands
from dotenv import load_dotenv

env_path = r"C:\Users\matth\PycharmProjects\ChatBotLLMJanai\JanaiBot\.env"
load_dotenv(dotenv_path=env_path)

twitch_access_token = os.environ.get("twitch_oauth_token")

class Bot(commands.Bot):

	def __init__(self):
		super().__init__(token=twitch_access_token, prefix='!', initial_channels=['channel'])

	async def event_ready(self):
		print(f'Logged in as | {self.nick}')

	async def event_message(self, message):
		print(f'Message from {message.author.name}: {message.content}')
		await self.handle_commands(message)


bot = Bot()
bot.run()
