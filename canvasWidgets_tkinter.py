#canvas => widget that is used to draw graphs, plots, images in a window

from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)
"""blue_line = canvas.create_line(0,0,500,500, fill="blue", width=5)
red_line = canvas.create_line(0,500,500,0, fill="red", width=5)
rectangle = canvas.create_rectangle(50,50,250,250, fill="purple")
coordinates = [250,0, 500,500, 0,500]
triangle = canvas.create_polygon(coordinates, fill="DodgerBlue", outline="black", width=2)
canvas.create_arc(0,0,500,500, fill="DodgerBlue", outline="black", width=2, style=PIESLICE, start=120, extent=180)"""

canvas.create_arc(0,0,500,500,fill="red", extent=180, width=10)
canvas.create_arc(0,0,500,500,fill="white", extent=180, start=180, width=10)
canvas.create_oval(190,190,310,310, fill="white", width=10)

canvas.pack()


window.mainloop()