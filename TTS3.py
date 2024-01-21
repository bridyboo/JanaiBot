import requests
import os
from xml.etree import ElementTree
from pydub import AudioSegment
from pydub.playback import play

# Set up the keys and endpoint
subscription_key = "5ba1c5a4c1b6443ab327c9f8982492f8"
tts_endpoint = "https://westus.tts.speech.microsoft.com/cognitiveservices/v1"

def text_to_speech(text, file_name="output.wav"):
    # Set the headers
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
        "User-Agent": "Python-requests"
    }

    # Construct the SSML request
    xml_body = ElementTree.Element('speak', version='1.0')
    xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
    voice = ElementTree.SubElement(xml_body, 'voice')
    voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
    voice.set('{http://www.w3.org/XML/1998/namespace}gender', 'Female')
    voice.set('name', 'en-US-AriaNeural')  # You can change the voice here

    # Add prosody for pitch and rate
    prosody = ElementTree.SubElement(voice, 'prosody')
    prosody.set('pitch', '+15%')  # Increase pitch by 10%
    prosody.set('rate', '+10%')  # Increase speed; you can also use percentages

    prosody.text = text

    # Convert to string
    body = ElementTree.tostring(xml_body)

    # Send the request
    response = requests.post(tts_endpoint, headers=headers, data=body)

    # Check for a successful response
    if response.status_code == 200:
        with open(file_name, "wb") as audio:
            audio.write(response.content)

        # Play the audio using pydub
        audio = AudioSegment.from_wav(file_name)
        play(audio)

        # Delete the file after playback
        os.remove(file_name)
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == '__main__':
    # Example usage
    text_to_speech("Hello! ooh-mimi ja-nye here! how's your day?")
