from JanaiBot import chatbot
from JanaiBot import TTS3
from Addons import read_chat_janai
import time

janai = chatbot.ChatBot()
chatting = True

sample_rate = 44100
DURATION = 5  # Duration to record in seconds
DEVICE_INDEX = 36  # Replace this with the index of your desired device


def process_text(text):
	print(text)


def follow(file):
	file.seek(0, 2)  # Move to the end of the file
	while True:
		line = file.readline()
		if not line:
			time.sleep(0.1)  # Sleep briefly to avoid busy waiting
			continue
		yield line.strip()  # Strip newline characters and yield the line as a string


def replace_words(text):
	text = text.replace("Umimi", "ooh-mimi")
	text = text.replace("Janai", "ja-nye")
	return text


if __name__ == '__main__':
	socket = read_chat_janai.connect_to_twitch()
	while chatting:
		question = read_chat_janai.read_single_message(socket)
		print("responding to: ", question)
		bot_response = janai.queryBot(question)

		modified_enunciation = replace_words(bot_response)
		TTS3.text_to_speech(modified_enunciation)
		print("Janai:", bot_response)
