"""radio button => similar to checkbox, but you can only select one from a group"""

from tkinter import *
snacks = ["pizza", "hamburger", "smokie"]

def order():
    if(x.get()==0):
        print("You've ordered Pizza")
    elif(x.get()==1):
        print("You've ordered Hamburger")
    elif(x.get()==2):
        print("You've ordered Sausage")
    else:
        print("huh!?")

window = Tk()
pizza_image = PhotoImage(file='pizza2.png')
hamburger_image = PhotoImage(file='frie-burger.png')
sausage_image = PhotoImage(file="sausages.png")

snack_images = [pizza_image, hamburger_image, sausage_image]


x = IntVar()

for index in range(len(snacks)):
    radio_button = Radiobutton(window,
                               text=snacks[index], #adds text to radio buttons
                               variable=x,  #groups radio buttons together if they share the same variable
                               value=index, #assigns each radiobutton a different value
                               padx=25, #adds padding on x-axis
                               font=('Impact', 15),
                               image=snack_images[index], #adds image to radio button
                               compound='left', #adds image & text (left-side)
                               #indicatoron=0, #eliminates circle indicators
                               #width=275 sets the width of radio buttons
                               command=order, #set the command of radio button to function
                               )
    radio_button.pack(anchor=W)
window.mainloop()