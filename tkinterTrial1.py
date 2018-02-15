#! python3
#tkinter practice scripts

import tkinter as tk

#START TKINTER FRAME
window = tk.Tk()

#TITLE OF FRAME
window.title('my main window')

#SIZE OF FRAME
window.geometry('400x400')

#LABEL
title = tk.Label(text ='Hello world.  Welcome to TK trials!')
title.grid(column=0, row=0) 


#BUTTON
button1 = tk.Button(text = 'Click Me!', bg='red') #bg = background fyi
button1.grid(column=0, row=1)

#ENTRY FIELD
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=2)

#TEXT FIELD 
text_field1 = tk.Text(master=window, height=10, width=30)
text_field1.grid(column=0, row=3)

#END TKINTER FRAME AND MAKES WINDOW APPEAR ON SCREEN
window.mainloop()   
