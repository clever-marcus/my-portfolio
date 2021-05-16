from tkinter import *
from tkinter import messagebox
#widgets = GUI elements: buttons, textboxes, labels, images
#windows = serves as a container to hold or contain these widgets
import tkinter as tk
window = Tk() #instantiate an instance of a window
window.geometry("420x300")
window.title("My GUI App")

icon = PhotoImage(file='mypic.png')
window.iconphoto(True, icon)
   #place window on computer screen, listen for events
lbl=Label(window, text="Enter the file name", fg='black', font=("Helvetica", 14))

lbl.place(x=0, y=10)

txtfld=Entry(window, text="", bd=3)
txtfld.place(x=0, y=50)
window.title('Hello Python')
window.geometry("300x200+10+10")

btn_1=Button(window, text="Ok", fg='black')
btn_2=Button(window, text="Cancel", fg='black')
btn_1.place(x=50, y=100)
btn_2.place(x=150, y=100)
window.title('Hello Python')
window.geometry("300x200+10+10")


def add():
    my_file = 'grocery.txt'

    def success():
        messagebox.showinfo('Success', 'File has been read')
        try:
            with open(my_file) as file:
                file.read()
        finally:
            open(my_file)
    def error():
        messagebox.showerror("Error", 'Possible bad file name Try Again!')

    if btn == my_file:
        success()
    else:
        error()
add()
window.mainloop()