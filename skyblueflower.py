import turtle
turtle.speed(0)
def petal(radius, steps):
    turtle.circle(radius, 110, steps)
    turtle.left(70)
    turtle.circle(radius, 110, steps)
    turtle.left(70)

n = 5
s = 8
r = 100

turtle.fillcolor('skyblue')
turtle.pensize(3)
turtle.begin_fill()
turtle.setheading(0)
for i in range(n):
    petal(r, s)
    turtle.left(360/n)

turtle.end_fill()

turtle.penup()
turtle.color('green')
turtle.pensize(8)
turtle.goto(85, -200)
turtle.right(80)
turtle.forward(50)
turtle.pendown()
turtle.left(150)
turtle.circle(170, 70, 8)
turtle.hideturtle()
