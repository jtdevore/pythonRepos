#! python 3
#This is a practice of reglular expressions to find specific phrases within a block of text.

import re
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from  tkinter import filedialog
from tkinter import simpledialog

def selectDoc():  #User selects file to parse
    path = Tk()
    path.filename =  filedialog.askopenfilename(initialdir = "Path Where the dialog should open first",title = "Select document to parse",filetypes = (("word files","*.docx"),("all files","*.*")))
    print (path.filename)
    path.withdraw()
    phraseFinder = re.compile(r'^technician')
    mo = phraseFinder.findall(path.filename)
    print (mo)
    
selectDoc()
