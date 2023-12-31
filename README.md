# virtual_translator

This repository is based on the Virtual Assistant on the Ringa Tech channel

## Configuration

To execute the project it is necessary:

Download the repository

```git clone https://github.com/ArmandoAv/virtual_translator.git```

Have a version of Python 3.8 or higher installed.

Optional: Create a virtual environment

```python -m venv venv```

Install dependencies by running

```pip install -r requirements.txt```

Create a file called ```.env``` place the keys in the file:

```
OPENAI_API_KEY=<your_openai_api_key>
ELEVENLABS_API_KEY=<your_elevenlabs_api_key>
URL=http://localhost:5000/
```

If you don´t have an openai or eleven labs api key. You can get the openai or eleven labs api key in the following links

```
https://openai.com/
https://elevenlabs.io/speech-synthesis
```

## Execution

This project uses Flask. You can start the server in debug mode by default on port 5000 with the command

```py app.py```

The program will run the server in debug mode by default and open the browser at the link 

```http://localhost:5000```
	
If it doesn't open automatically you can open it manually at that link

When you are in the link

- Click on the microphone to start recording
- Say the word or sentence you want to translate
- Click on the microphone to stop recording
- It will return the word or sentence translated into English
