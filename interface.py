from JanaiBot import chatbot
import speech
import TTS

janai = chatbot.ChatBot()
chatting = True

while (chatting):
	question = speech.speech_to_text()
	print("User:", question)

	bot_response = janai.queryBot(question)
	TTS.textToSpeech(bot_response)
	print("Janai:", bot_response)

	if 'end program' in question.lower():
		break

