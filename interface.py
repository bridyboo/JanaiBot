from JanaiBot import chatbot
import speech

janai = chatbot.ChatBot()
chatting = True

while (chatting):
	question = speech.speech_to_text()
	print("User:", question)

	bot_response = janai.queryBot(question)
	print("Janai:", bot_response)

	if 'end program' in question.lower():
		break

