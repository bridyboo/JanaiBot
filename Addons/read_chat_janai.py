import os
import socket
from dotenv import load_dotenv

env_path = r"C:\Users\matth\PycharmProjects\ChatBotLLMJanai\JanaiBot\.env"
load_dotenv(dotenv_path=env_path)

oauth_token = os.environ.get("twitch_oauth_works")

HOST = 'irc.chat.twitch.tv'
PORT = 6667
NICK = 'bridyboo_'
TOKEN = oauth_token  # Prefixed with 'oauth:'
CHANNEL = 'PhiDX'


def connect_to_twitch():
	# Initialize socket
	twitch_socket = socket.socket()

	# Connect to Twitch IRC
	twitch_socket.connect((HOST, PORT))

	# Authenticate
	twitch_socket.send(f"PASS {TOKEN}\r\n".encode('utf-8'))
	twitch_socket.send(f"NICK {NICK.lower()}\r\n".encode('utf-8'))
	twitch_socket.send(f"JOIN #{CHANNEL.lower()}\r\n".encode('utf-8'))

	return twitch_socket


def read_single_message(twitch_socket):
	while True:
		try:
			response = twitch_socket.recv(2048).decode('utf-8').strip()

			# Split response into individual messages if batched
			messages = response.split("\r\n")

			for msg in messages:
				if msg.startswith('PING'):
					twitch_socket.send("PONG :tmi.twitch.tv\r\n".encode('utf-8'))
				else:
					# Parsing the chat message
					if "PRIVMSG" in msg:
						parts = msg.split(":", 2)
						if len(parts) > 2:
							username = parts[1].split("!", 1)[0]
							message = parts[2].strip()
							output_message = f"{username} said {message}"
							return output_message  # Returns the first parsed message
		except socket.error as e:
			print(f"Socket error: {e}")
			break

def receive_messages(twitch_socket):
	while True:
		try:
			response = twitch_socket.recv(2048).decode('utf-8')

			if response.startswith('PING'):
				twitch_socket.send("PONG :tmi.twitch.tv\r\n".encode('utf-8'))
			else:
				# Parsing the chat message
				if "PRIVMSG" in response:
					parts = response.split(":", 2)
					if len(parts) > 2:
						username = parts[1].split("!", 1)[0]
						message = parts[2].strip()
						output_message = f"{username} said {message}\n"

						# Write the message to a text file
						with open('chat_log.txt', 'a', encoding='utf-8') as file:
							file.write(output_message)

						print(output_message)
		except socket.error as e:
			print(f"Socket error: {e}")
			break


if __name__ == "__main__":
	sock = connect_to_twitch()
	#receive_messages(sock)
	while True:
		question = read_single_message(sock)
		print(question)