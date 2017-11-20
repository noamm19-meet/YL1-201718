from turtle import Turtle,colormode
import random
 
class Square(Turtle):
    def __init__ (self, size):
        
        Turtle.__init__(self)
        self.shapesize(size)
        self.shape("square")
        def randome_color(self):
            
            self=random.randint(colormode)


sq = Square(5)
