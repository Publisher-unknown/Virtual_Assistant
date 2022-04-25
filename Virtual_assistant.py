print("Initializing")



from pyjokes import get_joke
import speech_recognition as sr
import pyttsx3
import datetime
from wikipedia import summary

import webbrowser
from os import startfile
listener=sr.Recognizer()
with open("name.txt","a") as f:
    pass

with open ("name.txt",mode="r") as w:
    user_name=w.readline()
with open("wakeword.txt","a") as f:
    pass

with open ("wakeword.txt",mode="r") as w:
    wakewordreal=w.readline().lower()

def talk(text,rememeberable=True):
    print (text)
    speaker=pyttsx3.init('sapi5')
    voices=speaker.getProperty('voices')
    speaker.setProperty('voice',voices[1].id)
    speaker.say(text)
    speaker.runAndWait()
    print()
    if rememeberable==True:
        remember(f"{wakewordreal} said:{text} \n")
def wishMe():
    """greets based on time.Good morning good afternoon and good evening are the three types of greets"""
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        talk(f"Good Morning {user_name}",False)
    if hour>12 and hour<15:
        talk(f"Good afternoon {user_name}",False)
    else:
        talk(f"Good Evening {user_name}",False)
def waiting():

        try:
            with sr.Microphone() as source:
                print ()
                print ("listening...")
                print()
                voice = listener.listen(source,phrase_time_limit=2,timeout=2)
                wakeword2 = listener.recognize_google(voice)
                wakeword2 = wakeword2.lower()
                return wakeword2
        except:
            pass     
def TakeCommand(rememberable=True):

        try:
            with sr.Microphone() as source:
                print ()
                print ("Ask anything ...")
                print ()
                
                voice = listener.listen(source)
                audiodata= listener.recognize_google(voice,language="en-in")
                print ()
                print ("recognizing...")
                print ()
                print (audiodata)
                if rememberable==True:
                    remember(f"{user_name} said:{audiodata} \n")
                print ()
            
        except sr.UnknownValueError:
            audiodata=""    
        except:
            pass  
        
        return audiodata
def remember(text):
    with open("C_log.txt",mode="a") as f:
        f.write(f"{text}\n")
def analyze():
                
    user_command=TakeCommand()
    user_command=user_command.lower()
    if "say" in user_command and "inverted" in user_command:
        user_command=user_command.replace("say","")
        user_command=user_command.replace("inverted","")
        talk(f"You said: {user_command[::-1]} ")
    elif "search for" in user_command:
        user_command=user_command.replace('seach for','')
        talk ("Searching wikipedia...")
        results=summary(user_command,2)
        talk (results)
    elif 'play' in user_command:
            from pywhatkit import playonyt
            user_command=user_command.replace('play','')
            talk('playing '+ user_command)
            playonyt(user_command)
    elif "take over the world" in user_command:
        talk ("I think I will take over the world on 2030, that sounds like a good year to start the war!")
    elif "time" in user_command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        talk ("It is "+time)
                
    elif "how are you" in user_command:
        talk("I am doing great today. Thanks for asking! what about you ?")
        y_or_n=TakeCommand()
        if    y_or_n in ['great','amazing','super','awesome','good']:
            talk("It is awesome that you have a great day ! ")
        else:
            talk("I am sorry! It will help if you talk to your friend or someone")
    elif user_command=="exit":
        talk("Have a great day sir!")
        quit()
    elif "introduce yourself" in user_command:
        talk (f" Hi everyone , I am {wakewordreal}. My master is {user_name} .  I don't like people calling me virtual . I can do anything . ")
    elif "joke" in user_command:
        joke=get_joke()
        talk (joke)
    elif "google for" in user_command:
        user_command=user_command.replace("google for","")
        webbrowser.open("https://google.com/search?q="+user_command)
    elif "open google" in user_command:
        webbrowser.open("google.com")
    elif "open facebook" in user_command:
        webbrowser.open("facebook.com")
    elif "open instagram" in user_command:
        webbrowser.open("instagram.com")
    elif "open stack overflow" in user_command:
        webbrowser.open("stackoverflow.com")
    elif "open wikipedia" in user_command:
        webbrowser.open("wikipedia.org")
    elif "open youtube" in user_command:
        webbrowser.open("youtube.com")
    elif "open code" in user_command:
        startfile("C:\\Users\\abhir\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

    elif "note" in user_command:
        talk("What should I say ?")
        note=TakeCommand(talking=False)
        seconds=datetime.datetime.now().second


        with open(f"note{seconds}.txt","w+") as f:
            f.write(note)
    

    else:
        talk("I don't understand")

if wakewordreal=="" or user_name=="":
    print ("------SETUP------")
    talk("Let's get to know each other. What's your name?",False)
    name=TakeCommand(rememberable=False)
    with open ("name.txt","w") as n:
        n.write(name)
    with open ("name.txt","r") as w:
        user_name=w.readline()
    talk(f"Hi {user_name}! Now what do you like to call me?",False)
    wakeword4=TakeCommand(rememberable=False)
    with open ("wakeword.txt","w") as w:
        w.write(wakeword4)
    with open ("wakeword.txt","r")as whatever:
        wakewordreal=whatever.readline().lower()

wishMe()
day=datetime.datetime.now().day
month=datetime.datetime.now().month
year=datetime.datetime.now().year
hour=datetime.datetime.now().hour
minutes=datetime.datetime.now().minute
remember(f"Conversation started on :   {hour}:{minutes} {day} / {month} /{year} \n")


while True:

    wakeword5=waiting()
    if wakeword5 ==wakewordreal:
        analyze()



