import tkinter
sirka = 600
vyska = 600
canvas = tkinter.Canvas(width=sirka, height=vyska)
canvas.pack()
rozostup = 30
farba1 = "red"
farba2 = "blue"
hrubka = 2
for i in range(1, (sirka // rozostup) + 1):
    canvas.create_line(i * rozostup, 0, i * rozostup, vyska, fill=farba1, width=hrubka)
    farba1, farba2 = farba2, farba1
for i in range(1, (vyska // rozostup) + 1):
    canvas.create_line(0, i * rozostup, sirka, i * rozostup, fill=farba1, width=hrubka)
    farba1, farba2 = farba2, farba1

canvas.mainloop()
