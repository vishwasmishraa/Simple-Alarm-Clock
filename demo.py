from tkinter.ttk import *
from tkinter import *
from pygame import *

from datetime import *
import sys
sys.setrecursionlimit(10000)


from pygame import mixer
from time import sleep
#window
window= Tk()
window.title("")
window.geometry('350x200')



def sound_alarm():
    mixer.music.load('alarm2.mp3')
    mixer.music.play()
mixer.init

def sound_alarm():
    while True:
        control = 1
        print(control)
        alarm_hour='05'
        alarm_minute='19'
        alarm_second='00'
        alarm_period='PM'.upper()

        now = datetime.now()
        
        hour= now.strftime('%I')
        minute= now.strftime("%M")
        second= now.strftime("%S")
        period=now.strftime("%p")

        if control== 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_second == second:
                            print("Time to take a break...")
                            sound_alarm()
        sleep(1)

mixer.init()
sound_alarm()

window.mainloop()