import sounddevice as sd
import numpy as np
import wave
import tempfile
import faster_whisper

class AudioTranscriber:
    def __init__(self, sample_rate=44100, device_index=36):
        self.sample_rate = sample_rate
        self.device_index = device_index
        self.model = faster_whisper.WhisperModel("large")

    def record_audio(self, duration):
        print("Recording...")
        recording = sd.rec(int(duration * self.sample_rate), samplerate=self.sample_rate, channels=1, dtype='float32', device=self.device_index)
        sd.wait()
        return recording

    def save_audio_to_file(self, audio, file_path):
        with wave.open(file_path, 'wb') as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)  # 16-bit PCM
            wf.setframerate(self.sample_rate)
            wf.writeframes((audio * 32767).astype(np.int16))

    def transcribe_audio(self, file_path):
        result = self.model.transcribe(file_path)
        transcription_segments = result[0]
        transcribed_text = ""

        for segment in transcription_segments:
            transcribed_text += segment.text + " "

        return transcribed_text.strip()

    def ambient_stt(self, duration):
        audio = self.record_audio(duration)
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp_file:
            self.save_audio_to_file(audio, tmp_file.name)
            transcription = self.transcribe_audio(tmp_file.name)
        return transcription


if __name__ == '__main__':
    DURATION = 3  # Duration to record in seconds
    DEVICE_INDEX = 36 # Replace this with the index of your desired device

    transcriber = AudioTranscriber(44100, DEVICE_INDEX)
    print(transcriber.ambient_stt(DURATION))
