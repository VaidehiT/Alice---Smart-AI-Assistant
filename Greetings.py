import pyttsx3
import datetime

print("Greetings module loaded")  # Add this at the top of Greetings.py

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, V")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon, V")
    else:
        speak("Good Evening, V")

    speak("How can I help you today?")