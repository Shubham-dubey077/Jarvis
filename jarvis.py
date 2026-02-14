import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pyjokes
import wikipedia
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hey Shubham, how can i help you")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"User said:{query}\n")

    except sr.UnknownValueError:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('codinglearner7@gmail.com' 123')
    server.sendmail('codinglearner7@gmail.com',to, content)
    server.close()

    
if __name__== "__main__":
    wishMe()
    # while True:
    if 1:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        # elif "open whatsapp".lower() in query.lower(): 
        #     os.system("open whatsapp")

        elif 'open music' in query:
            webbrowser.open("https://soundcloud.com/bhagirath20/5000-old-songs-1")

        elif 'the time' in query:
            # strTime = datetime.datetime.now().strftime("%H:%M:%S")
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak(f"Sir time is {hour} bajjkee {min} minutes")
            print(hour, min)
            # speak(f"Sir, the time is{strTime}")
            
        elif 'open code' in query:
            codePath = "C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to shubham' in query:
            try:
                speak("what should I say?")
                content = takecommand()
                to = "codinglearner7@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry my freind shubham bhai. I am not able to send this email")