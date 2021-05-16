from tkinter import *
from tkinter import colorchooser #submodule

def click():
    window.config(bg=colorchooser.askcolor()[1]) #this will change background color


window = Tk()
window.geometry("420x420")
button = Button(text="Click color", command=click)
button.pack()

window.mainloop()