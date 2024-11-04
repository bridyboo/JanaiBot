import requests
import os
from dotenv import load_dotenv
from xml.etree import ElementTree
from pydub import AudioSegment
import simpleaudio as sa

# dotenv
env_path = r"C:\Users\matth\PycharmProjects\ChatBotLLMJanai\JanaiBot\.env"
load_dotenv(dotenv_path=env_path)
sub_key = os.environ.get("azuretts_api")

# Set up the keys and endpoint
subscription_key = sub_key
tts_endpoint = "https://eastus.tts.speech.microsoft.com/cognitiveservices/v1"

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
    voice.set('name', 'en-US-NancyNeural')  # You can change the voice here

    # Add prosody for pitch and rate
    prosody = ElementTree.SubElement(voice, 'prosody')
    prosody.set('pitch', '+18%')  # Increase pitch by 18%
    prosody.set('rate', '+15%')  # Increase speed by 15%

    prosody.text = text

    # Convert to string
    body = ElementTree.tostring(xml_body)

    # Send the request
    response = requests.post(tts_endpoint, headers=headers, data=body)

    # Check for a successful response
    if response.status_code == 200:
        with open(file_name, "wb") as audio:
            audio.write(response.content)

        # Play the audio using simpleaudio
        audio = AudioSegment.from_wav(file_name)
        play_obj = sa.play_buffer(audio.raw_data, num_channels=audio.channels, bytes_per_sample=audio.sample_width, sample_rate=audio.frame_rate)
        play_obj.wait_done()

        # Delete the file after playback
        os.remove(file_name)
    else:
        print(f"Error: {response.status_code}, {response.text}")

if __name__ == '__main__':
    # Example usage
    text_to_speech("Hello! ooh-mimi ja-nye here! how's your day?")
    text_to_speech("Elden ring!! It's like FromSoftware took everything they've learned from their previous titles and cranked it up to eleven.")
