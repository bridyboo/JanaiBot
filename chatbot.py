import os
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()
# Retrieve the API key from the environment variables
OPENAI_API_KEY = os.environ.get("api_key2")
file_path = 'context.json'


class ChatBot:

	def __init__(self):
		# Set the API key in the OpenAI client
		self.client = OpenAI(api_key=OPENAI_API_KEY)
		self.messages = []

		# Initialize the chatbots' "messages" context
		try:
			with open(file_path, 'r') as file:
				role_system_content = json.load(file)

			# Extract the content string from the role system content
			system_content_string = json.dumps(role_system_content)

			# Add the role system content to the chatbot's messages
			self.messages.append({"role": "system", "content": system_content_string})

		except FileNotFoundError:
			print(f"Error: File '{file_path}' not found.")
		except json.JSONDecodeError as json_error:
			print(f"Error decoding JSON file: {json_error}")
		except Exception as e:
			print(f"Error reading file: {e}")

	def queryBot(self, question):
		# Create a new list for each query, including existing messages
		current_messages = self.messages.copy()
		current_messages.append({"role": "user", "content": question})

		try:
			completion = self.client.chat.completions.create(
				model="gpt-3.5-turbo-1106",
				messages=current_messages,
				max_tokens=70  # this alters the max amount of tokens usable in a single response
			)

			# Extract and return the bot's reply
			bot_reply = completion.choices[0].message.content

			# Add bot's reply to the conversation
			current_messages.append({"role": "assistant", "content": bot_reply})
			self.messages = current_messages  # Update messages for the next query

			return bot_reply

		except Exception as e:
			print(f"Error during API call: {e}")
			return "An error occurred during the conversation."
