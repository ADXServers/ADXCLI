import sys
import audioop
import os
import time
from typing import Mapping
import git
from git import Repo
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import os
import wikipedia

def mainf():
    def cls():
        print("\033c", end="")
    #speaker = tts.init('dummy')
    wname = "default"
    reco = speech_recognition.Recognizer()
    speaker = tts.init("espeak")
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice',voices[3].id)
    speaker.setProperty("rate", 160)
    speaker.setProperty('volume', 0.2)
    speaker.say("Welcome "+wname)
    speaker.runAndWait()
    cls()
    print("Welcome "+wname)
    speaker.say("This Voice Assistant was made by ADX")
    speaker.runAndWait()
    print("This Voice Assistant was made by ADX")
    print("Discord - ADX#0001")
    print("Website - https://adxservers.xyz")
    print("Voice Command list:\nWhat is my name = Says your name.\nChange my name = Changes your name.\nHello = Responds with a greeting\nCreate note = Creates a note\nWho is / What is / Wikipedia  = Finds information from wikipedia\nBye = Stops program\n")
    def speak(text):
        speaker.say(text)
        speaker.runAndWait
    def Hi():
        speaker.say("Hello")
        print("Hello")
        speaker.runAndWait()

    def bye():
        speaker.say("Goodbye!")
        speaker.runAndWait()
        sys.exit()
    def thx():
        speaker.say("Hello.")
        speaker.runAndWait()
    def create_note():
        global reco
        speaker.say("What do you want to write in your notes")
        speaker.runAndWait()

    

        

        d = False
        while not d:
            try:
                with speech_recognition.Microphone() as mic:
                    reco = speech_recognition.Recognizer()
                    reco.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = reco.listen(mic)
                    note = reco.recognize_google(audio)
                    note = note.lower()
                    print(note)
                    speaker.say("What do you want to name your file as")
                    speaker.runAndWait()
                    reco.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = reco.listen(mic)
                    fname = reco.recognize_google(audio)
                    fname = fname.lower()
                    print(fname)
                with open(fname, "w") as f:
                    f.write(note)
                    d = True
                    speaker.say(f"Your note has been written, name of your note is {fname}")
                    speaker.runAndWait()
            except speech_recognition.UnknownValueError:
                reco = speech_recognition.Recognizer()
                speaker.say("I did not understand.")
                speaker.runAndWait()

    def wiki():
        global reco
        speaker.say("What do you want to search from wikipedia")
        speaker.runAndWait()
        d = False
        while not d:
            try:
                with speech_recognition.Microphone() as mic:
                    reco = speech_recognition.Recognizer()
                    reco.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = reco.listen(mic)
                    winfo = reco.recognize_google(audio)
                    winfo = winfo.lower()
                    print(winfo)
                    d = True
                    speaker.say(wikipedia.summary(winfo))
                    print(wikipedia.summary(winfo))
                    speaker.runAndWait()
            except speech_recognition.UnknownValueError:
                reco = speech_recognition.Recognizer()
                print(winfo)
                speaker.say("Wikipedia page not found. Try again")
                print("Wikipedia page not found. Try again")
                speaker.runAndWait()
    def setname():
        global reco
        speaker.say("What do you want to set as your name")
        speaker.runAndWait()
        d = False
        while not d:
            try:
                with speech_recognition.Microphone() as mic:
                    reco = speech_recognition.Recognizer()
                    reco.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = reco.listen(mic)
                    wname = reco.recognize_google(audio)
                    wname = wname.lower()
                    file = open("current.txt", "w")
                    file.write(wname)
                    file.close()
                    print(wname+" Is now your new name")
                    d = True
                    speaker.say("Hello "+wname)
                    speaker.runAndWait()
            except speech_recognition.UnknownValueError:
                reco = speech_recognition.Recognizer()
                speaker.say("I did not understand.")
                speaker.runAndWait()

    def myname():
        file = open("current.txt", "r")
        wname = file.read()
        speaker.say("Your name is "+wname)
        speaker.runAndWait



    mappings = {
        'greeting' : Hi,
        'create_note' : create_note,
        'goodbye' : bye,
        'thanks' : thx,
        'wiki' : wiki,
        'setname' : setname,
        'name' : myname
    }
    AI = GenericAssistant('intents.json', intent_methods=mappings)
    #AI.train_model()
    AI.load_model()



    while True:
        try:
            with speech_recognition.Microphone() as mic:
                cls()
                print("This Voice Assistant was made by ADX")
                print("Discord - ADX#0001")
                print("Website - https://adxservers.xyz")
                print("Voice Command list:\nWhat is my name = Says your name.\nChange my name = Changes your name.\nHello = Responds with a greeting\nCreate note = Creates a note\nWho is / What is / Wikipedia  = Finds information from wikipedia\nBye = Stops program\n")
                speaker.runAndWait()
                reco.adjust_for_ambient_noise(mic, duration=0.5)
                audio = reco.listen(mic)
                message = reco.recognize_google(audio)
                message = message.lower()
                print(message)
                AI.request(message)
        except speech_recognition.UnknownValueError:
                speaker.say("Voice command not found. Try again")
                #speak("I didnt understand")
                print("Voice command not found. Try again")
                speaker.runAndWait()
