from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.new_location()
    def new_location(self):
        x_num = random.randint(-270, 270)
        y_num = random.randint(-270, 270)
        self.goto(x_num, y_num)
