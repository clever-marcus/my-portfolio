#listbox ==> A listing of selectable text items within it's own container

from tkinter import *

def submit():
    food = []
    for index in my_box.curselection():
        food.insert(index,my_box.get(index))

    print("You have ordered: ")
    for index in food:
        print(index)


def add():
    my_box.insert(my_box.size(), entry_box.get())
    my_box.config(height=my_box.size())

def delete():
    for index in reversed(my_box.curselection()):
        my_box.delete(index)
    my_box.config(height=my_box.size())

window = Tk()

my_box = Listbox(window,
                 bg="#f7ffde",
                 font=('Constantia', 20),
                 width=12,
                 selectmode=MULTIPLE,
                 )
my_box.pack()

my_box.insert(1, 'pizza')
my_box.insert(2, 'hamburger')
my_box.insert(3, 'hotdog')
my_box.insert(4, 'samosa')
my_box.insert(5, 'sausage')

my_box.config(height=my_box.size())

entry_box = Entry(window)
entry_box.pack()

button = Button(window,
                text="Submit",
                font=('Consolas', 12),
                command=submit)
button.pack()

add_button = Button(window,
                    text="Add",
                    font=('Consolas', 12),
                    command=add)
add_button.pack()

delete_button = Button(window,
                    text="Delete",
                    font=('Consolas', 12),
                    command=delete)
delete_button.pack()


window.mainloop()