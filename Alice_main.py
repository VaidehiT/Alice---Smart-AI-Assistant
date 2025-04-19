import pyttsx3
import speech_recognition
from Greetings import greetMe  # Import the greetMe function
import requests
import bs4
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import random
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)

# Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Command function to listen to audio
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        try:
            audio = r.listen(source, timeout=5)  # Adjust timeout for no input
            print("Audio captured, understanding...")
        except speech_recognition.WaitTimeoutError:
            print("Timeout, didn't hear anything.")
            return "None"
        except Exception as e:
            print(f"Error: {e}")
            return "None"

    try:
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't understand. Please repeat.")
        return "None"
    return query

# Weather function using OpenWeatherMap API
def get_weather_via_api(city_name):
    api_key = "ae551de825887d4e970edc234c0f8c83"  # Your working key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            return f"Sorry, I couldn't find weather data for {city_name}."

        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]
        city = data["name"]
        country = data["sys"]["country"]

        return f"The current temperature in {city}, {country} is {temp}°C, feels like {feels_like}°C with {description}."
    except Exception as e:
        print(f"Weather API error: {e}")
        return "Sorry, I couldn't fetch the weather right now."
    
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
    
# Main program loop
if __name__ == "__main__":
    print("Program started")
    is_awake = False  # To track if the assistant is already awake

    while True:
        query = takeCommand().lower()
        print(f"Query: {query}")  # Check what's captured

        # Check if the query is "wake up"
        if "wake up" in query and not is_awake:
            greetMe()  # Call greetMe from the greetMe.py file
            is_awake = True  # Set the assistant as awake
            print("Assistant is awake!")

            while True:
                query = takeCommand().lower()
                print(f"Inner Query: {query}")

                if "go to sleep" in query:
                    speak("Ok V, You can call me anytime.")
                    is_awake = False  # Reset the assistant's state
                    break

                elif "hello" in query:
                    speak("Hello V, How are you?")
                    
                elif "i am good" in query:
                    speak("That's great V!")
                    
                elif "how are you" in query:
                    speak("Amazing V, thanks for asking!")
                
                elif "how old are you" in query:
                    speak("You made me, V!")
                    
                elif "thank you" in query:
                    speak("Anytime love!")
                    
                elif "who do i like" == query:
                    speak("That's easy, Vicky!")

                elif "tired" in query or "Play my favourite song" in query:
                    speak("Sure V! playing now")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=MpST_mgRoU4")
                    elif b==2:
                        webbrowser.open("https://www.youtube.com/watch?v=RNYFp8uYDLw")
                    elif b==3:
                        webbrowser.open("https://www.youtube.com/watch?v=EiiOYwqk3A0")

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("Video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down")
                    volumedown()

                elif "open" in query:
                    from Dictapp import opeenappweb
                    opeenappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)


                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews() 

                elif "temperature" in query or "weather" in query:
                    speak("Please tell me the city name.")
                    city_query = takeCommand().lower()
                    if city_query != "None":
                        weather_report = get_weather_via_api(city_query.strip())
                        speak(weather_report)
                    else:
                        speak("Sorry, I didn't catch the city name.")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("set the time")
                    a = input("please tell the time:- ")
                    alarm(a)
                    speak("Done v")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"V, the time is {strTime}")

                elif "finally sleep" in query:
                    speak("bye bye V")
                    exit()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("Alice","")
                    speak("I was told to" + rememberMessage)  
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage) 
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to" + remember.read())              

                else:
                    print(f"Unrecognized query: {query}")