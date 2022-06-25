#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 15:17:01 2022

@author: riddhiekajain
"""

from tkinter import *
import speech_recognition as sr
root = Tk()
root.geometry("500x500")
def r_audio():
    speech_recogniser= sr.Recognizer()
    with sr.Microphone() as source:
        audio= speech_recogniser.listen(source)
        voice_data=''
        try: 
            voice_data= speech_recogniser.recognize_google(audio, language='en-in' )
        except sr.UnknownValueError:
            print('please repeat, I did not get that')
    print(voice_data)
    
r_audio()
root.mainloop()