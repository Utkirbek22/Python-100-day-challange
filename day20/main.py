import time
from turtle import Turtle, Screen
from snake_game_day1 import Snakes
from food import Food
from Scorekeeping import Score
screen = Screen()
food = Food()
score = Score()

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
count = 0
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
#     Detact collision with food
    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        score.increase()
        snake.create_snake()
#     Detact with wall collision

    if snake.snakes[0].xcor() > 480 or snake.snakes[0].xcor() < -480 or snake.snakes[0].ycor() > 480 or snake.snakes[0].ycor() < -480:
        is_game_on = False


        #  Detact with the tail
    for segment in snake.snakes[1:]:
        # if segment == snake.snakes[0]:
        #     pass
        if snake.snakes[0].distance(segment) < 10:
            is_game_on = False


screen.exitonclick()

