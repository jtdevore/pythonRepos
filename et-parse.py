import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from  tkinter import filedialog


path = Tk()
path.filename =  filedialog.askopenfilename(initialdir = "Path Where the dialog should open first",title = "Select Event File",filetypes = (("xml files","*.xml"),("all files","*.*")))
print (path.filename)
path.withdraw()   
tree = ET.parse (path.filename)#this is where the file location to be parsed goes
root = tree.getroot()



for child in root:
    alarmDict = child.attrib      #This lists the alarm codes as dicts
    alarm_list = ['Out of Fuel', 'System Min Bat No Fc', 'alarm'] 
    for alarm in alarm_list:
        if alarm in alarmDict.values():
            print ('contains this alarm', alarm)
        else:
            print ('No valid operator error alarm found in event file')
            break
        

         
    


