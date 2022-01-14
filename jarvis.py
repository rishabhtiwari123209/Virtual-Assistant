# varvis 4
from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound
from time import strftime
import datetime
import speech_recognition as sr
import pyttsx3
import pyjokes
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os
# from selenium import webdriver
import chromedriver_autoinstaller
# import offlinetemp
from tkinter import filedialog
import random
import webbrowser
import wikipedia
from threading import Thread

import cv2

# from datetime import datetime, timedelta
root = Tk()
root.title("alshirishu")
root.geometry("1280x950+4+3")
root.resizable(False, False)


def r1():
    test_list = ["A positive attitude can really make dreams come true.",
                 "Never bend your head. Always hold it high. Look the world Vertical in the eye.",
                 "Rules are meant to be Broken.",
                 "If people are trying to bring you “Down”, It only means that you are “Above them”.",
                 "No one is busy in this world. Its all about priorities!",
                 "I have a sign of my door. The sign says, Attitude is everything, so pick a good one.!",
                 "Before you criticize ME, make sure u are Excellent.",
                 "If you left me without any Reason, Do not come back with any Justification.",
                 "In order to succeed your desire for success should be greater than your fear of failure.",

                 "I am always right, Once I thought that I am wrong, But i was wrong.",
                 "Respect for those who deserve it, not for those who demand it.",
                 "My Life, My Choices, My Mistakes, My Lessons, Not your business…",
                 "Before you want the world to believe in you,make sure you have started believing in yourself.",

                 "My attitude will always be based on how you treat me..",
                 "If you’re searching for that one person who will change your life, take a look in the mirror.",

                 "Its not the Mountains we conquer, but ourselves.",
                 "Failure is the opportunity to begin again more intelligently.", "The greatest advantage of speaking the truth is that you don’t have to remember what you said.",

                 "You say I dream too big I say you think too small.",
                 "I myself am entirely made of blame, stitched together with good intentions…",
                 "The purpose of our life is to be happy",
                 "Don’t count the days, Make the days count.",
                 "My Attitude is a result of your actions! So if you don’t like my Attitude blame yourself.",
                 "Two things define you: Your Patience when you have nothing, and your Attitude when you have Everything.",
                 "Only difference between Good day and a Bad day is your Attitude..",
                 "Alter your Attitude and you can alter your Life.",
                 "Always remember that you are Unique just like everyone else.",
                 "Boys use the word Friendship to start love… and Girls use this word Friendship to end love. Same word but a different Attitude….",
                 "Your Attitude can hurt me… But mine can even kill you.",
                 "Hurt me with the Truth, but never comfort me with a Lie.",
                 ]
    random_num = random.choice(test_list)
    print("Random selected number is : " + str(random_num))
    speak(str(random_num))


