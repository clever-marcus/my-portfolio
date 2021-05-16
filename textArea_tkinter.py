# text widget => functions like a text area, you can enter multiple lines of text from tkinter import *
from tkinter import *

def submit():
    user_input = text.get("1.0", END)
    print(user_input)


window = Tk()
text = Text(window,
            bg="light yellow",
            font=("Ink Free", 20),
            height=8,
            width=20,
            padx=20,
            pady=20,
            fg="DodgerBlue")
text.pack()

button = Button(window,text="Submit", command=submit)
button.pack()

window.mainloop()

