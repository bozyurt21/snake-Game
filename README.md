# Snake Game 

## Description
This is a basic python project written with turtle library which I had made while I was relearning python from Angela Yu, Udemy. This project tought me a lot about turtle library, how can I use it and also tought me designing a game in basic level.

## About the program
This part is about how I structure program and illustrate what does each function in class do.

### [scoreborad.py](scoreboard.py)
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

**to increase score:**
```
<name_of_your_scoreboard>.increase()
```
>which will increase the score by 1.

**to reset the game:**
```
<name_of_your_scoreboard>.reset()
```
>use this in your main to store your highscore in main when you die and also to update the current score to 0.
>This would not update the score on board but just would update the initial variables. If you want to write the updated score use below:

**to update scoreboard:**
```
<name_of_your_scoreboard>.update_scoreboard()
```
>As I said, this will update your scoreboard written on the window.


**If you want to end the game and write "GAME OVER" int the middle of the window:**
```
<name_of_your_scoreboard>.end_the_game()
```
>**If you use this you couldn't replay the game**, please consider that while you implement this in your main.py.
>In my main I use 'space' to stop the game (you can consider using it like that)

**This are all the functions you can use with scoreboard class**

### [food.py](food.py)
> this is a class which locate food in random positions.
> first you need to implement the file into your system with following:
```
from food import Food
```
then:
**to locate food in new places:**
```
<name_of_your_food>=Food()
```
>Again we assign our varible <name_of_your_food> too class function Food().
>**What does Food function do?**
>choose random integer between from -270 to 270 for both x and y coordinates and with using turtle goto() function move the food turtle to this random location.

### [snake.py](snake.py)
This file consist class where we create our snake and with below functions assign required specialities to our snake.

To be able to use this class do the following:
```
from snake import Snake
```
Again you need to assign variable to Snake() class as follow:
```
<your_snake>=Snake()
```
**To move right use:**
```
<your_snake>.screen_right()
```
>This will move snakes head to the right.

**To move left use:**
```
<your_snake>.screen_left()
```
>This will move snakes head to the left.

**To move up use:**
```
<your_snake>.screen_up()
```
>This will move sneakes head to the up direction.

**To move down use:**
```
<your_snake>.screen_down()
```
>This will move sneakes head to the down direction.

# These functions DO NOT move sneak entirely just move the head, to be able to move in direction you should use the following:

**to move continuesly use:**
```
<your_snake>.move()
```

**to increase the length of snake use:**
```
<your_snake>.extend()
```
**to reset the snake length use:**
```
<your_snake>.reset()
```

# If you have any question regarding to my code, please mail [bensuozyurt.21@gmail.com](bensuozyurt.21@gmail.com).
### Hope you enjoyed my code :)



