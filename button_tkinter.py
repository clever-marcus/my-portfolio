from tkinter import *

"""button => you click it, then it does stuff"""

count = 0
def click():
    global count
    count += 1
    print(count)

window = Tk()
photo = PhotoImage(file='windows.png')
button = Button(window,
                text="Like",
                command=click,
                font=("Comic Sans", 20),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                image=photo,
                compound="right")
button.pack()





window.mainloop()