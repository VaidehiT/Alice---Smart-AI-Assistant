# SearchNow.py

import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

# Text-to-speech setup
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("google", "").replace("search", "").replace("Alice", "").strip()
        speak("This is what I found on Google.")
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 2)
            speak(result)
        except:
            speak("No speakable result found.")

def searchYoutube(query):
    if "youtube" in query:
        speak("Here's what I found on YouTube.")
        query = query.replace("youtube", "").replace("search", "").replace("Alice", "").strip()
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done.")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "").replace("search", "").replace("Alice", "").strip()
        try:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            print(results)
            speak(results)
        except:
            speak("Couldn't find anything on Wikipedia.")
