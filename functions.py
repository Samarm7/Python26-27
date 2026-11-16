#myfunctions.py
import turtle

bob = turtle.Turtle()

def polygon(c, sides, distance):
    bob.color(c)
    angle = 360 / sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()

def polygon(sides, distance):
    angle = 360 / sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.left(angle)
    bob.end_fill()
 
    polygon(3,100)

def moon(x,y):
    jump(x,y)
    bob.width(10)
    bob.color("white")
    for times in range(10):
        polygon(3,20)
        bob.forward(30)
        bob.right(36)
    jump(16 + x,-75 + y)
    bob.width(20)
    bob.circle(30)
    
def jump(x, y):
    bob.penup()
    bob.goto(x, y)
    bob.pendown()

def rectangle():
    bob.forward(100)
    bob.right(90)
    bob.forward(40)
    bob.right(90)
    bob.forward(100)
    bob.right(90)
    bob.forward(40)
