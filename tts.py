import os
from time import sleep
from dotenv import load_dotenv
import requests

#Text to voice with ElevenLabs
class TTS():
    def __init__(self):
        load_dotenv()
        self.key = os.getenv('ELEVENLABS_API_KEY')
    
    def process(self, text):
        CHUNK_SIZE = 1024
        # Use an elevenlabs voice
        url = "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL"

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.key
        }

        data = {
            "text": text,
            "model_id": "eleven_multilingual_v1",
            "voice_settings": {
                "stability": 0.55,
                "similarity_boost": 0.55
            }
        }

        # Save the audio in static/response.mp3 so that the website
        # can read and play it in the browser
        file_name = "response.mp3"

        # Validate if the directory exists
        if os.path.isdir("static/"):
            pass
        else:
            os.mkdir("static/")

        # Delete the audio from the previous run
        if os.path.exists("static/" + file_name):
            os.remove("static/" + file_name)
            sleep(2)
        
        # Create the audio
        response = requests.post(url, json=data, headers=headers)
        with open("static/" + file_name, 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
                    
        return file_name
