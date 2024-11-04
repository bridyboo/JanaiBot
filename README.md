this is an OpenAI based LLM chatbot called JanaiBot, I updated it and compiled it with a more stable version of python
now using python 3.11 instead of 3.12

* Leveraging openAI's LLM API, using the API's json config to create a unique 1 of 1 personality 'Janai'
* Implementing speech recognition using faster_whisper, very accurate and realtime transcription work very-inspired/based off https://github.com/KoljaB 
* JanaiBot's voice is powered with AzureAI speech's Neural Text-to-Speech (NTTS)

* This project is technically 3 implementations of JanaiBot:
* 1. JanaiBot can listen to ambient content: 
1. so it will listen, and respond to content from my computer (games, songs, podcasts)
2. it will not listen to my microphone

* 2. JanaiBot listening to Microphone:
1. listens and respond to my microphone and ignores every other source of audio. 

* 3. Janaibot reacts to Twitch Chat:
1. Utilizing the Twitch REST API to parse Live viewer comments
2. JanaiBot collects chat history locally and will have persistent memory of previous interactions, makes for a 'human-like interaction'

 