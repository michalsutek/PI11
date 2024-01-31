import tkinter

canvas = tkinter.Canvas()
canvas.pack()


def kruh(x, y, r, farba):
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=farba)


def kruhy_riadok(x, y, pocet, r, farba):
    for i in range(pocet):
        kruh(x, y, r, farba)
        x = x + r * 2


def kruhy_stvorec(x, y, pocet, r, farba):
    for i in range(pocet):
        kruhy_riadok(x, y, pocet, r, farba)
        y = y + r * 2


kruhy_stvorec(50, 50, 5, 20, "blue")

canvas.mainloop()
