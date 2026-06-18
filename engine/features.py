from playsound import playsound
import eel
import os
from engine.command import speak
from engine.config import ASSISTANT_NAME

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\audio_startsound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query = query.lower().strip()

    if query:
        speak("Opening " + query)
        os.system("start " + query)
    else:
        speak("Not found")