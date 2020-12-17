import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

# engine.say("hello sir i am jarvis")
# engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")

    speak("I am jarvis!What can i help you?")

def takeCommand():
    "it tacks command through microphone"
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        #print(e)

        print("say that again please..")
        return "None"
    return query
if__name__ = '__main__'
wishMe()
query="open chrome"
if 'wikipedia' in query:
    speak("searching wikipedia sir!please wait!")
    result=wikipedia.summary(query,sentences=2)
    speak("According to wikipedia!")
    print(result)
    speak(result)
elif 'open youtube' in query:
    webbrowser.open("youtube.com")
elif 'open google' in query:
    webbrowser.open("googlechrom.com")
elif 'play song' in query:
    music="G:\\22 MIX HITZ"
    songs=os.listdir(music)
    print(songs)
    print(len(songs))
    n=random.randint(0,56)
    os.startfile(os.path.join(music,songs[n]))

elif 'time' in query:
    strTime=datetime.datetime.now().strftime("%H:%M:%S")
    print(strTime)
    speak(f"sir!the time is {strTime}")

elif 'open chrome' in query:
    chromePath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    os.startfile(chromePath)


