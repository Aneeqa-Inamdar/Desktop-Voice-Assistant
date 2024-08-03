import pyttsx3
import subprocess
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from ecapture import ecapture as ec
import time
import sys
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening!")
    speak("Hello! I am Baymax. How may I help you Mam?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.........")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception as e:
        print(e)
        speak("Sorry, I didn't catch that. Can you please repeat?")
        return ""


if _name_ == "_main_":
    wishMe()
    query = takeCommand().lower()

    if 'wikipedia' in query:
        speak("Searching Wikipedia......")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=4)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        sys.exit()

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        sys.exit()
    elif 'open google' in query:
        webbrowser.open("google.com")
        sys.exit()
    elif 'open facebook' in query:
        webbrowser.open("facebook.com")
        sys.exit()
    elif 'open gmail' in query:
        webbrowser.open("gmail.com")
        sys.exit()
    elif 'open stack overflow' in query:
        webbrowser.open("stackoverflow.com")
        sys.exit()


    elif 'play music' in query:
        music_dir = 'D:\\Song'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir, songs[0]))
        sys.exit()

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Mam, the time is {strTime}")
        sys.exit()

    elif 'open code' in query:
        codePath = "D:\project Baymax"
        os.startfile(codePath)
        sys.exit()

    elif "where is" in query:
        def searchLocation(location):
            query = location.replace(" ", "+")
            url = f"https://www.google.com/maps/search/{query}"
            webbrowser.open(url)

        if "where is" in query:
            location = query.replace("where is", "")
            speak("User asked to locate")
            speak(location)
            searchLocation(location)
        sys.exit()

    elif "camera" in query or "take a photo" in query:
        ec.capture(0, "baymax camera ", "img.jpg")
        sys.exit()

    elif "restart" in query:
        subprocess.call(["shutdown", "/r"])
        sys.exit()

    elif "hibernate" in query or "sleep" in query:
        speak("Hibernating")
        subprocess.call("shutdown / h")
        sys.exit()

    elif "log off" in query or "sign out" in query:
        speak("Make sure all the application are closed before sign-out")
        time.sleep(5)
        subprocess.call(["shutdown", "/l"])
        sys.exit()

    else:
        speak("I'm sorry, I didn't understand that.")
        sys.exit()