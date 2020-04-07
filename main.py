import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import random
import webbrowser
import os
import smtplib

# path for open software
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
firefox_path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
vs_code = "C:\\Users\\Ash\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
sublime = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"


# voice engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

def takeCommand():
    # it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening...")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n")
    except Exception as e:
        print(e)
        speak("Say that again please...")
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    speak("What Can I Help You?")
    while True:
    # if 1:
        query = takeCommand().lower()
        # open some websites
        if 'open google' in query:
            if 'in firefox' in query:
                webbrowser.get(firefox_path).open("google.com")
                print("Opened Google in Firefox")
            else:
                webbrowser.get(chrome_path).open("google.com")
                print("Opened Google in Chrome")

        elif 'open github' in query:
            if 'in firefox' in query:
                webbrowser.get(firefox_path).open("github.com")
                print("Opened Github in Firefox")
            else:
                webbrowser.get(chrome_path).open("github.com")
                print("Opened Github in Chrome")

        # open chrome and firefox
        elif 'open chrome' in query:
            webbrowser.get(chrome_path).open("google.com")
            print("Opened Chrome")

        elif 'open firefox' in query:
            webbrowser.get(firefox_path).open("google.com")
            print("Opened Firefox")

        # open code editor
        elif 'open vs code' in query:
            os.startfile(vs_code)
            print("Opened Vs Code")

        elif 'open sublime text' in query:
            os.startfile(sublime)
            print("Opened Sublime text")

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            # print(type(songs))
            # print(songs)
            song = random.choice(songs)
            print(song)
            os.startfile(os.path.join(music_dir, song))

        # time now
        elif 'time now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        # today date
        elif 'today date' in query:
            strDate = datetime.date.today().strftime("%d/%m/%Y")
            speak(f"Sir, the date is {strDate}")
            print(strDate)

        # wikipedia search
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'what is your name' in query:
            speak("my name is Ash. and i am your assistant")

        elif 'exit' in query:
            speak("i will see you again")
            exit()
