from turtle import Turtle

STARTING_POSITON = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITON)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)
