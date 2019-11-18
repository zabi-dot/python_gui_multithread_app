# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:40:42 2019

@author: macie
"""

import threading
import time
import datetime

from tkinter import *
from tkinter import scrolledtext # importujemy pole z tekstem

myTime = 1 # time is 1 sec

window = Tk()
 
window.title("Regulator komory termostatycznej")
window.geometry('800x480')  # ustawiamy rozmiar okna



def doit_measure(arg):
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        measure()
        time.sleep(1)
    print("Stopping as you wish.")


t = threading.Thread(target=doit_measure, args=("task",))
def buttonStartClicked():
    print("The START button was clicked!")
    if not t.is_alive():
        t.start()
    
        
    
    #t.start()
    
    
    
    
def buttonStopClicked():
    print("The STOP button was clicked!")
    t.do_run = False
    t.join()

    
def buttonCloseClicked():
    print("The CLOSE button was clicked!")
    window.destroy()    # zamknięcie programu
    
def buttonMeasureClicked():
    print("The MEASURE button was clicked!")

def measure():
    myDateTime = datetime.datetime.now() # odczytaj bieżący czas
    temp = 28.5 
    resist = 1152.4
    labelValueTemperature.configure(text = str(temp)) # pokaż wartosc w etykiecie
    labelValueResistance.configure(text = str(resist))
    napisRezystancja = 'R = ' + str(resist) + ' Ohm '
    napisTemperatura = 'T = ' + str(temp) + ' C '
    napisGodzina = myDateTime.strftime("%X")
    napis = napisRezystancja + napisTemperatura + napisGodzina + ' \n'
    textArea.insert(INSERT,napis)
    
    
    
    

#przyciski
#buttonStart = Button(window, text="Rozpocznij pomiary", command = buttonStartClicked)
buttonStart = Button(window, text="Rozpocznij pomiary", command = buttonStartClicked)
buttonStart.grid(column=0, row=0)

#buttonStop = Button(window, text="Koniec pomiarów", command = buttonStopClicked)
buttonStop = Button(window, text="Koniec pomiarów", command = buttonStopClicked)
buttonStop.grid(column=1, row=0)

buttonMeasure = Button(window, text="Zmierz temperaturę", command = buttonMeasureClicked)
buttonMeasure.grid(column=2, row=0)


buttonClose = Button(window, text="Zamknij program", command = buttonCloseClicked)
buttonClose.grid(column=3, row=0)

# pola z napisami
labelTemperature = Label(window, text="Temperature: ")
labelTemperature.grid(column=0, row=1)

labelValueTemperature = Label(window)
 
labelValueTemperature.grid(column=1, row=1)

labelResistance = Label(window, text="Resistance: ")
labelResistance.grid(column = 0, row = 2)

labelValueResistance = Label(window)
labelValueResistance.grid(column=1, row=2)

# pole tekstowe pokazujące historię wartoci
textArea = scrolledtext.ScrolledText(window,width=60,height=20)
textArea.grid(column=0, row=3, columnspan=4, rowspan=6)




window.mainloop()