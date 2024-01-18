import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Say something:")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                print("You said:", text)

                # Exit the loop if the recognized text is 'end program'
                if text.lower() == 'end program':
                    print("Ending the program.")
                    break

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    speech_to_text()
