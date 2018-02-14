from  tkinter import filedialog

def file_save():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None:# asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = str(text.get(1.0, END)) # starts from `1.0`, not `0.0`
    f.write(text2save)
    f.close() # `()` was missing.
file_save()