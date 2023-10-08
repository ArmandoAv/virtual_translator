from googletrans import Translator

# Translates text to English
class Translate:
    def __init__(self):
        pass
        
    def translate(self, text):

        translator = Translator()
        text_english = translator.translate(text, dest = 'en')
        return text_english.text
