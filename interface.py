import chatbot

janai = chatbot.ChatBot()
chatting = True
while(chatting):
	question = input("user: ")
	bot_response = janai.queryBot(question)
	print("Janai:", bot_response)

