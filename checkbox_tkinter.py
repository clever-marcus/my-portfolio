from tkinter import *

count = 0
def display():
    if(x.get()==1):
        global count
        count += 1
        print(count)
    else:
        print("You don't Agree :(")
window = Tk()

x= IntVar()
check_button = Checkbutton(window,
                           text="Check it",
                           variable=x,
                           onvalue=1,
                           offvalue=0,
                           command=display,
                           font=('Arial', 15),
                           fg="#00FF00",
                           bg="black",
                           activeforeground="#00FF00",
                           activebackground="black",
                           padx=25,
                           pady=10)
check_button.pack()


window.mainloop()