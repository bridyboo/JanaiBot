# JanaiBot LLM 
- this is an OpenAI based LLM chatbot called JanaiBot, I updated it and compiled it with a more stable version of python
- now using python 3.11 instead of 3.12, JanaiBot is a LLM-based "idol" using Speech recognition and Neural TTS Janai is brought to life 
- as a very responsive and interactive chatbot. It can react to your microphone inputs, media background and Twitch Chat!

## Video Example of JanaiBot:
<a href="https://www.youtube.com/watch?v=vLVMcHfOAlI" target="_blank"><img src="https://i.imgur.com/bxD8SE9.jpeg" title="UmimiJanai chatbot" /></a>

## Technical Scope
Leveraging openAI's LLM API, using the API's json config to create a unique 1 of 1 personality 'Janai'
Implementing speech recognition using faster_whisper, very accurate and realtime transcription work very-inspired/based off https://github.com/KoljaB 
JanaiBot's voice is powered with AzureAI speech's Neural Text-to-Speech (NTTS)

### JanaiBot
This project is technically 3 implementations of JanaiBot:

- JanaiBot can listen to ambient content: 
  1. so it will listen, and respond to content from my computer (games, songs, podcasts)
  2. using sounddevice library to record background audio and interfacing it with faster_whisper for it to be transcribed for JanaiBot

- JanaiBot listening to Microphone:
  1. listens and responds to my microphone and ignores every other source of audio. 

- Janaibot reacts to Twitch Chat:
  1. Utilizing the Twitch REST API to parse Live viewer comments
  2. JanaiBot collects chat history locally and will have persistent memory of previous interactions, makes for a 'human-like interaction'

 