from gtts import gTTS
from pydub import AudioSegment
import pygame
import os

def textToSpeech(textspeech):
    # Text you want to convert to speech
    text = textspeech

    # Language code (e.g., English)
    language = 'en'

    # Output file names
    original_filename = "output_speed.mp3"
    adjusted_filename = "output_adjusted_speed.mp3"

    # Remove the old output files if they exist
    for filename in [original_filename, adjusted_filename]:
        if os.path.exists(filename):
            os.remove(filename)

    # Passing the text and language to the engine
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the generated original audio file
    tts.save(original_filename)

    # Load the original audio file
    audio = AudioSegment.from_file(original_filename, format="mp3")

    # Adjust the speed (a value greater than 1 increases speed, less than 1 decreases speed)
    adjusted_audio = audio.speedup(playback_speed=1.4)  # Adjust as needed

    # Increase the pitch by setting a higher frame rate
    increased_pitch_audio = adjusted_audio.set_frame_rate(int(adjusted_audio.frame_rate * 1.25))  # Adjust as needed

    # Save the adjusted audio
    increased_pitch_audio.export(adjusted_filename, format="mp3")

    # Use pygame to play the adjusted audio
    pygame.mixer.init()
    pygame.mixer.music.load(adjusted_filename)
    pygame.mixer.music.play()

    # Keep the program running until the audio finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    # Stop playback and close the audio file
    pygame.mixer.music.stop()
    pygame.mixer.quit()

    # Remove both output files after playing the audio
    for filename in [original_filename, adjusted_filename]:
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == "__main__":
    while True:
        textToSpeech("oh umimi .i'm just a cute streamer girl!")
