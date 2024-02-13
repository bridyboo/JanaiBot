import pyaudio
import speech_recognition as sr

def transcribe_system_audio():
    recognizer = sr.Recognizer()
    p = pyaudio.PyAudio()

    # Replace this with the appropriate device index
    device_index = 41

    stream = p.open(format=pyaudio.paInt16,
                    channels=8,
                    rate=44100,
                    input=True,
                    input_device_index=device_index,
                    frames_per_buffer=2048)

    try:
        while True:
            audio_data = stream.read(1024)
            audio = sr.AudioData(audio_data, 44100, 2)

            try:
                text = recognizer.recognize_google(audio)
                print("Transcribed: " + text)
            except sr.UnknownValueError:
                print("Audio not understood")
            except sr.RequestError as e:
                print(f"Error: {e}")

    except KeyboardInterrupt:
        print("Stopping transcription")

    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    transcribe_system_audio()
