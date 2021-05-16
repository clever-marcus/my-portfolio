from tkinter import *

"""entry widget => textbox that accepts a single line of user input"""

def submit():
    username = entry.get()
    print(username)
    password_entry = entry.get()
    print(password_entry)

    #entry.config(state=DISABLED)
def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1, END)


window = Tk()
window.geometry("350x200")
window.title("Graphical User Interface")
window.config(background='#5cfcff')

label = Label(window,
              text="Username",
              font=('Arial', 10, 'bold'))
label.place(x=0, y=0)
password = Label(window,
                 text="Password",
                 font=('Arial', 10, 'bold'))
password.place(x=0, y=50)
entry = Entry(window,
              font=("Arial", 13),
              fg='black',
              bg="#5cfcff")
#entry.insert(0, 'marcus')
entry.pack()
password_entry = Entry(window,
                       font=("Arial", 13),
                       fg='black',
                       bg="#5cfcff",
                       show="*")
password_entry.place(x=80, y=50)
submit_button = Button(window, text="Submit", command=submit)
submit_button.place(x=290, y=0)

delete_button = Button(window, text="Delete", command=delete)
delete_button.place(x=290, y=100)

backspace_button = Button(window, text="Backspace", command=backspace)
backspace_button.place(x=150, y=100)







window.mainloop()