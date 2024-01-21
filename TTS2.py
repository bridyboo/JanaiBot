import os

from elevenlabs import generate, voices, play
from elevenlabs import Voice, VoiceSettings, generate, set_api_key
from dotenv import load_dotenv

load_dotenv()


def text_to_speech(query):
	set_api_key(os.environ.get("elevenlabs_api"))
	# pFZP5JQG7iQjIQuC4Bku 'Lily'
	audio = generate(
		text = query,
		voice=Voice(
			voice_id='pFZP5JQG7iQjIQuC4Bku',
			settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
		)
	)
	play(audio)

if __name__ == '__main__':
	text_to_speech("hello! umimi janai here! how's your day?")