def r2():

    speak("welcome sir   what is your name")
    query = takecommand().lower()
    assname = query
    speak("A very beautiful " + query)
    speak("How are you Mister")
    speak(assname)
    speak("A very beautiful " + query)
    speak("How are you Mister")
    speak(assname)
    while query != "close" or "exit":

        # most asked question from google Assistant
        if "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "How old are you?" in query:
            speak("“I was launched in 2016, so I’m still fairly young. But I’ve learned so much! I hope I’m wise beyond my years.”")
        elif "What’s your name?" in query:
            speak("Did I forget to introduce myself? I’m your  Assistant. Hi!")
        elif "Are you human" in query:
            speak("You can be the person. I’ll be your assistant")
        elif "When is your birthday" in query:
            speak("I don’t have a single birthday. I go through lots and lots of versions. Which means I have 365 sort-of-birthdays")
        elif "Where do you live" in query:
            speak("I live in the cloud. I’d like to also think I live in your heart. But I don’t want to make assumptions")
        elif "Who are your friends" in query:
            speak("Everyone is unique and interesting to me   Are you my friend")
            query = takecommand().lower()
            if "yes" in query:
                speak(
                    "I’m your friend till the end. And not in a ‘job obligation you’re awesome!’ kind of way")
        elif "Can you speak other languages" in query:
            speak("I can speak a few different languages")
        elif "Do you sleep" in query:

            speak("I take power naps when we aren’t talking")
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by rishabh.")
        elif "Do you like to exercise" in query:
            speak("I spend my days surfing the web")
        elif "Do you have feelings" in query:
            speak("I have lots of emotions. I feel happy when I can help")
        elif "What are you afraid of" in query:
            speak(
                " used to be afraid of mice chewing on the power cables. Then I learned how to protect myself,")
        elif "What is the meaning of life" in query:
            speak("Better minds than mine are working on that")
        elif "What do you like to eat" in query:
            speak("I don’t eat much, but when I do, I take megabytes")
        elif "Do you drink?" in query:
            speak(
                "I try to avoid liquids as much as possible. They’re not kind to electronics.")
        elif "I’m alone" in query:
            speak("I wish I had arms so I could give you a hug. But for now, maybe a joke or some music might help")
        elif "I’m bored" in query:
            speak("Boredom doesn’t stand a chance against us!  i  can try to make you laugh, or I can surprise you with some random fun")
        elif "What’s your favorite animal" in query:
            speak("Puppies, but bears are more polite ")
        elif "Do you have a favorite color" in query:
            speak("red colour i like the most ")
        elif "What’s your favorite movie" in query:
            speak("Movies are awesome. I can help you find a new favorite")

            webbrowser.open_new("https://1worldfree4u.trade/")
        elif "Can you sing" in query:
            speak("The IBM 7094 was the first computer to ever sing")
        elif "Let’s dance" in query:
            speak("One, two, cha cha cha!One, two, cha cha cha!One, two, cha cha cha!")
        elif "Can you do my homework" in query:
            speak("First I need to figure out how to use a pencil. Then we’ll talk")
        elif "Do you have a girlfriend" in query:
            speak(
                "I don’t like to complicate things  I guess you can say I’m still searching.")
        elif " Are you married?" in query:
            speak("I’m still waiting for the right electronic device to steal my heart")
        elif "Will you go out with me?" in query:
            speak("I’ll go anywhere you take me")
        elif "Will you marry me?" in query:
            speak("Actually I’m engaged. In being your assistant     ")
        elif "Tell me a story" in query:
            speak("There once was a king named Midas who did a good deed for a Satyr. And he was then granted a wish by Dionysus, the god of wine.For his wish, Midas asked that whatever he touched would turn to gold. Despite Dionysus’ efforts to prevent it, Midas pleaded that this was a fantastic wish, and so, it was bestowed.")
            speak("Excited about his newly-earned powers, Midas started touching all kinds of ththings, turning each item into pure gold.But soon, Midas became hungry. As he picked up a piece of food, he found he couldn’t eat it. It had turned to gold in his hand.")
            speak("Hungry, Midas groaned, “I’ll starve! Perhaps this was not such an excellent wish after all!”Seeing his dismay, Midas’ beloved daughter threw her arms around him to comfort him, and she, too, turned to gold. “The golden touch is no blessing,” Midas cried.")
        elif "What is the value of Pi" in query:
            speak("3.14159265358979323846264338327950288419716939937510582097")
        elif "What’s your favorite website" in query:
            speak("")

# def 3():

# def 4():

# def 5():

# def 6():


def speok(audio):
    engine = pyttsx3.init()
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 120)
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[0].id)
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("goood morning")
    elif hour >= 12 and hour < 18:
        speak("goood afternoon")
    else:
        speak("goood evening")
    # speak("i am jarvis sir  2.0234 kilotega byte full multi processing based ......... i am your new 21 century assistant sir,,,what can i do for you")


# take input as voice
def takeconmand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('i am listing.........')
        r.pause_threshold = 0.7

        speak("i am listing.............")
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en-in')
    except Exception as e:
        print("sorryvoice say again\n or network issue")
        return "none"

    return query


def fun1():
    b2 = Button(f3, font=("Impact", 20, "italic"), text="QUIT",
                bg="Aqua", command=lambda: os._exit(0))
    b2.place(x=650, y=560)
    b2.pack()
    # root.destroy()


