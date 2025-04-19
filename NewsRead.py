import requests
import json
import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 150)

# Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestnews():
    api_dict = {"business":"https://newsapi.org/v2/top-headlines?country=gb&category=business&apiKey=878a59ab517e4c15aca80adde1405bed",
               "entertainment":"https://newsapi.org/v2/top-headlines?country=gb&category=entertainment&apiKey=878a59ab517e4c15aca80adde1405bed",
               "health":"https://newsapi.org/v2/top-headlines?country=gb&category=health&apiKey=878a59ab517e4c15aca80adde1405bed",
               "science":"https://newsapi.org/v2/top-headlines?country=gb&category=science&apiKey=878a59ab517e4c15aca80adde1405bed",
               "sports":"https://newsapi.org/v2/top-headlines?country=gb&category=sports&apiKey=878a59ab517e4c15aca80adde1405bed",
               "technology":"https://newsapi.org/v2/top-headlines?country=gb&category=technology&apiKey=878a59ab517e4c15aca80adde1405bed"
 }

    content = None
    url = None
    speak("Which field do you want, [business] , [health] , [technology] , [sports] , [entertainment] , [science]")
    field = input("Type field news that you want: ")
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("Url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more visit: {news_url}")
           
        a = input("[Press 1 to continue] and [Press 2 to stop]")
        if str(a) == "1":
            pass
        elif str(a) == "2":
            break

    speak("That's all")
    