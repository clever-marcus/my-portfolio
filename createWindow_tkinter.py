from tkinter import *

def create_window():
    #new_window = Toplevel() #is a new window 'on top' of other windows, linked to a 'bottom' window
    my_window = Tk()           #Tk() => new independent window

    old_window.destroy()    #close out of old window

old_window = Tk()
Button(old_window, text="Create New File", command=create_window).pack()


old_window.mainloop()