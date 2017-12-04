from turtle import *
import random
import math
class Ball(Turtle):
    def __init__(self, radius, color, speed):
        Turtle.__init__(self)
        self.shape('circle')
        self.shapesize(radius)
        self.color(color)
        self.speed(speed)
def chek_coliision(ball1,ball2):        
    if math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2)+(math.pow((ball1.ycor()-ball2.ycor()),2)))<=radius:
        ball1=ball1.color('red')




ball1=Ball(2,"blue",10 )
ball1.goto(100,100)
ball2=Ball(5, 'green',100)                                          
