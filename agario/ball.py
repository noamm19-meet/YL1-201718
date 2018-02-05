from turtle import *
import random
class Ball ( Turtle):

    def __init__(self, x , y, dx , dy , radius , color):
        
        Turtle.__init__(self)
        #Turtle.hideturtle()
        
        self.shape('circle')
        self.color(color)
        self.shapesize(radius/10)
        self.radius=radius
        self.penup()
        self.goto(x,y)
        self.dx = dx
        self.dy = dy
        self.radius=radius
    def move(self ,screen_widht , screen_height ) :
        current_x=self.xcor()
        new_x = current_x+self.dx
        current_y =self.ycor()
        new_y = current_y+self.dy
        right_side_ball= new_x+self.radius
        left_side_ball=new_x+self.radius
        up_side_ball=new_y+self.radius
        downe_side_ball=new_y+self.radius
##        print(new_x,new_y)
        self.goto(new_x , new_y)
        if right_side_ball >= screen_widht:
            self.dx = random.uniform(-1,-0.5)
        if left_side_ball <= - screen_widht:
            self.dx= random.uniform(0.5,1)
        if new_y >= screen_height:
            self.dy = random.uniform(-1,0.5)
        if new_y <= - screen_height:
            self.dy= random.uniform(0.5, 1)
