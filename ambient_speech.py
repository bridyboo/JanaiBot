import sounddevice as sd
import numpy as np
import wave
import tempfile
import faster_whisper


def record_audio(duration, sample_rate=44100, device_index=30):
	print("Recording...")
	recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='float32',
					   device=device_index)
	sd.wait()
	return recording


def save_audio_to_file(audio, sample_rate, channels, file_path):
	with wave.open(file_path, 'wb') as wf:
		wf.setnchannels(channels)
		wf.setsampwidth(2)  # 16-bit PCM
		wf.setframerate(sample_rate)
		wf.writeframes((audio * 32767).astype(np.int16))


def transcribe_audio(file_path):
	model = faster_whisper.WhisperModel("large")
	result = model.transcribe(file_path)

	transcription_segments = result[0]
	transcribed_text = ""

	for segment in transcription_segments:
		# Access the text attribute of the Segment object
		transcribed_text += segment.text + " "

	return transcribed_text.strip()


def ambientSTT(duration, sample_rate, device_index):
	audio = record_audio(duration, sample_rate, device_index)
	with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp_file:
		save_audio_to_file(audio, 44100, 1, tmp_file.name)
		transcription = transcribe_audio(tmp_file.name)
	return transcription


if __name__ == '__main__':
	DURATION = 7  # Duration to record in seconds
	DEVICE_INDEX = 36 # Replace this with the index of your desired device

	print(ambientSTT(DURATION,44100, DEVICE_INDEX))
