import turtle
t = turtle.Turtle()
t.speed(0)
def stvorec(dlzka):
    for i in range(4):
        t.forward(dlzka)
        t.left(90)

for i in range(100):
    stvorec(100)
    t.left((360/100))

turtle.mainloop()