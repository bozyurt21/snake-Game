# Snake Game 

## Description
This is a basic python project written with turtle library which I had made while I was relearning python from Angela Yu, Udemy. This project tought me a lot about turtle library, how can I use it and also tought me designing a game in basic level.

## About the program
This part is about how I structure program and illustrate what does each function in class do.

### [Scoreborad.py](scoreboard.py)
>This is the class which I kept my scores and also visualized my scores with Turtle
>To use this class first import the scoreboard class to your main.py 
```
from scoreboard import ScoreBoard
```

>After you implement the class, assign this class to a varible named <name_of_your_scoreboar> as it illustrated below:

```
<name_of_your_scoreboard>=ScoreBoard()
```

**To better understand the scoreboard let's look inside a little**

```
You can choose the defined variables ALIGN and FONT whatever you want!
```

>to increase score:
```
<name_of_your_scoreboard>.increase()
```
>which will increase the score by 1.

>to reset the game:
```
<name_of_your_scoreboard>.reset()
```
>use this in your main to store your highscore in main when you die and also to update the current score to 0.
>This would not update the score on board but just would update the initial variables. If you want to write the updated score use below:

>to update scoreboard:
```
<name_of_your_scoreboard>.update_scoreboard()
```
>As I said, this will update your scoreboard written on the window.


>If you want to end the game and write "GAME OVER":
```
<name_of_your_scoreboard>.end_the_game()
```
>If you use this you couldn't replay the game, please consider that while you implement this in your main.py

**This are all the functions you can use with scoreboard class**


