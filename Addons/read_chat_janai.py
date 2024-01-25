import os
import socket
from dotenv import load_dotenv

env_path = r"C:\Users\matth\PycharmProjects\ChatBotLLMJanai\JanaiBot\.env"
load_dotenv(dotenv_path=env_path)

oauth_token = os.environ.get("twitch_oauth_works")

HOST = 'irc.chat.twitch.tv'
PORT = 6667
NICK = 'bridyboo_'
TOKEN = oauth_token   # Prefixed with 'oauth:'
CHANNEL = 'Lil_Majin'

def connect_to_twitch():
    # Initialize socket
    sock = socket.socket()

    # Connect to Twitch IRC
    sock.connect((HOST, PORT))

    # Authenticate
    sock.send(f"PASS {TOKEN}\r\n".encode('utf-8'))
    sock.send(f"NICK {NICK.lower()}\r\n".encode('utf-8'))
    sock.send(f"JOIN #{CHANNEL.lower()}\r\n".encode('utf-8'))

    return sock

def receive_messages(sock):
    while True:
        try:
            response = sock.recv(2048).decode('utf-8')

            if response.startswith('PING'):
                sock.send("PONG :tmi.twitch.tv\r\n".encode('utf-8'))
            else:
                # Parsing the chat message
                if "PRIVMSG" in response:
                    parts = response.split(":", 2)
                    if len(parts) > 2:
                        username = parts[1].split("!", 1)[0]
                        message = parts[2].strip()
                        output_message = f"{username}: {message}\n"

                        # Write the message to a text file
                        with open('chat_log.txt', 'a', encoding='utf-8') as file:
                            file.write(output_message)

                        print(output_message)
        except socket.error as e:
            print(f"Socket error: {e}")
            break

if __name__ == "__main__":
    sock = connect_to_twitch()
    receive_messages(sock)
