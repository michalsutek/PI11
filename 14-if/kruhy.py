import tkinter
canvas_width = 600
canvas_height = canvas_width
polomer = 10
pocet = canvas_width // (polomer * 2)

canvas = tkinter.Canvas(bg='white', width=canvas_width, height=canvas_height)
canvas.pack()

for i in range(pocet):  # riadky
    for j in range(pocet):  # stlpce
        x = j * polomer * 2
        y = i * polomer * 2
        if j == pocet // 2:
            farba = "red"
        else:
            farba = "white"
        canvas.create_oval(x - polomer, y - polomer, x + polomer, y + polomer, fill=farba)

tkinter.mainloop()