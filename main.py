#main.py
from functions import *

#bob.speed(0)
turtle.tracer(0)

from random import randint

turtle.bgcolor("black")

turtle.colormode(255)


for times in range(100):
    x = randint(-500, 500)
    y = randint(-500, 500)
    
    
    #orange circle
    jump(x, y)
    #c = (255, 165, 0)
    bob.color("white")
    bob.begin_fill()
    bob.circle(3)
    bob.end_fill()

for times in range(100):
    x = randint(-500, 500)
    y = randint(-500, 500)
    
    
    #orange circle
    jump(x, y)
    #c = (255, 165, 0)
    bob.color("pink")
    bob.begin_fill()
    bob.circle(3)
    bob.end_fill()

for times in range(100):
    x = randint(-500, 500)
    y = randint(-500, 500)

    #orange circle
    jump(x, y)
    #c = (255, 165, 0)
    bob.color("purple")
    bob.begin_fill()
    bob.circle(3)
    bob.end_fill()


jump(200, 285)

bob.color("white")
bob.begin_fill()
bob.circle(55)
bob.end_fill()

jump(-200, 100)

bob.color("blue")
bob.begin_fill()
bob.circle(55)
bob.end_fill()

jump(100, 100)

bob.color("orange")
bob.begin_fill()
bob.circle(55)
bob.end_fill()

jump(200, -240)

bob.color("dark orange")
bob.begin_fill()
bob.circle(100)
bob.end_fill()








   
   




