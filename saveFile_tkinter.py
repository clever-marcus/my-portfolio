from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Marcus\\Documents\\python files",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()

window = Tk()

button = Button(text="Save", command=saveFile)
button.pack()
text = Text(window, font=("Ink Free", 20),
            height=8,
            width=20,
            padx=20,
            pady=20,)
text.pack()


window.mainloop()