from tkinter import *


def submit():
    print("The Temperature is: "+str(scale.get())+ " degrees Celsius")

window = Tk()

hotImage = PhotoImage(file='')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              length=450,
              orient=VERTICAL, #orientation of scale
              font=('Consolas', 20),
              tickinterval=10, #adds numeric indicators for values
              #showvalue =0 #hide the current value
              resolution=5, #increment of slider
              troughcolor='#69FAFF',
              fg='#FF1C00',
              bg='black',
              )
"""scale.set(((scale['from']-scale['to'])/2)+scale['to']) -> this places the scale indicator in the middle by default depending on the max-scale value provided"""
scale.pack()

button = Button(window, text='submit', padx=15, pady=8, command=submit)
button.pack()

coldImage = PhotoImage(file='')
coldLabel = Label(image=coldImage)
coldLabel.pack()





window.mainloop()