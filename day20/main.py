import time
from turtle import Turtle, Screen

from snake_game_day1 import Snakes


screen = Screen()
screen.setup(width=1000, height=1000)
screen.bgcolor("black")
screen.title("Snake game, childhood memory")
screen.tracer(0)

screen.update()
is_game_on = True

snake = Snakes()

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



screen.exitonclick()