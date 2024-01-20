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
	text_to_speech("Hey, beautiful fam! Welcome back to the stream! 💖 Today, I am super excited to dive into this amazing game that you all have been recommending. I heard the graphics are stunning! By the way, shoutout to our newest subscribers - thank you for joining the family! 🌟 Don't forget to hit that like button and share the stream with your friends. Let's make this chat lively with your questions and comments. Also, huge thanks to our sponsor for making today's stream possible. You guys are the real MVPs! 🙌🏼 I'll be doing a special giveaway later, so stay tuned for that. Grab your snacks, get comfy, and let's have an epic gaming session together! 💕✨")