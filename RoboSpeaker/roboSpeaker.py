# Project 1 : Robo Speaker
import os
from win32com.client import Dispatch
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created By Nitin")
    while True:
        speak = Dispatch('SAPI.SpVoice').Speak
        voiceSpeaker = input('Enter what you want me to speak: ')
        if voiceSpeaker == 'quit':
            voiceSpeaker = speak(f'Thanks for using Robo Speaker.')
            break
        speak = Dispatch('SAPI.SpVoice').Speak
        speak(f'{voiceSpeaker}')
