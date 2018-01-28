import tkinter
from tkinter import simpledialog

root = tkinter.Tk()
root.withdraw()
var = tkinter.simpledialog.askstring("Name prompt", "enter your name")
print (var)

