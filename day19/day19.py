from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)
def back():
    tim.backward(10)
def right_move():
    tim.right(10)
def left_move():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=back)
screen.onkey(key="d", fun=right_move)
screen.onkey(key="a", fun=left_move)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
