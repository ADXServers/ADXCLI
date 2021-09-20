#!/usr/bin/env python3
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
#from voiceAI import *
from voiceapi import *
#reco = speech_recognition.Recognizer()
#speaker = tts.init("espeak")
#voices = speaker.getProperty('voices')
#speaker.setProperty('voice',voices[11].id)
print("\033c", end="")
print("This Commandline was made by ADX")
print("Discord - ADX#0001")
print("Website - https://adxservers.xyz")
print("Commands list:\nLogout = logs out of the current user.\nvoiceAI = starts a voice assistant.\ncdir = Creates a directory\ncls = Clears all text from console.\nhelp = Lists all commands\ncreateuser = Creates a user\npasswd = Changes password of a user\nchangename = Changes the name of an user\nls = Lists all files inside a directory")
print("Warning! EVERYTHING IS CASE SENSITIVE.")



file = open("root.txt", "a")
devmode = False
usernamefound = False
passwordfound = False
loggedin = False
#SaveLogin = None
cmd = None

#Functions
def cls():
    print("\033c", end="")



#Commands ( DO NOT EDIT )

#Clear command

def clscmd():
    print("Clearing commandline")
    time.sleep(1)
    cls()
    print("Commandline cleared")
    cmdline()
    return
#if commandline == "Yes":
    #if cmd == "cls":
        #clscmd()
#/Clear command

#CDIR (Create Folder)

def cmdcdir():
    directory = input("Directory Name: ")
    dirpath = input("Directory Path: ")
    path = os.path.join(dirpath, directory)
    os.mkdir(path)
    print("Directory '%s' created" %directory)
    cmdline()
    return
#if commandline == "Yes":
    #if cmd == "cdir":
        #cmdcdir()
#/CDIR (Create Folder)

#HELP (Lists all commands)

def help():
    cls()
    print("This Commandline was made by ADX")
    print("Discord - ADX#0001")
    print("Website - https://adxservers.xyz")
    print("Commands list:\nLogout = logs out of the current user.\nvoiceAI = starts a voice assistant.\ncdir = Creates a directory\ncls = Clears all text from console.\nhelp = Lists all commands\ncreateuser = Creates a user\npasswd = Changes password of a user\nchangename = Changes the name of an user\nls = Lists all files inside a directory")
    cmdline()
    return
#if commandline == "Yes":
    #if cmd == "help":
        #help()
#/HELP (Lists all commands)

#Createuser (Creates user)
def createuser():
    arg1 = input("Username: ")
    if os.path.exists(arg1+".txt"):
        print(arg1+" already exists!")
        return
    else:
        file = open(arg1+".txt", "a")
        file.close()
        time.sleep(0.3)
        arg2 = input("Enter password: ")
        file = open(arg1+".txt", "w")
        file.write(arg2+"\n")
        time.sleep(0.5)
        cls()
        print("New user has been made!\nUsername: "+arg1+"\nPassword: "+arg2)
        return
#/Createuser (Creates user)

#Passwd (Changes password of an user)
def cpasswd():
    arg1 = input("User: ")
    if os.path.exists(arg1+".txt"):
        arg2 = input("New password: ")
        arg3 = input("Confirm password: ")
        if arg2 == arg3:
            file = open(arg1+".txt", "w")
            file.write(arg2)
            cls()
            print("Password Changed!\nUsername: "+arg1+"\nPassword: "+arg2)
            return
        else:
            print("Failed to confirm password.")
            return
#/Passwd (Changes password of an user)

#changename (changes name of an user)
def cname():
    arg1 = input("Current username: ")
    if os.path.exists(arg1+".txt"):
        arg2 = input("New name: ")
        arg3 = input("Confirm name: ")
        if arg2 == arg3:
            arg4 = "/users/"+arg1+".txt"
            arg5 = "/users/"+arg2+".txt"
            os.rename(arg4, arg5)
            print("Name changed!\nUsername: "+arg2)
            return
        else:
            print("Failed to confirm name!")
            return
#/changename (changes name of an user)

#Listdir
def listdir():
    arg1 = input("Directory [-C = Current directory]: ")
    if arg1 == "-C":
        start_path = '.'
        os.listdir(start_path)
        print(os.listdir(start_path))
        return
    elif os.path.exists(arg1):
        print(os.listdir(arg1))
        return
    else:
        print("Directory not found.")
        return
#/Listdir

