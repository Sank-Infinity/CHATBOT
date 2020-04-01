#Importing Required libraries 
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import turtle
import wikipedia
import random
import webbrowser
import os
import smtplib
import array as arr
 
machine = pyttsx3.init('sapi5')
voices = machine.getProperty('voices')
machine.setProperty('voice', voices[0].id)

def speak(audio):  
    machine.say(audio)
    machine.runAndWait()

class Circle():
    pi = int(3.14)
    def __init__(self,radius=1):
        self.radius = int(radius)

    def get_circumference(self):
        speak("You will get result soon.....")
        circumference = (self.radius * self.pi * 2)
        print("Circumference of circle is " + str(circumference))
        speak("Circumference of circle is " + str(circumference))
    def get_area(self):
        speak("You will get result soon.....")
        area = (self.radius *self.radius*self.pi)
        print("Area of circle is " + str(area))
        speak("Area of circle is " + str(area))

class Rec():

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def get_area(self):
        speak("You will get result soon.....")
        area = (self.length*self.breadth)
        print("Area of Rectangle is "+ str(area))
        speak("Area of rectangle is " + str(area))

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning BOSS..!!!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon BOSS...!!!")
    elif hour >= 18 and hour < 20:
        speak("Good Evening BOSS...!!!")
    else:
        speak("Good Night BOSS...!!!")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.dynamic_energy_threshold = 50
        audio = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said:{query}\n")
    except Exception as e:
        speak('I dont get you boss please say that again.......')
        print('please say that again....\n\n')
        return "NONE\n\n"
    return query

def triangle():
    speak("Here, it is.....You can see")
    window = turtle.Screen()
    window.screensize(400,300,'red')
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("black")
    brad.forward(100)
    brad.right(120)
    brad.forward(100)
    brad.right(120)
    brad.forward(100)

def circle(radius):
    speak("Here, it is.....You can see")
    window = turtle.Screen()
    window.screensize(400, 300, 'red')
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("black")
    brad.circle(radius)

def rectangle():
    speak("Here, it is.....You can see")
    window = turtle.Screen()
    window.screensize(400, 300, 'red')
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("black")
    brad.forward(100)
    brad.right(90)
    brad.forward(50)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(50)


