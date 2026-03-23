from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from  scorekeeping import Score

ball = Ball()
r_score = Score((100,250))
l_score = Score((-100,250))




screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #  Detact the collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hor_move()

    # Detact the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
         ball.bounce()



    #  Detact the collision with r_paddle

    if ball.xcor() > 380:
        ball.reset_pos()
        l_score.increase()
    #  detact the collison with l_paddle

    if ball.xcor() < -380:
        ball.reset_pos()
        r_score.increase()




screen.exitonclick()