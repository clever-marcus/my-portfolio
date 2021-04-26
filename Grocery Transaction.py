from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

window = Tk()


def myFuction():

    window.title("Grocery Transaction")
    lbl = Label(window, text="Enter the file name", fg='black', font=("Helvetica", 14))
    lbl.place(x=0, y=10)
    btn_1 = Button(window, text="Ok", fg='black')
    btn_2 = Button(window, text="Cancel", fg='black')
    btn_1.place(x=50, y=100)
    btn_2.place(x=150, y=100)

    def add():
        my_file = 'grocery.txt'

        def success():
            messagebox.showinfo('Success', 'File has been read')
            try:
                open(my_file, 'r')


        def error():
            messagebox.showerror("Error", 'Possible bad file name Try Again!')

        if btn_1 == my_file:
            success()
        else:
            error()
    add()


    window.mainloop()