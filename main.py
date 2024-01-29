from turtle import *
import time
from snake import Snake
from food import Food
from scoreboard import scoreboard

tracer(0)

screensize(600, 600)
bgcolor("black")
title("Snake Game")
snake = Snake()
food = Food()
food.createfood()
score = scoreboard()
score.scores()
listen()
onkey(snake.up,"Up")
onkey(snake.down,"Down")
onkey(snake.right,"Right")
onkey(snake.left,"Left")
game_on = True
while game_on is True:
    update()
    time.sleep(0.1)
    snake.move()
    #collision with food
    if snake.head.distance(food) < 20:
        food.refres()
        snake.extend()
        score.update()
    #collision with wall
    if snake.head.xcor() > 300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300:
        game_on = False
        score.gameover()
    #collision with tail
    for snakes in snake.snaky:
        if snakes == snake.head:
            pass
        elif snake.head.distance(snakes) < 10:
            game_on = False
            score.gameover()


exitonclick()
