from turtle import Turtle
from food import Food

S_DISTANCE = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snakes:
    def __init__(self):
        self.snakes = []
        self.create_snake()


    def create_snake(self):
        for snake_index in S_DISTANCE:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(snake_index)
            self.snakes.append(snake)


    def move(self):
        for sn_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[sn_num - 1].xcor()
            new_y = self.snakes[sn_num - 1].ycor()
            self.snakes[sn_num].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_DISTANCE)

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)

    def up(self):
        if self.snakes[0].heading()!= DOWN:
            self.snakes[0].setheading(UP)

    def left(self):
        if self.snakes[0].heading()!= RIGHT:
            self.snakes[0].setheading(LEFT)

    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)
