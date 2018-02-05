import turtle
import time
from turtle import Turtle
from turtle import *
import random
import math
from ball import Ball

turtle.tracer
turtle.penup()
turtle.hideturtle()
turtle.goto(500, 500)
turtle.pendown()
turtle.goto(-500 ,500)
turtle.goto(-500 ,-500)
turtle.goto(500 , -500)
turtle.goto(500 ,500)
RUNING = True
SLEAP = 0.0077
SCREEN_WIDTH = int(turtle.getcanvas().winfo_width()/2)
SCREEN_HEIGHT = int(turtle.getcanvas().winfo_height()/2)

NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS =10
MAXIMUM_BALL_RADIUS= 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX =5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY=5

BALLS= []
for i in range (NUMBER_OF_BALLS):


    x = random.randint(int( - SCREEN_WIDTH )+ MAXIMUM_BALL_RADIUS , int( SCREEN_WIDTH) - MAXIMUM_BALL_RADIUS)
    y = random.randint(int( - SCREEN_HEIGHT) + MAXIMUM_BALL_RADIUS , int(SCREEN_HEIGHT) -MAXIMUM_BALL_RADIUS)
    dx = random.randint(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
    dy = random.randint(MINIMUM_BALL_DY , MAXIMUM_BALL_DY) 
    radius = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)


def chek_colision(ball_a,ball_b):
    if ball_a.radius == ball_b.radius and ball_a.pos() == ball_b.pos():
        print("bad")
        return False
    
    distance = math.sqrt(math.pow((ball1.xcor()-ball2.xcor()),2)+(math.pow((ball1.ycor()-ball2.ycor()),2)))
    if distance+10<=ball_a.radius +  ball_b.radius:
        print("good")
        return True
    print ("bad")
    return False

def chek_all_colision():
    for i in BALLS:
        if chek_colision(ball_a, i) == True:
            a= i.radius
            b=ball_2.radius
        if chek_colision(ball_a, ball_b) == True:
            A= i.radius
            B=ball_b.radius
##    chek_colision(ball1, ball2)   
##    chek_colision(ball1 , ball3)
##    chek_colision(ball3 , ball2)   




def moove_all_balls():
    for i in BALLS:
           i.move(SCREEN_WIDTH  , SCREEN_HEIGHT)
        

def chek_my_ball_colision():
    for i in BALLS:
        if chek_colision(BALLS[i] , MY_BALL):


ball2=Ball(x, y, dx, dy,radius , "blue");

ball2.goto(100,100)

BALLS.append(ball2)


ball3=Ball(x, y, dx, dy,radius , "green")
ball3.goto(200,200)
BALLS.append(ball2)

##ball4=Ball(x, y, dx, dy,radius , "oreng")
##BALLS.append(ball4)
##ball4.move(SCREEN_WIDTH , SCREEN_HEIGHT )

ball1=Ball(x, y, dx, dy,radius , "red")
BALLS.append(ball1)
moove_all_balls()
chek_all_colision()

##ball1=Ball(0,0 , 1 , 1,10 , "green")
##while True:
##    ball2.move(300, 500)
##    ball3.move(400 ,500)
##    ball1.move(500,500)

    
