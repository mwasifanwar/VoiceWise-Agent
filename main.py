
#### main.py

```python
import speech_recognition as sr
from gtts import gTTS
import os
import playsound
from config import Config
from conversation.conversation_manager import ConversationManager
import logging

# Setup logging
logging.basicConfig(filename='logs/agent.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

config = Config()
conversation_manager = ConversationManager(config)

def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None

if __name__ == "__main__":
    logging.info("AI Voice Agent started.")
    while True:
        query = listen()
        if query:
            response = conversation_manager.handle_query(query)
            logging.info(f"User: {query} | Bot: {response}")
            print(f"Bot: {response}")
            speak(response)
