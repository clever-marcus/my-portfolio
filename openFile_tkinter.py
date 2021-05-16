from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Marcus\\Documents\\python files\\marcus.txt",
                                          filetypes=("text files", ".txt"))
    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()
button = Button(text="Open File", command=openFile)
button.pack()


window.mainloop()