from lucidlib import *
import tkinter
import speech_recognition as sr
import RPi.GPIO as GPIO
import subprocess as cmdLine
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
def speak(textts, vce):
    cmdLine.run("clear")
    if vce == "girl":
        try:
            command = "espeak -ven-us+f4 -s170 " + chr(34) + textts+ chr(34)
            cmdLine.run(command, shell=True)
            cmdLine.run("clear")
        except:
            print("no")
    elif vce == "boy":
        try:
            command = "espeak -ven-us+f9 -s169 " + chr(34) + textts + chr(34)
            cmdLine.run(command, shell=True)
            cmdLine.run("clear")
        except:
            print("no")
            
    elif vce == "bot":
        try:
            command = "espeak -ven-us+f9 -s140 -p0 " + chr(34) + textts + chr(34)
            cmdLine.run(command, shell=True)
            cmdLine.run("clear")
        except:
            print("no")
GPIO.output(18, True)
GPIO.output(15, False)
GPIO.output(14, False)
r = sr.Recognizer()
micph = sr.Microphone()
def listen2():
    with micph as source:
        print("You can now speak")
        GPIO.output(18, True)
        GPIO.output(15, True)
        GPIO.output(14, True)
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source)
        print("Translating your speech...")
        GPIO.output(18, False)
        GPIO.output(15, False)
        GPIO.output(14, False)
        text = r.recognize_houndify(audio, client_id="4fs7kqkegfXPQGG161IuiA==", client_key="JoFPmS30niFiqeR92-WsfuAlixrQOyXND38GhQK1oqCHFOKbgUnmJyCmUCICA_lxhQ83sYrxuwM0wKRzQuBfEw==")
        print(text)
        return(text)
def listen():
    with micph as source:
        print("You can now speak")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        print("Translating your speech...")
        GPIO.output(18, False)
        GPIO.output(15, False)
        GPIO.output(14, True)
        text = r.recognize_houndify(audio, client_id="4fs7kqkegfXPQGG161IuiA==", client_key="JoFPmS30niFiqeR92-WsfuAlixrQOyXND38GhQK1oqCHFOKbgUnmJyCmUCICA_lxhQ83sYrxuwM0wKRzQuBfEw==")
        print(text)
        return(text)
def listenforlucid():
    GPIO.output(15, True)
    GPIO.output(14, True)
    GPIO.output(18, True)
    text = listen2()
    if "lucid" in text:
        GPIO.output(15, True)
        GPIO.output(14, False)
        GPIO.output(18, False)
        speak("what can I do for you?", "boy")
        text = listen()
        print(text)
        if "drink" or "pump" in text:
            speak('What do you want', "boy")
            text = listen()
            print(text)
            if 'sparkling' and "ice" in text:
                speak("pumping sparkling ice", "boy")
                GPIO.output(18, True)
                GPIO.output(15, False)
                GPIO.output(14, False)
                pump("sparkling ice")
                speak("Enjoy.","boy")
                listenforlucid()
            else:
                speak("Sorry, I did'nt catch that.", "boy")
                listenforlucid()
    else:
        listenforlucid()
listenforlucid()