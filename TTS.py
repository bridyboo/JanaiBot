from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
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

    # Play the adjusted audio using pydub
    play(increased_pitch_audio)

    # Remove both output files after playing the audio
    for filename in [original_filename, adjusted_filename]:
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == "__main__":
    while True:
        textToSpeech("oh umimi .i'm just a cute streamer girl!")
