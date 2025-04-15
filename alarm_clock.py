import time
import pygame
import datetime
import keyboard
from tkinter import *
import threading  # Import threading module

sound_file = 'tvoff.mp3'

def set_alarm():
    # Retrieve the alarm time from the Entry widget
    alarm_time = alarm_time_var.get()
    print(f"Alarm set for {alarm_time}")
    
    def check_alarm():
        is_running = True

        while is_running:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(current_time)
            time.sleep(1)

            if current_time == alarm_time:
                print("WAKE UP!!!")
                pygame.mixer.init()
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()

                
                is_running = False
                
    
    # Start the alarm check in a separate thread to prevent blocking the main thread
    threading.Thread(target=check_alarm, daemon=True).start()

if __name__ == "__main__":
    root = Tk()
    root.geometry('444x444')
    root.title("ALARM CLOCK")

    Label(root, text="Alarm Clock", font='comicsansms 18 bold').pack(anchor=CENTER)

    alarm_time_var = StringVar()

    Entry(root, textvariable=alarm_time_var, font='rubik 15 bold', fg='red').pack(anchor=CENTER)

    Button(root, text='Set Alarm', font='comicsansms 17 bold', fg='red', bg='yellow', command=set_alarm).pack(anchor=CENTER)

    Button(root,text="Stop Alarm", font='rubil 15 bold',fg='yellow',bg='red',command=quit).pack(anchor=CENTER)

    root.mainloop()

