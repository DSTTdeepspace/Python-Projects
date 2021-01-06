import subprocess

import sounddevice as sd 

import soundfile as sf 

import datetime

import re

from tkinter import *

import wolframalpha

import pyttsx3

import tkinter

from bs4 import BeautifulSoup

import subprocess

import json

import random

import operator

from googlesearch import search

import speech_recognition as sr

import datetime

import wikipedia

from pyowm import OWM

import webbrowser

import os

import winshell

import pyjokes

import feedparser

import smtplib

import ctypes

import time


import requests

import shutil

import gtts

from twilio.rest import Client

from clint.textui import progress

from ecapture import ecapture as ec

from bs4 import BeautifulSoup

import win32com.client as wincl

from urllib.request import urlopen

import playsound

import time

#voice

voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voice_id)

# speak command

def speak(text):
   
    engine.say(text)
    
    engine.runAndWait()
    
#wishing function
 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>= 0 and hour<12:
        
        speak("Good Morning!")
  
    elif hour>= 12 and hour<18:
        
        speak("Good Afternoon!")   
  
    else:
        
        speak("Good Evening!")  
  
    assname =("This EDITH here")
    
    speak("Hope you had a nice day")
    
    speak(assname)
    
#username

def usrname():
    speak("What should i call you")
    
    uname = input('Enter a suitable name: ')
    
    speak("Welcome")
    
    speak(uname)
    
    print("Welcome Mr.", uname) 
    
    speak("How can i Help you")
    
#getting the board ready

clear = lambda: os.system('cls')

clear()

wishMe()

usrname()    

for i in range (0, 10000+1):
    
    query = input('Enter your query: ').lower()

    #wikipedia
    
    if 'wikipedia' in query:
                speak('Searching Wikipedia...')
            
                t = input("enter your search term: ")
                
                query = query.replace("wikipedia", t)
                
                results = wikipedia.summary(query, sentences = 3)
                
                speak("According to Wikipedia")
                
                print(results)
                
                speak(results)
                
    #youtube
                
    elif 'open youtube' in query:
        
                speak("Here you go to Youtube\n")
            
                webbrowser.open("https://www.youtube.com/")
     
    #google

    elif 'open google' in query:
        
                speak("Here you go to Google\n")
            
    #time
            
    elif 'time' in query:
        
                strTime = datetime.datetime.now().strftime("% H:% M:% S") 
            
                speak(f"Sir, the time is {strTime}")
                
                webbrowser.open("google.com")
    
    #stackoverflow
    
    elif 'open stackoverflow' in query:
        
                speak("Here you go to Stack Over flow. Happy coding!")
            
                webbrowser.open("stackoverflow.com") 
    
    #how are you?

    elif 'how are you' in query:
                speak("I am fine, Thank you")
            
                speak("How are you, Sir")
                
                query_sub1 = input('enter here: ')
                
                if 'bad' in query or 'depressed' in query or 'sad' in query or 'alone' in query:
                    speak('Bad times have an end and so your cloud will also have a silver lining')
                else :
                    speak('Good to know that Sir.')
                    
    # what is your name?

    elif "what's your name" in query or "What is your name" in query:
        
                speak("My friends call me")
            
                speak('EDITH')
                
                print("My friends call me EDITH")
                
    #exit

    elif 'exit' in query:
                speak("Thanks for giving me your time")
                break
                
    #who made you?
    
    elif "who made you" in query or "who created you" in query: 
        
                speak("KGP")
       
    #joke

    elif 'joke' in query:
        
                import pyjokes
            
                speak(pyjokes.get_joke())
               
    #who are you?, Why you?

    elif "who are you" in query:
        
                speak("I'm Batman")

    elif "why you" in query:
        
                speak("It's not up to you")
    #open powerpoint

    elif 'power point' in query:
                speak("opening Power Point presentation")
            
                power = r(input("enter the location: "))
                
                os.startfile(power)
    #lock pc
    
    elif 'lock window' in query:
                speak("locking the device")
            
                ctypes.windll.user32.LockWorkStation()
                
     #search
                
    elif 'search' in query:
                try: 
                    from googlesearch import search 
                except ImportError: 
                    print("No module named 'google' found") 

                # to search 
                output = re.search('search (.*)', query)

                for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
                    print(j) 

                
     #empty recycle bin
    
    elif 'empty recycle bin' in query:
                winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            
                speak("Recycle Bin Recycled")
    #shut down pc
    
    elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
            
                subprocess.call('shutdown / p /f')
                
     #photo
 
    elif "camera" in query or "take a photo" in query:
        
                ec.capture(0, "Edith Cam ", "img.jpg")
            
    #who is....?

    elif "who is" in query:
        
        x = input("enter the first search term: ")
        
        y = input("enter the second search term: ")
        
        webbrowser.open("https://www.google.com/search?gs_ssp=eJzj4tDP1TcwSrHMNmD04k1JLMtMUUhKTc7OSMwFAFt2B8M&q="+x+"+"+y+"&oq="+x+"+&aqs=chrome.2.69i57j46i433l2j46i131i433l2j46i433j69i60l2.3101j0j7&sourceid=chrome&ie=UTF-8")

     #what is
    
    elif "what is" in query:
        
        x = input("enter the first search term: ")
        
        y = input("enter the second search term: ")
        
        webbrowser.open("https://www.google.com/search?q=what+is+"+x+"+"+y+"&oq=what+is+"+x+"+"+y+"&aqs=chrome..69i57j0i13i457j0i13l6.6382j0j7&sourceid=chrome&ie=UTF-8")
        
    #weather
    
    elif 'current weather' or 'temperature' in query:
        
        reg_ex = re.search('current weather in (.*)', query)
        
        if reg_ex:
            
            city = reg_ex.group(1)
            
            owm = OWM('ab0d5e80e8dafb2cb81fa9e82431c1fa')
            
            mgr = owm.weather_manager()
            
            observation = mgr.weather_at_place(city) 
            
            weather = observation.weather
            
            k = weather.detailed_status 
            
            x = weather.temperature(unit='celsius')
            
            speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
            
            print('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
            

