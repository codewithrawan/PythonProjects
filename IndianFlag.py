# FOLLOW @CODEWITHRAWAN FOR MORE

import turtle
from turtle import*

screen = turtle.Screen()



t = turtle.Turtle()
t.speed(50)


t.penup()
t.goto(-300, 400)
t.pendown()
t.color("brown")
t.begin_fill()
t.forward(5)
t.right(90)
t.forward(1000)
t.right(90)
t.forward(5)
t.right(90)
t.forward(1000)




t.penup()
t.goto(-294, 400)

t.pendown()



t.color("orange")
t.begin_fill()
t.right(90)
t.forward(800)
t.right(90)
t.forward(167)
t.right(90)
t.forward(800)
t.end_fill()
t.left(90)
t.forward(167)


t.color("green")
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(800)
t.left(90)
t.forward(167)
t.end_fill()


t.penup()
t.goto(150, 150)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(70)
t.end_fill()


t.penup()
t.goto(140, 150)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()


t.penup()
t.goto(23, 142)
t.pendown()
t.color("navy")
for i in range(24):
	t.begin_fill()
	t.circle(3)
	t.end_fill()
	t.penup()
	t.forward(15)
	t.right(15)
	t.pendown()
	

t.penup()
t.goto(100, 150)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(80, 150)
t.pendown()
t.pensize(2)
for i in range(24):
	t.forward(60)
	t.backward(60)
	t.left(15)
t.penup()
goto(-100, -350)
turtle.pencolor("black")
t.pendown()
turtle.write(
    "JAI HIND",
    font=("Comic Sans", 24, "bold"))
t.penup()

turtle.goto(-170, -360)
turtle.write(
    "@codewithRawan",
    font=("Arial",6, "bold"))

turtle.done()

# FOLLOW @CODEWITHRAWAN FOR MORE
