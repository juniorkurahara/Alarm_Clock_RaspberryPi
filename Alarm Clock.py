# Importações
from tkinter import *
import datetime
import time
import winsound

# Loop do Alarme
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("A data do alarme é: ", date)
        print(now)
        if now == set_alarm_timer:
            print('Hora de acordar!')
            winsound.PlaySound('sound.wav', winsound.SND_ASYNC)
            break
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

# Graphic User Interface (GUI) - tkinter

clock = Tk()
clock.title("Despertador")
clock.geometry("400x200")
time_format=Label(clock, text= "Formato: 24 horas", fg="red",bg="black",font="Arial").place(x=120,y=120)
addTime = Label(clock,text = "Hora  Min   Seg",font=60).place(x = 140)
setYourAlarm = Label(clock,text = "Quando deseja despertar?",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=10, y=29)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=140,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=180,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 10).place(x=230,y=30)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =140,y=70)
clock.mainloop()

# Fonte: https://data-flair.training/blogs/alarm-clock-python/