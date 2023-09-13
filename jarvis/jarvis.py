import pyttsx3
import speech_recognition 
import pyaudio
import requests
from bs4 import BeautifulSoup 
import datetime
import os
import random
import webbrowser
import shutdown
from plyer import notification
import pyautogui
import speedtest
import Translator
import wikipedia



for i in range(3):
    a = input("Enter password to open jarvis :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("welcome, sir ! plz speak [wake up] to load me up")
        break
    elif (i==2 and a!=pw):
        exit()


    elif (a!=pw):
        print("try Again") 

from INTRO import play_gif
play_gif


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")
    except Exception as e:
        print("say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarm.txt","a")
    timehere.write(query)
    timehere.close()    
    os.startfile("alarm.py")

if __name__== "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from me import me
            me()
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("ok sir you can call me anytime")
                    break
                ################ jarvis: the trilogy 2.0 ###############################
            
                elif "change password" in query:
                    speak("what's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"your new password is{new_pw}")

                elif  "schedule my day" in query:
                    tasks = []#Empty list    
                    speak("Do you want to clear old tasks (plz speak Yes or No)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of taska :-"))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter The task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}.{tasks[i]}\n")
                            file.close

                    if "no" in query:
                        tasks = []
                        no_tasks = int(input("Enter the number of tasks: "))
                        for i in range(no_tasks):
                            task = input("Enter the task: ")
                            tasks.append(task)
                            with open("tasks.txt", "a") as file:
                                 file.write(f"{i}.{task}\n")

                elif "show my schedule" in query:        
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    
                    notification.notify(
                    title = "My schedule :-",
                    sendMessage = content,
                    timeout = 15)

                elif "focus mode" in query:    
                    a = (input("Are you sure that you want to enter focus mode :-[1 for yes / 2 for no]"))
                    if (a==1):
                        speak("Entering the focus mode....")
                        os.startfile("C:\\Users\\DELL\\Desktop\\jarvis\\FocusMode.py")
                        exit()

                    else:    
                        pass

                elif "show my focus" in query:    
                    from Focus_Graph import focus_graph
                    focus_graph()

                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)


                elif "open" in query:
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")
                
                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576
                    download_net = wifi.download()/1048576
                    print("wifi download speed is ",download_net)
                    print("wifi Upload Speed is", upload_net)
                    speak(f"wifi download speed is{download_net}")
                    speak(f"wifi upload speed is{upload_net}")

                elif "ipl score" in query:     
                    from plyer import notification
                    import requests
                    from bs4 import BeautifulSoup
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                         title = "IPL SCORE :- ",
                         message = f"{team1} : {team1_score} \n {team2} : {team2_score}",
                        timeout = 15 )


                    

                elif "play a game" in query:    
                    from game import game_play
                    game_play()

                elif "screenshot" in query:    
                    import pyautogui
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")

                elif "click my photo" in query:    
                    pyautogui.press("super")
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                

                ##############################################################
                elif "hello" in query:
                    speak("Hello sir, how are you?")
                elif "i am fine " in query:
                    speak("that's great, sir")  
                elif "how are you" in query:
                    speak("Perfect, sir")   
                elif "thank you" in query:
                    speak ("you are welcome, sir") 

                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) 
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("https://www.youtube.com/watch?v=FIeJs8aeR3Y")
                
                    
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()

                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                elif "open" in query:
                    from app import openappweb  
                    openappweb(query)
                elif "close" in query:
                    from app import closeappweb    
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

                elif "calculate" in query:
                    from Calculaternumber import wolframalpha
                    from Calculaternumber import Calc
                    query = query.replace("calculater","")
                    query = query.replace("jarvis","")
                    Calc(query)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage 
                    sendMessage()




                elif "temperature" in query:
                    search = "temperature in haryana"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div" , class_ = "BNeawe").text
                    speak(f"current{search} is {temp}") 

                elif  "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("set the tme")
                    a = input("please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")

                elif "weather" in query:
                    search = "temperature in haryana"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    date = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div" , class_ = "BNeawe").text
                    speak(f"current{search} is {temp}") 

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir the time is {strTime}")

                elif "finally sleep" in query:
                    speak("Going to sleep,sir")    
                    exit()

                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())
                
                elif "shutdown the system" in query:
                    speak("Are you sure you want to shutdown?")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                     os.system("shutdown /s /t 1")
                elif shutdown == "no":
                    break