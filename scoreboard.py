from turtle import Turtle
ALIGN='center'
FONT=("Courier",24,'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.ht()
        self.penup()
        self.score=0
        with open("data.txt") as data:
            self.highscore= int(data.read())
        self.update_scoreboard()
        self.is_game_on=True
    def increase_score(self):
        self.score+=1
        self.update_scoreboard()


    def reset(self):
        if self.score >= int(self.highscore):
            with open("data.txt",mode="w") as data:
                data.write(f"{self.score}")
            with open("data.txt",mode="r") as data:
                self.highscore=data.read()
        self.score=0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} ", align=ALIGN, font=FONT)
        self.goto(0, 250)
        self.write(f"High Score: {self.highscore}", align=ALIGN, font=FONT)

    def end_the_game(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN,font=FONT)
        self.is_game_on=False




