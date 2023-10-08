import os
import openai
from dotenv import load_dotenv
from flask import Flask, render_template, request
from transcriber import Transcriber
from tts import TTS
from pc_command import PcCommand
from translate import Translate


# Load keys from .env file
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
elevenlabs_key = os.getenv('ELEVENLABS_API_KEY')

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("recorder.html")

@app.route("/audio", methods=["POST"])
def audio():
    # Get recorded audio and transcribe it
    audio = request.files.get("audio")
    text = Transcriber().transcriber(audio)
    print(f"You want to traslate: \n {text}")

    # Transalate text into English
    final_response = Translate().translate(text)
    print(f"Your translation is: \n {final_response}")
    print(type(final_response))
    tts_file = TTS().process(final_response)
    return {"result": "ok", "text": final_response, "file": tts_file}

# Main function
if __name__ == "__main__":
    tab = 0
    while tab < 1:
        PcCommand().open_browse()
        tab += 1

    app.run(debug=True)
