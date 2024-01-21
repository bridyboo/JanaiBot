from JanaiBot import chatbot
from speech2 import AudioToTextRecorder
from multiprocessing import Manager, freeze_support
import TTS  # deprecating this one I think
import TTS2
import TTS3

janai = chatbot.ChatBot()
chatting = True


def process_text(text):
	print(text)


def replace_words(text):
	text = text.replace("Umimi", "ooh-mimi")
	text = text.replace("Janai", "ja-nye")
	return text


if __name__ == '__main__':
	# Ensure freeze_support is called on Windows
	freeze_support
	recorder = AudioToTextRecorder()
	while chatting:
		question = recorder.text()
		# question = input("say something: ")
		print("User:", question)

		bot_response = janai.queryBot(question)
		# TTS.textToSpeech(bot_response)
		# TTS2.text_to_speech(bot_response)
		modified_enunciation = replace_words(bot_response)
		TTS3.text_to_speech(modified_enunciation)
		print("Janai:", bot_response)

		if 'close program' in question.lower():
			chatting = False

	# shutdown the recorder
	recorder.shutdown()
