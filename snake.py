import time
from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.snaky = []
        self.create_snake()
        self.head = self.snaky[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_snaky(position)

    def add_snaky(self,position):
        tim = Turtle("square")
        tim.color('white')
        tim.penup()
        tim.goto(position)
        self.snaky.append(tim)

    def extend(self):
        self.add_snaky(self.snaky[-1].position())

    def move(self):
        for place in range(len(self.snaky) - 1, 0, -1):  # start=2, stop=0, step=-1
            new_x = self.snaky[place - 1].xcor()
            new_y = self.snaky[place - 1].ycor()  # get the position of second last seg
            self.snaky[place].goto(new_x, new_y)  # reverse order, let the last seg move to the second last seg position
        self.head.forward(MOVE_SPEED)
    def up(self):
        if self.head.heading()!= DOWN:
            self.snaky[0].setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.snaky[0].setheading(DOWN)
    def left(self):
        if self.head.heading()!= RIGHT:
            self.snaky[0].setheading(LEFT)
    def right(self):
        if self.head.heading()!= LEFT:
            self.snaky[0].setheading(RIGHT)

