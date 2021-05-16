from tkinter import *

from tkinter import messagebox #This imports message box library

def click():
    #messagebox.showinfo(title="messagebox", message="Successfully installed Virus")
    #messagebox.showwarning(title="Warning", message="Virus in your PC!!!")
    #messagebox.showerror(title="error", message="something went wrong")

    """if messagebox.askokcancel(title="Ask ok cancel", message="Leave Page!"):
        print("page left :(")
    else:
        print("Page running")"""
    #***********************************************************************************************
    """if messagebox.askretrycancel(title="Ask retry cancel", message="loading failed! \nRetry?"):
        messagebox.showinfo(title='load retry', message="retrying...")
    else:
        messagebox.showerror(title='error', message="Loading Cancelled")"""
    #*******************************************************************************************
    """if messagebox.askyesno(title='user response', message="Do you have a girl?"):
        messagebox.showinfo(title='$$', message="Congratulations")
    else:
        messagebox.showerror(title='**', message="Quit bitching and look for one!!")"""
    #*****************************************************************************************
    """response = messagebox.askquestion(title='ask question', message='Do you like fish?')

    if(response == 'yes'):
        messagebox.showinfo(title='response', message="You're a real african person")
    else:
        messagebox.showerror(title='error', message="Why are you even in Africa!?")"""
    #********************************************************************************************

    answer = messagebox.askyesnocancel(title="mandatory question", message="Do you love coding?")
    if(answer == True):
        messagebox.showinfo(title='response', message="You're a computer nerd")
    elif(answer == False):
        messagebox.showinfo(title='response', message="Start loving it!!")
    else:
        messagebox.showerror(title='response', message="What are you even doing here!?")
window = Tk()

button = Button(window,
                text="Click Here",
                command=click)
button.pack()


window.mainloop()



