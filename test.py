import xml.etree.ElementTree as ET
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from  tkinter import filedialog
from tkinter import simpledialog


def repairTimeS(): #Stores user input variable repairSdate for later use
        root = Tk()
        root.withdraw()
        repairSdate = tkinter.simpledialog.askstring("Enter Truck  Number", "Enter Truck number")
        return repairSdate

vars1 = repairTimeS()

print (vars1)