#Logout
def logoutf():
    arg2 = input("Is your login saved? [Yes / No]: ")
    if arg2 == "Yes":
        SaveLogin = "No"
        os.remove("latest.txt")
        cls()
        print("Succesfully removed your saved login.")
        loggedin = False
        commandline = False
        print("\nThis command line will shutdown in 5 seconds!\n")
        time.sleep(1)
        print("\nThis command line will shutdown in 4 seconds!\n")
        time.sleep(1)
        print("\nThis command line will shutdown in 3 seconds!\n")
        time.sleep(1)
        print("\nThis command line will shutdown in 2 seconds!\n")
        time.sleep(1)
        print("\nThis command line will shutdown in 1 seconds!\n")
        time.sleep(1)
        print("\nGoodbye!\n")
        time.sleep(0.3)
        exit()
    else:
        arg1 = input("Write your password confirm logout: ")
        file = open(name+".txt", "r")
        if arg1 in file.read():
            cls()
            print("Succesfully logged out of your account.\n")
            print("\nThis command line will shutdown in 5 seconds!\n")
            loggedin = False
            commandline = False
            time.sleep(1)
            print("\nThis command line will shutdown in 4 seconds!\n")
            time.sleep(1)
            print("\nThis command line will shutdown in 3 seconds!\n")
            time.sleep(1)
            print("\nThis command line will shutdown in 2 seconds!\n")
            time.sleep(1)
            print("\nThis command line will shutdown in 1 seconds!\n")
            time.sleep(1)
            print("\nGoodbye!\n")
            time.sleep(0.3)
            exit()
#/Logout

def gAI():
    cls()
    reco = speech_recognition.Recognizer()
    speaker = tts.init("espeak")
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice',voices[3].id)
    speaker.setProperty("rate", 178)
    speaker.setProperty('volume', 0.2)
    g = True
    commandline = "No"
    #print("debug")
    file = open("current.txt", "w")
    file.write(name)
    file.close()
    mainf()
    

def cmdline():
    while True:
        cmd = input("Enter Command: ")

        if commandline == "Yes":
            if cmd == "cls":
                clscmd()
        if commandline == "Yes":
            if cmd == "cdir":
                cmdcdir()
        if commandline == "Yes":
            if cmd == "voiceAI":
                gAI()
        if commandline == "Yes":
            if cmd == "help":
                help()
        if commandline == "Yes":
            if cmd == "createuser":
                createuser()
        if commandline == "Yes":
            if cmd == "passwd":
                cpasswd()
        if commandline == "Yes":
            if cmd == "changename":
                cname()
        if commandline == "Yes":
            if cmd == "ls":
                listdir()
        if commandline == "Yes":
            if cmd == "logout":
                logoutf()
        if commandline == "Yes": 
           if cmd == "quit":
                exit()

    


#ROOT User
file = open("root.txt", "r")
#if "root" in file.readlines():
    #print("ROOT user found")
#else:
    #file = open("users/root.txt", "w")
    #file.write("root\n")
    #file.close()
    #file = open("users/root.txt", "r")
if "admin" in file.read():
    print("ROOT user found")
else:
    file = open("root.txt", "w")
    file.write("admin\n")
    file.close()


#Developer mode
if devmode == True:
    debug = input("debug: ")
    if debug == "dev":
        file = open("adx.txt", "w")
        file.write("adx\nadxvps")
        file.close()



#User management

if os.path.exists("latest.txt"):
        file.close()
        file = open("latest.txt", "r")
        print("Logged in as "+file.read())
        loggedin = True
else:
    name = input("Enter username:")
    if os.path.exists(name+".txt"):
        file = open(name+".txt", "r")
        file.close()
        usernamefound = True
        usernameid = name
        cls()
        print("Username " + usernameid + " found!")

    else:  
        print("Username not found! Exiting program") #file = open("users/"+createuser+".txt", "w")
        exit()

if usernamefound == True:
    passwd = input("Enter password:")
    file = open(name+".txt", "r")
    if passwd in file.read():
        cls()
        print("Logged in as " + name)
        loggedin = True
        SaveLogin = input("Do you want to save this login?\n [ Yes / No ]: ")
        if SaveLogin == "Yes":
            file.close()
            file = open("latest.txt", "a")
            file.close
            file = open("latest.txt", "w")
            file.write(name)
            


if loggedin == True:
    commandline = input("Do you want to start commandline? Yes/No:\n")
    if commandline == "Yes":
        cls()
        print("Opening commandline.")
        time.sleep(1)
        cls()
        print("This Commandline was made by ADX")
        print("Discord - ADX#0001")
        print("Website - https://adxservers.xyz")
        print("Commands list:\nLogout = logs out of the current user.\nvoiceAI = starts a voice assistant.\ncdir = Creates a directory\ncls = Clears all text from console.\nhelp = Lists all commands\ncreateuser = Creates a user\npasswd = Changes password of a user\nchangename = Changes the name of an user\nls = Lists all files inside a directory")
        cmdline()
    else:
        print("Logout Yes/No") #logout function







