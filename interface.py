from JanaiBot import chatbot
from speech2 import AudioToTextRecorder
from multiprocessing import Manager, freeze_support
import TTS

janai = chatbot.ChatBot()
chatting = True

def process_text(text):
	print(text)


if __name__ == '__main__':
	# Ensure freeze_support is called on Windows
	freeze_support
	recorder = AudioToTextRecorder()
	while chatting:
		question = recorder.text()

		print("User:", question)

		bot_response = janai.queryBot(question)
		TTS.textToSpeech(bot_response)
		print("Janai:", bot_response)

		if 'close program' in question.lower():
			chatting = False

	# shutdown the recorder
	recorder.shutdown()

