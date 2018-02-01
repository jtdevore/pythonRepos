import xml.etree.ElementTree as ET
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from  tkinter import filedialog
from tkinter import simpledialog

def woTemplate():            
    master = Tk()
    variable = StringVar(master)
    variable.set("Select the main fault for billable event") # default value
    w = OptionMenu(master, variable, "Out of fuel", "Dead battery from misuse", "E-stop", "Frozen", "Damage", "E-brake unplugged", "OI unplugged")
    w.pack()

    def ok():
        print ('Billable event due to ' +  variable.get()) #gui.    
        master.withdraw()
        

    button = Button(master, text="OK", command=ok)
    button.pack()
    return variable.get()

    master.mainloop()
    master.quit()

vars2 =woTemplate()

print (vars2)