from gtts import gTTS
from pydub import AudioSegment
import pygame


def textToSpeech(textspeech):
    # Text you want to convert to speech
    text = textspeech

    # Language code (e.g., English)
    language = 'en'

    # Passing the text and language to the engine
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the generated audio file
    tts.save("output_speed.mp3")

    # Load the audio file
    audio = AudioSegment.from_file("output_speed.mp3", format="mp3")

    # Adjust the speed (a value greater than 1 increases speed, less than 1 decreases speed)
    adjusted_audio = audio.speedup(playback_speed=1.4)  # Adjust as needed

    # Increase the pitch by setting a higher frame rate
    increased_pitch_audio = adjusted_audio.set_frame_rate(int(adjusted_audio.frame_rate * 1.25))  # Adjust as needed

    # Save the adjusted audio
    increased_pitch_audio.export("output_adjusted_speed.mp3", format="mp3")

    # Use pygame to play the adjusted audio
    pygame.mixer.init()
    pygame.mixer.music.load("output_adjusted_speed.mp3")
    pygame.mixer.music.play()

    # Keep the program running until the audio finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

if __name__ == "__main__":
    textToSpeech("they're testing on rats in china")