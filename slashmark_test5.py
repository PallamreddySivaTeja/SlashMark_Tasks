#main code
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import tkinter as tk
from tkinter import *
from tkinter import ttk

import google.generativeai as genai
l=""
# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
global t,label
t="your command:"
engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice

os.environ["GEMINI_API_KEY"] = "AIzaSyBp73xiV4Yvw78MKDcR5DYJCbrLd96SNeo"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-pro')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        label1.configure(text="Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing...")
        label1.configure(text="Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query
def work(t):
    query = take_command().lower()
    t+=query
    label.configure(text=t)

    print(query)
    if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
    elif 'are you' in query:
            speak("I am Siri developed by prabhas")
    elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
    elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
    elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
    elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
    elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
    elif 'open whatsapp' in query:
            speak("opening whatsapp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
    elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
    elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
    elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
    elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
    elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
    elif 'sleep' in query:
            exit(0)
    elif query !=None:
        #     te="tell me about "+query +"in 2 lines"
        #     response = model.generate_content(te)
        #     re =response['candidates'][0]['content']['parts'][0]['text']
        #     print(re)
        #     speak(re)
        te = "tell me answer " + query + " in 2 lines"
        response = model.generate_content(te)
        print(response)
        
        rep=str(response)
        loca=rep.find("{'text':")
        loca+=8
        stt=""
        while True:
                if rep[loca] =='}' and rep[loca+1]=="]":
                        break
                elif rep[loca]=="\\" and rep[loca+1]=="n":
                        loca+=1
                elif  rep[loca]=="." or rep[loca]=="," or rep[loca].isspace() or rep[loca].isalnum():
                        stt=stt+rep[loca] 
                loca+=1
        print(stt)
        speak(stt)
def print_selected_option():
    print(selected_value.get())
    if selected_value.get()=="female":
      i=1
      engine.setProperty('voice', voices[i].id)  # 1 for female and 0 for male voice
      engine.say("voice is female now")
    else:
      i=0
      engine.setProperty('voice', voices[i].id)  # 1 for female and 0 for male voice
      engine.say("voice is male now")
    
    
    engine.runAndWait()
def process(t):
        print_selected_option()
        work(t)
        
        

root = tk.Tk()
root.title("Virtual Assistant")
root.geometry("300x300")
style = ttk.Style()
style.configure("TButton", padding=20, relief="flat", background="#007bff", foreground="white", font=("Arial", 12))
label = tk.Label(root, text=t, font=("Arial", 16))
label.pack(pady=20)
selected_value = StringVar()
selected_value.set("female")  

options = ["male", "female"]

dropdown = OptionMenu(root, selected_value, *options)
dropdown.pack()
button1 = ttk.Button(root, text="change voice", command=lambda: print_selected_option(), style='Colorful.TButton')
button1.pack(pady=10, padx=20)
    
button2 = ttk.Button(root, text="Speak", command=lambda: work(t), style='Colorful.TButton')
button2.pack(pady=10)
label1 = tk.Label(root, text=l, font=("Arial", 16))
label1.pack(pady=20)
speak("Siri assistance activated ")
speak("How can i help you sir")

root.mainloop()
