#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class
#from tkinter import *
import pyautogui
import speech_recognition as sr
#import win32api
#import win32con
import time
import pyaudio
import keyboard
import winsound

snd_speak = "C:\\Users\\jacob\\Downloads\\speak.wav"
snd_ready = "C:\\Users\\jacob\\Downloads\\ready.wav"
snd_done = "C:\\Users\\jacob\\Downloads\\done.wav"
snd_fail = "C:\\Users\\jacob\\Downloads\\fail.wav"

#root = Tk()
#button = Button(root, text = "get_speech")
#button.pack()

'''
def wait_for_click():
    while True:
        if (win32api.GetAsyncKeyState(win32con.VK_LBUTTON)) < 0:
            break
        time.sleep(0.01)
'''

def get_speech():
    winsound.PlaySound(snd_ready, winsound.SND_ASYNC)
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
        #print("click somewhere")
        #wait_for_click()
        print("Say something!")

        # recognize speech using Google Speech Recognition
        try:
            audio = r.listen(source,timeout=3,phrase_time_limit=30)
            string = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said: " + string)
            pyautogui.typewrite(string)
            winsound.PlaySound(snd_speak, winsound.SND_ASYNC)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            winsound.PlaySound(snd_fail, winsound.SND_ASYNC)
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            winsound.PlaySound(snd_fail, winsound.SND_ASYNC)
        except sr.WaitTimeoutError as k :
            print("time out")    #error handler for time out error
            winsound.PlaySound(snd_fail, winsound.SND_ASYNC)



        
#myPyAudio=pyaudio.PyAudio()
#print("Seeing pyaudio devices:",myPyAudio.get_device_count())

keyboard.add_hotkey('shift+control+z', get_speech)
keyboard.wait('shift+esc')

#button.configure(command=get_speech)
#root.mainloop()
