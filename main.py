from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen=Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('sneaky snake game')
screen.tracer(0)

mySnake=Snake()
food=Food()
myScoreBoard=ScoreBoard()
screen.listen()

screen.onkey(fun=mySnake.screen_up, key="Up")
screen.onkey(fun=mySnake.screen_down, key="Down")
screen.onkey(fun=mySnake.screen_right, key="Right")
screen.onkey(fun=mySnake.screen_left, key="Left")
screen.onkey(fun=myScoreBoard.end_the_game, key="space ")

while myScoreBoard.is_game_on:
    screen.update()
    time.sleep(0.1)
    mySnake.move()
    if mySnake.head().distance(food)<15:
        food.new_location()
        myScoreBoard.increase_score()
        mySnake.extend()
    for segment in mySnake.mySnakes[1:]:
        if mySnake.mySnakes[0].distance(segment)<10:
            myScoreBoard.reset()
            mySnake.reset()

    if mySnake.head().xcor()>280 or mySnake.head().xcor()<-280 or mySnake.head().ycor()>280 or mySnake.head().ycor()<-280:
        myScoreBoard.reset()
        mySnake.reset()
screen.exitonclick()