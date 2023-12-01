from turtle import Turtle, Screen
DIRECTIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.mySnakes=[]
        self.create_snake()
    def create_snake(self):
        for direct in DIRECTIONS:
            self.add_segment(direct)


    def add_segment(self,direct):
        newSnake = Turtle('square')
        newSnake.color('white')
        newSnake.penup()
        newSnake.goto(direct)
        self.mySnakes.append(newSnake)

    def extend(self):
        self.add_segment(self.mySnakes[-1].position())

    def move(self):

        for  num in range(len(self.mySnakes)-1,0,-1):
            new_x = self.mySnakes[num - 1].xcor()
            new_y = self.mySnakes[num - 1].ycor()
            self.mySnakes[num].goto(new_x, new_y)
        self.mySnakes[0].forward(MOVE_DISTANCE)
    def screen_right(self):
        if self.mySnakes[0].heading() != LEFT:
            self.mySnakes[0].setheading(RIGHT)
    def screen_left(self):
        if self.mySnakes[0].heading() != RIGHT:
            self.mySnakes[0].setheading(LEFT)

    def screen_up(self):
        if self.mySnakes[0].heading() != DOWN:
            self.mySnakes[0].setheading(UP)

    def screen_down(self):
        if self.mySnakes[0].heading() != UP:
            self.mySnakes[0].setheading(DOWN)

    def head(self):
        return self.mySnakes[0]


    def reset(self):
        for seg in self.mySnakes:
            seg.goto(1000,1000)
        self.mySnakes.clear()
        self.create_snake()