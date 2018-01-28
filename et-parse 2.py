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



for data in root:
    dataDict =root.attrib
    fc1hours = (dataDict['FuelCellHours'])
    

    break

    
    


