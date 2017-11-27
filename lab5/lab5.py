from turtle import Turtle
from turtle import *
colormode(255)
import random
import turtle

def r():
    turtle.hideturtle()
    for i in range(6):
        turtle.forward(100)
        turtle.left(60)

    

class Square(Turtle):
    def __init__ (self, size):
        Turtle.__init__(self)
        self.shapesize(size)
        self.shape("square")
    def random_color(self):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        self.color(r,g,b)


##class NShape(Turtle):
##    def __init__ (self):
##        Turtle.__init__(self):
            

sq = Square(5)
sq= sq.random_color()


class Hexagone(Turtle):
    def __init__(self,size):
        Turtle.__init__(self)
        self.shape(r())
        r1=random.randint(0,255)
        g1=random.randint(0,255)
        b1=random.randint(0,255)
        self.color(r1,g1,b1)
        


hx =  Hexagone(10)   