if __name__ == "__main__":
    wishMe()
    min=0
    max=5
    r = str(random.randint(min, max))

    if r=='0':
        speak("I am Alvis!!!!!")
    elif r=='1':
        speak("..What was I thinking? You’re usually so discreet...?")
    elif r=='2':
        speak("How are YOU .....!!!")
    elif r=='3':
        speak("Always at your SERVICE .....")
    elif r=='4':
        speak("i'm just waiting for you, i just done with terabytes of calculations...... now we can proceed....?")
    else:
        speak("what is going around sir......?")

    alvis = True

    while alvis:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("i am on the way of wikipedia...results will coming soon...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("i got the results boss.....According to wikipedia....")
            print(results)
            speak(results)

        if 'open' and 'youtube' in query:
            speak("Opening YOuTUbe very soon....")
            webbrowser.open("https://www.youtube.com/")

        if 'play music' in query:
            speak("OPening Melody.......")
            music_dir = 'Insert Path'
            song = os.listdir(music_dir)
            length = len(song)
            min = 0
            max = (length-1)
            p = int(random.randint(min, max))
            os.startfile(os.path.join(music_dir, song[p]))

         
        if 'who creates you' in query:
            speak('I Have created by THE MECHANIC.......I CALL HIM AS BOSSS......')

        if 'how are you' in query:
            min = 0
            max = 3
            reply = str(random.randint(min, max))
            if reply=='0':
                speak("I am fine BOSS.....")
            if reply=='1':
                speak("I am ROcking.....")
            if reply=='2':
                speak("Feeling so enthusiastic .......")
            if reply=='3':
                speak("NOTHING. AS USUAL....")

        

        if 'what' and 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        if 'your name' in query:
            speak("MY NAME is ALVIS....")

        if 'long form of your name' in query:
            speak("A LOGICAL VAST INTELLIGENT SYSTEM....")

        if 'where' and 'live' in query:
            speak("IN BETWEEN inside coding of complicated hardware circuits which works on voltage of 0s and 1s ...")

        if 'draw' and 'shape' in query:
            speak("which Shape i need to draw, master....?")
            temp = takecommand()
            if temp == 'Triangle' or temp == 'triangle' :
                triangle()
            elif temp == 'rectangle':
                rectangle()
            elif temp == 'circle':
                circle(100)
            else:
                speak("still i am not programmed for draw that shape.")

        if 'why are you exist' in query:
            speak("FOR Helping and provide security to HUMANS.....")

        if 'open google' in query:
            speak("Which thing do you want to search.....???")
            temp = takecommand()
            webbrowser.open("https://google.com/search?q=%s" % temp)


        if 'create' and 'folder' in query:
            speak("Where do you want to create folder?")
            temp= takecommand()
            if 'desktop' in temp:
                speak("got it BOSS.....")
                os.chdir(r"Insert Path")
                speak("Your directory bosss...")
                print(os.getcwd())
                speak("which name should i give to folder...")
                name = takecommand()
                os.mkdir(name)
                speak("i am ready with your folder, please check it....")
            if 'downloads' in temp:
                speak("got it BOSS.....")
                os.chdir(r"Insert Path")
                speak("Your directory bosss...")
                print(os.getcwd())
                speak("which name should i give to folder...")
                name = takecommand()
                os.mkdir(name)
                speak("i am ready with your folder, please check it....")
            if 'documents' in temp:
                speak("got it BOSS.....")
                os.chdir(r"Insert Path")
                speak("Your directory bosss...")
                print(os.getcwd())
                speak("which name should i give to folder...")
                name = takecommand()
                os.mkdir(name)
                speak("i am ready with your folder, please check it....")
            if 'videos' in temp:
                speak("got it BOSS.....")
                os.chdir(r"Insert Path")
                speak("Your directory bosss...")
                print(os.getcwd())
                speak("which name should i give to folder...")
                name = takecommand()
                os.mkdir(name)
                speak("i am ready with your folder, please check it....")

        if 'open' and 'file' in query:
            speak("Locate directory if required....")
            temp1 = takecommand()
            if 'desktop' in temp1:
                os.chdir(r"Insert path")
                print(os.listdir(r"Insert Path"))
                speak("Which file do you want to open ?")
                name1 = takecommand()
                os.startfile(name1)
                speak("Opening file in few seconds........")

         

        if 'show' and 'movie' in query:
            os.chdir(r"Insert Path")
            print(os.listdir(r"Insert path"))
            speak("WHich movie you would like to see....?")
            movie = takecommand()
            if 'Iron Man 1' in movie:
                os.chdir(r"Insert Path")
                os.startfile("Inset file name")
            if 'Iron Man 2' in movie:
                os.chdir(r"Insert Path")
                os.startfile("Inset file name")
            if 'Iron Man 3' in movie:
                os.chdir(r"Insert Path")
                os.startfile("Inset file name")
            if 'strange' in movie:
                os.chdir(r"Insert Path")
                os.startfile("Inset file name")
               


        if 'q and a' in query:
            speak("I am ready ask what you want.....")
            Q_and_A = True
            while Q_and_A:
                question = takecommand()
                if 'you' and 'genius' in question:
                    speak("Thank you...")
                if 'ok stop it' in question:
                    speak("Ok boss.....")
                    break
                else:
                    try:
                        question = question.replace("wikipedia", "")
                        results = wikipedia.summary(question, sentences=3)
                        print(results)
                        speak(results)
                        speak("next question....Please")
                    except Exception as e:
                        speak("May I don't get, Please repeat question..... ")

        if 'you' and 'like' in query:
            speak("To do Work...!!!")


        if 'find' and 'circumference' in query:
            speak("Please Enter radius.....")
            rad = int(input("Enter Radius:"))
            my_circle = Circle(rad)
            my_circle.get_circumference()

        if 'find' and 'area' and 'circle' in query:
            speak("Please Enter radius.....")
            rad = int(input("Enter Radius:"))
            my_circle = Circle(rad)
            my_circle.get_area()

        if 'find' and 'area' and 'rectangle' in query:
            speak("Please Enter Length.")
            length = int(input("Enter Length:"))
            speak("Please Enter Breadth.")
            breadth = int(input("Enter Breadth:"))
            my_rec = Rec(length,breadth)
            my_rec.get_area()

        if "do you" and "eat" in query:
            speak("No, Unfortunately I can't eat anything....")

        if "do you" and "drink" in query:
            speak("No, Unfortunately I can't drink anything....")

        if 'see you soon' in query:
            speak("OK boss....TAKE CARE")
            alvis = False
