from tkinter import *

master = Tk()

variable = StringVar(master)
variable.set("one") # default value

w = OptionMenu(master, variable, "one", "two", "three")
w.pack()

def ok():
    print ('value is ' +  variable.get())
    master.withdraw()

button = Button(master, text="OK", command=ok)
button.pack()


mainloop()
