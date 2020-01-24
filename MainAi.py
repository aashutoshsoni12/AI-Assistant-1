# This project is developed in Ubuntu 18.04. So install libraries and sounds according to your operating system.

import pyttsx3
import speech_recognition as sr
import wikipedia
import os
import datetime
import smtplib
import webbrowser
from pydub import AudioSegment
from pydub.playback import play

engine = pyttsx3.init()  # Initialise the voices
voices = engine.getProperty('voices')
engine.setProperty('voice', 'english+m3')  # Set the type of voice.
engine.setProperty('rate', 160)  # Set the type of voice.
engine.setProperty('volume', 1.0)  # Set the volume of the output voice.


def speak(audio):  # Will speak the arguments given.
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)  # Take the hours from datetime module
    if 0 <= hour < 12:
        speak('Good Morning Sir')
    elif 12 <= hour < 18:
        speak('Good Afternoon Sir')
    else:
        speak('Good Evening Sir')
    speak('I am your assistant, please tell how may I help you')


'''
def takeCommand():
    # It takes microphone input from the user and returns string output
    # Use this function only if you have pyaudio installed in your system.
    # If this dosnt work, just type and take the input. by function - def writeCommand()  

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
'''


def writeCommand():  # Use this function if speech recognition doesnt work.
    speak("please type your command")
    try:
        # print("Sir, please Enter your command...")
        query = input("Sir, please type your command...\n")
    except Exception:
        print("Sorry sir, you entered something wrong")
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = writeCommand()

        # Logic for executing task based on query.
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            print("Searching Wikipedia...")
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=10)
            speak("According to wikipedia")
            print(results)
            speak(results)
            break

        elif 'youtube' in query:
            speak('Opening youtube')
            webbrowser.open('youtube.com')
            break

        elif 'google' in query:
            speak('opening google')
            webbrowser.open('google.com')
            break

        elif 'stackoverflow' in query:
            speak('opening stack overflow')
            webbrowser.open('stackoverflow.com')
            break

        elif 'play music' in query:
            song = AudioSegment.from_mp3('avicii.mp3')
            play(song)
            break

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, The time is {strTime}")

        elif 'terminal' in query:
            os.system('gnome-terminal')
            break

        elif 'facebook' in query:
            speak('opening facebook')
            webbrowser.open('facebook.com')
            break

        elif 'tweaks' in query:
            speak('opening gnome tweaks')
            os.system('gnome-tweaks')
            break

# After these tasks, many other tasks can also be automated like sending emails.
