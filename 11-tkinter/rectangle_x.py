import tkinter

canvas = tkinter.Canvas()
canvas.pack()

x = 10
y = 10
d = 20
farba = "blue"
canvas.create_rectangle(x, y, x+d, y+d, fill=farba)
canvas.create_rectangle(x+d, y+d, x+2*d, y+2*d, fill=farba)

x = 6 * d
y = 10
farba = "red"
canvas.create_rectangle(x, y, x+d, y+d, fill=farba)
canvas.create_rectangle(x+d, y+d, x+2*d, y+2*d, fill=farba)

canvas.mainloop()