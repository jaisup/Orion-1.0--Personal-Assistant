import pyttsx3 
import datetime 
import speech_recognition as sr 
import wikipedia 
import smtplib
import webbrowser as wb
import os
import pyautogui  
import psutil 
import pyjokes 
import random
import operator
import json
import time
from urllib.request import urlopen
import requests
import wolframalpha

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%H:%M:%S")
    speak("the time is")
    speak(Time)
    
    
def date():
    year = (datetime.datetime.now().year)
    month = (datetime.datetime.now().month)
    date = (datetime.datetime.now().day)
    speak("the date is")
    speak(date)
    speak(month)
    speak(year)
    

def wishme():
    speak("Hey jai! what can I help you with today?")
    

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-pk')
        print(query)
        
    except Exception as e:
        print(e)
        print("Did not quiet catch that, could you please repeat")
        speak("Did not quiet catch that, could you please repeat")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail 
    server.login('i.am.cool713@gmail.com', 'enter your own lol')
    server.sendmail('Your email', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save('D:/Python projects/Orion/Orion screenshots/sc1.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

def Introduction():
    speak("I am ORION 2.0 , Personal AI assistant , "
    "I am created by jai , "
    "and I can help in various things such as , "
    "Help find something for you on the Internet , "
    "or grab definitions for you from wikipedia , "
    "In layman terms , I can try to make your life a bed of roses , "
    "Where you just have to command me , and I will do it for you! ")

def Creator():
    speak("Jai is a super cool person ,"
    "He has a passion for anything that makes him curious,"
    "If you are facing any problem regarding the 'Orion', He will be glad to help you ")




    
if __name__ == '__main__':


    clear = lambda: os.system('cls') 
    clear()

    wishme()
    
    while True:
        query = TakeCommand().lower()
 

        if 'time' in query:
            time_()

        elif 'date' in query:
            date()

        elif 'how are you' in query:
            speak("I might need a little oil change but other than that I am perfectly fine")


        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        
        elif 'open youtube' in query:
            speak("What should I search for?")
            Search_term = TakeCommand()
            speak("opening Youtube\n")
            wb.open("https://www.youtube.com/results?search_query="+Search_term)
            time.sleep(5)

        elif 'google' in query:
            speak("What should I search for?")
            Search_term = TakeCommand()
            speak("opening google\n")
            wb.open('https://www.google.com/search?q='+Search_term)
        
       
        
        elif "who am i" in query:
            speak("If you can talk, then definitely you are a human")

        elif "who made you" in query:
            speak("jai did, the rest on why is a secret... wink wink")

        

        elif 'what is love' in query:
            speak("It is 7th sense that destroy all other senses , "
            "And I think it is just a mere illusion , "
            "It is a waste of time")


        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                speak("Please enter the Recievers email id?")
                reciept = input("Enter recieptant's email: ")
                to = (reciept)
                sendEmail(to,content)
                speak(content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                speak("Unable to send the email.")

        elif 'open chrome' in query:
            speak("What should I search ?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = TakeCommand()
            speak("opening chrome")
            wb.get(chromepath).open_new_tab(search+'.com')

        # elif 'log out' in query:
        #     os.system("shutdown -l")
        # elif 'restart' in query:
        #     os.system("shutdown /r /t 1")
        # elif 'shutdown' in query:
        #     os.system("shutdown /s /t 1")
        
        
        
        elif 'play songs' in query:
            video ='Videos'
            audio = 'Music'
            speak("What songs should i play? Audio or Video")
            ans = (TakeCommand().lower())
            while(ans != 'audio' and ans != 'video'):
                speak("I could not understand you. Please Try again.")
                ans = (TakeCommand().lower())
        
            if 'audio' in ans:
                    songs_dir = audio
                    songs = os.listdir(songs_dir)
                    print(songs)
            elif 'video' in ans:
                    songs_dir = video
                    songs = os.listdir(songs_dir)
                    print(songs)
                
            speak("select a random number")
            rand = (TakeCommand().lower())
            while('number' not in rand and rand != 'random'):                     
                speak("I could not understand you. Please Try again.")        
                rand = (TakeCommand().lower())

            if 'number' in rand:
                    rand = int(rand.replace("number ",""))
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue                                                
            elif 'random' in rand:
                    rand = random.randint(1,219)
                    os.startfile(os.path.join(songs_dir,songs[rand]))
                    continue
                
            
        elif 'remember' in query:
            speak("What should I remember ?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'what do you remember' in query:
            remember =open('memory.txt', 'r')
            speak("You asked me to remeber that"+remember.read())
        
        
        elif "write a note" in query:
            speak("What should i note down, sir")
            note = TakeCommand()
            file = open('note.txt', 'w')
            speak("Sir, Should i include date and time")
            dt = TakeCommand()
            if 'yes' in dt or 'sure' in dt:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak('done')
            else:
                file.write(note)
                
        elif "show note" in query:
            speak("Showing Notes")
            file = open("note.txt", "r")
            print(file.read())
            speak(file.read()) 

        elif "weather" in query: 
			
		
            api_key = "7e6229f2275d2390a70c77ee2e5b4827"
            base_url = "http://api.openweathermap.org/data /2.5/weather?q="
            speak(" which city ")
            city_name = TakeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
            
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
                
            else:
                speak(" City Not Found ") 





        elif 'news' in query:
            
            try:

                jsonObj = urlopen("https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d90f4f7bb6ce443bb893a0afc61fb4fa")
                data = json.load(jsonObj)
                i = 1
                
                speak('here are some top news from the world')
                print('''=============== TOP HEADLINES ============'''+ '\n')
                
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
                    
            except Exception as e:
                print(str(e)) 


                
        
        elif 'take screenshot' in query:
            screenshot()
            speak("Done!")    

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'tell me about yourself' and 'who are you' in query:
            Introduction()

        elif 'tell me about jai' and 'creator' in query:
            Creator()
        
        #show location on map
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            wb.open("https://www.google.com/maps/place/" + location + "")

        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about that, might be a little weird")
            
        elif "i love you" in query:
            speak("no you dont")
        

        #calculation
        elif "calculate" in query:
            
            app_id = "XRW98Y-22KXKYKWX8"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer) 

        



        #General Questions
        elif "what is" in query or "who is" in query: 
			
			# Use the same API key 
			# that we have generated earlier
            client = wolframalpha.Client("XRW98Y-22KXKYKWX8")
            res = client.query(query)
            
            try:
                print (next(res.results).text)
                speak (next(res.results).text)
            except StopIteration:
                print ("No results") 




        #sleep-time
        elif "don't listen" in query or "stop listening" in query:
            speak("how many seconds do you want me to stop listening for?")
            a = int(TakeCommand())
            time.sleep(a)
            print(a)

        #quit
        elif 'offline' in query or "thank you" in query:
            speak("Hope you have a good day jai, goodbye")
            quit()