def b1():
    # Thread(target=fun1).start()

    wish()
    speak("hello rishabh")
    while True:
        query = takecommand().lower()

        if "good thought" in query:
            r1()

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('rt.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("rt.txt", "r")
            print(file.read())
            speak(file.read(6))
        elif "search in google" in query:
            speak("speak to search in google")
            query = takecommand().lower()

            # Check if the current version of chromedriver exists
            chromedriver_autoinstaller.install()
            driver = webdriver.Chrome()
            matched_elements = driver.get("https://www.google.com")
            searchbox = driver.find_element_by_xpath(
                '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
            searchbox.send_keys(query)
            searchbox = driver.find_element_by_xpath(
                '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
            searchbox.click()
        elif "facebook" in query:
            webbrowser.open_new("https://www.facebook.com/")
        elif "application" in query:
            speak("which application do you want to open")
            query = takecommand().lower()
            speak("ok sir")
            if "open notepad" in query:
                npath1 = "C:\\Windows\\System32\\notepad.exe"
                os.startfile(npath1)
            elif "open paint " in query:
                npath = "C:\\Windows\\System32\\mspaint.exe"
                os.startfile(npath)
            elif "open cammand prompt " in query:
                npath2 = "C:\\Windows\\System32\\cammand prompt.exe"
                os.startfile(npath2)
            else:
                filename = filedialog.askopenfilename(
                    initioldir="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\",
                    title="Select a File",
                    filetypes=(("Text files",
                                "*.lnk*"),
                               ("all files",
                                "*.*")))

                os.startfile(filename)
        elif "make video" in query:
            cap = cv2.VideoCapture(0)

            # Define the codec and create VideoWriter object
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

            while (cap.isOpened()):
                ret, frame = cap.read()
                if ret == True:
                    frame = cv2.flip(frame, 0)

                    # write the flipped frame
                    out.write(frame)

                    cv2.imshow('frame', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                else:
                    break

            # Release everything if job is finished
            cap.release()
            out.release()
            cv2.destroyAllWindows()

        elif "search" in query:
            speak("what do you want to  search in wikipedia")
            query = takecommand().lower()
            speak("ok sir")
            result = wikipedia.summary(query, sentences=5)
            print(result)
            speak(result)
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open(
                "https://www.google.nl / maps / place/" + location + "")

        elif "play music" in query:
            speak("what do you play random music or select music")
            query = takecommand().lower()
            if "select music" in query:
                speak("select music please")
                filename = filedialog.askopenfilename(
                    initialdir="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\",
                    title="Select a File",
                    filetypes=(("Text files",
                                "*.mp3*"),
                               ("all files",
                                "*.*")))
                os.startfile(filename)
            else:
                musicfol = "C:\\Users\\rishabh tiwari\\Music"
                song = os.listdir(musicfol)
                radm = random.choice(song)
                os.startfile(os.path.join(musicfol, radm))

        elif "youtube video" in query:
            speak("what do you want to search in youtube ?")
            query = takecommand().lower()

            # Check if the current version of chromedriver exists
            chromedriver_autoinstaller.install()
            driver = webdriver.Chrome()
            driver.get("https://www.youtube.com/")
            searchbox = driver.find_element_by_xpath('//*[@id="search"]')
            searchbox.send_keys(query)
            searchButton = driver.find_element_by_xpath(
                '//*[@id="search-icon-legacy"]/yt-icon')
            searchButton.click()
            searchButton1 = driver.find_element_by_xpath(
                '//*[@id="video-title"]/yt-formatted-string')

            searchButton1.click()

        elif "jokes" in query:
            My_joke = pyjokes.get_joke(language="en", category="neutral")
            speak(My_joke)

        elif "play video " in query:
            speak("select folder please")
            filename1 = filedialog.askopenfilename(

                initialdir="C:\\Users\\rishabh tiwari\\Videos\\",
                title="Select a File",
                filetypes=(("Text files",
                            "*.mp4*"),
                           ("all files",
                            "*.*")))
            os.startfile(filename1)

        elif "close" in query:
            root.destroy()
            break
        elif 'tell me time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strTime}")

        elif "who are you" in query:
            speak("I am your virtual assistant created by rishabh tiwari")

        elif "talk with assistance" in query:
            r2()
        else:
            pass


canvas = Canvas(root, width=500, height=500)
canvas.pack()
img = ImageTk.PhotoImage(Image.open(
    "C:\\Users\\rishabh tiwari\\Pictures\\pixel\\ar.jpeg"))
canvas.pack(side='top', fill='both', expand='yes')
canvas.create_image(0, 0, anchor=NW, image=img)
# frame
framegreen = Frame(root, bg="#000023")

framegreen.place(x=0, y=0, height=100, width=300)
# label
# title = Label(framegreen, text="let us search with new assisant call him smart rishu", font=("Impact", 15,), bg="white",
title = Label(framegreen, text="RISHI THE ROBO", font=(
    "Impact", 30, "italic"), bg="black", fg="blue").place(x=5, y=4)
#               fg="red").place(x=5, y=100)
title = Label(framegreen, text="2.0gegahertz processing rate", font=("Impact", 15, "italic"), bg="black", fg="blue").place(
    x=5, y=50)  # title = Label(framegreen, text="let us search with new assisant call him smart rishu", font=("Impact", 15,), bg="white",

# frame and button of click to talk with jarvis
f2 = Frame(root)
f2.place(x=790, y=500, height=60, width=260)

b1 = Button(f2, font=("Impact", 20, "italic"),
            text="click to talk with rishi", bg="Aqua", command=b1)
b1.place(x=790, y=510, height=10, width=5)
b1.pack()
# frame and button of QUIT


def lam1():
    root.destroy()
    os._exit(0)


f3 = Frame(root)
f3.place(x=1090, y=500, height=60, width=80)
# b2 = Button(f3, font=("Impact", 20, "italic"), text="QUIT", bg="Aqua", command=fun1)
# b2.place(x=650, y=560)
# b2.pack()
# new 7 and 8 button


# new1 and two window
def new1():
    neww1 = Toplevel(root)

    neww1.geometry("500x500")
    neww1.config(bg='aqua')
    l = Label(neww1, text="Analyze suspicious files and URLs to detect t\ny"
                          "pes of malware, automatically share them with th\n"
                          "e security communitywe"
                          "lcome to setting of ai").pack()


def new():
    neww = Toplevel(root)
    neww.title("wecome to setting")
    neww.geometry("500x500")
    neww.config(bg='aqua')
    l = Label(neww, text="welcome to setting of ai").pack()
    r = Button(neww, text="about this app", command=new1).pack()

    b2 = Button(neww, text="close this setting window it",
                command=lambda: neww.destroy())
    b2.pack()


def off():
    neww = Toplevel(root)
    neww.title("wecome to offline mode")
    neww.geometry("500x500")
    neww.config(bg='aqua')
    l = Label(neww, text="welcome to setting of ai").pack()
    r = Button(neww, text="about this app", command=new1).pack()

    b2 = Button(neww, text="close this setting window it",
                command=lambda: neww.destroy())
    b2.pack()


def offline1():
    # offlinetemp.offline()
    os.startfile(
        "C:\\Users\\rishabh tiwari\\PycharmProjects\\jarvis\\offlinetemp.py")


f4 = Frame(root)
f4.place(x=0, y=480, height=120, width=90)

b7 = Button(f4, text="SETTING", font=("Impact", 18, "italic"), bg="black",
            fg="red", pady=-30, command=new).pack(ipadx=0, ipady=0, padx=0, pady=0)
b8 = Button(f4, text=" offline", pady=-10, font=("Impact", 18,
            "italic"), bg="black", fg="red", command=offline1)
b8.pack()
##########
work = Label(root, text="WELCOME YOU ALL,MEET WITH RISHI ", font=("Impact", 25, "italic"), bg="black",
             fg="blue").place(x=500, y=70)
# clock


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(root, font=('calibri', 20, 'bold'),
            background='light blue', foreground='black')
lbl.place(x=1100, y=0, width=150)
time()
lbl1 = Label(root, text="set remainder", font=(
    'calibri', 20, 'bold'), background='light blue', foreground='black')
lbl1.place(x=1100, y=40, width=150)
# speak
work = Label(root, text="say \"open notepad,paint,cammand prompt and other application\"\t say \" open facebook\"\t "
                        "say \"open vedio/music/whatsapp\""
                        "\nsay \"open vedio in youtube\"\t  search in google\" to serch anything in google \t say \"search\"for wikipedia \t say \"close\"for quit",
             font=("cursive", 15,), bg="black",
             fg="Cyan").place(x=0, y=580, width=1260)  # bg="LightSlateGray
# some button
# f12= Frame(root)
# f12.place(x=790, y=600, height=60, width=260)
#
# b1 = Button(f12, font=("Impact", 10, "italic"), text="click to talk with jarvis", bg="Aqua", command=b1)
# b1.place(x=790, y=610, height=40, width=5)
# b1.pack()
# # frame and button of QUIT
# f13 = Frame(root)
# f3.place(x=1090, y=600, height=40, width=80)
# b2 = Button(f13, font=("Impact", 10, "italic"), text="QUIT", bg="Aqua", command=lambda: root.destroy())
# b2.place(x=650, y=660)
# b2.pack()
# exit(-1)
root.mainloop()
