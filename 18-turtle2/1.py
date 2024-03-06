import turtle

t = turtle.Turtle()
turtle.delay(0)


def stvorec(dlzka):
    for i in range(4):
        t.fd(dlzka)
        t.rt(90)


def n_uholnik(n, dlzka):
    for i in range(n):
        t.fd(dlzka)
        t.lt(360/n)



# stvorec(20)
for n in range(3, 30):
    n_uholnik(n, 50)

turtle.mainloop()