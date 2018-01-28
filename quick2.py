#! python 3
#This is a practice of reglular expressions to find specific phrases within a block of text.

import re
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from  tkinter import filedialog
from tkinter import simpledialog



path = Tk()
path.filename =  filedialog.askopenfilename(initialdir = "Path Where the dialog should open first",title = "Select document to parse",filetypes = (("word files","*.docx"),("all files","*.*")))

    
    
    

with open(path.filename, 'r') as myfile:
    for line in myfile:
        m = re.search('^technician')
        if m is not None:
            m.group(0)
            print ('Found it.')
            break # Break out of the loop