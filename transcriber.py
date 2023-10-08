import openai

#Convert audio to text
class Transcriber:
    def __init__(self):
        pass
        
    # Create the audio.mps file with whisper
    def transcriber(self, audio):
        audio.save("audio.mp3")
        audio_file= open("audio.mp3", "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript.text
