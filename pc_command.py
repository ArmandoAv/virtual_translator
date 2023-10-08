import os
from webbrowser import open
from dotenv import load_dotenv

class PcCommand():
    def __init__(self):
        pass
    
    # Open browser
    def open_browse(self):
        load_dotenv()
        url = os.getenv('URL')
        
        open(url, new=2, autoraise=True)
