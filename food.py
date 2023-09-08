from turtle import Turtle
import random

X_AXIS = 280
Y_AXIS = 280

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_wid = 0.7, stretch_len = 0.7)
        self.color("slateblue")
        self.speed(0) 
           
        self.refresh()

    def refresh(self) -> None:
        self.goto(random.randint(-X_AXIS, X_AXIS), random.randint(-Y_AXIS, Y_AXIS))

    
