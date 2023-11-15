import tkinter
import random

canvas = tkinter.Canvas(width=600, height=500)
canvas.pack()
canvas.create_polygon(10, 10, 100, 10, 100, 100, fill="red", outline="black")

canvas.mainloop()