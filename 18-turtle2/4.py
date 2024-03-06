import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.penup()
t1.setpos(-100, 0)
t1.pendown()

t2.penup()
t2.setpos(100, 0)
t2.pendown()

for i in range(4):
    t1.fd(50)
    t2.fd(50)
    t1.left(90)
    t2.left(90)

turtle.mainloop()