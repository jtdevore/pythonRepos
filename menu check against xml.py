import xml.etree.ElementTree as ET
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from  tkinter import filedialog
from tkinter import simpledialog
import openpyxl
import win32com.client as win32
import time

master = Tk()
master.filename =  filedialog.askopenfilename(initialdir = "Path Where the dialog should open first",title = "Select Event File",filetypes = (("xml files","*.xml"),("all files","*.*")))
print (master.filename)

global root
tree = ET.parse(master.filename)#this is where the file location to be parsed goes
root = tree.getroot()


alarmOptions = ['Unit out of fuel', 'Out of fuel','EWN FC Lockout', 'Dead battery from misuse','Estop', 'E-stop','FC stack frozen', 'Frozen','UI can-bus failure', 'OI unplugged','SYS brake rly open', 'E-brake unplugged','Other', 'damage']

variable = StringVar(master)
variable.set("Select the main fault for billable event") # default value
w = OptionMenu(master, variable, alarmOptions[1], alarmOptions[3], alarmOptions[5], alarmOptions[7], alarmOptions[13], alarmOptions[11], alarmOptions[9], alarmOptions[12])
w.pack()

def ok():
    print ('Billable event due to ' +  variable.get()) #gui button.
    master.destroy()
    
selection = variable.get()




button = Button(master, text="OK", command=ok)
button.pack()
master.wait_window(button)

for child in root:
    alarmDict = child.attrib      #This lists the alarm codes as dicts
    alarm_list = alarmOptions 
    for alarm in alarm_list:
        if alarm in alarmDict.values():
            print ('contains this alarm', alarm)
          
                
        else:
            print ('No valid operator error alarm found in event file')
            break

print (alarmOptions[1])
