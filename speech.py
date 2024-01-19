import speech_recognition as sr


def speech_to_text():
	recognizer = sr.Recognizer()
	mic = sr.Microphone(device_index=1)  # specific microphone

	while True:
		with mic as source:
			print("Say something:")
			recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
			audio = recognizer.listen(source)

			try:
				text = recognizer.recognize_google(audio)
				return text  # Return text if successful

			except sr.UnknownValueError:
				print("Could not understand audio")
			except sr.RequestError as e:
				print(f"Could not request results from Google Speech Recognition service; {e}")


if __name__ == "__main__":
	print(speech_to_text())
