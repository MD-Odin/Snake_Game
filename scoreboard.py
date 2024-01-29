from turtle import Turtle

class scoreboard(Turtle):
    def scores(self):
        self.score=0
        self.update()

    def update(self):
        self.clear()
        self.score = self.score + 1
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score:{self.score-1}",(0,270),"center",('Arial',20,"normal"))
        self.hideturtle()

    def gameover(self):
        self.goto(0,0)
        self.write(f"GameOver score is {self.score-1}",move=(0,0),align="center",font=("Arial",20,"normal"))

