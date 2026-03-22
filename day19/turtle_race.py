from turtle import Turtle, Screen
import random
screen = Screen()
is_race = False
screen.setup(width=1000, height=900)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
colors = ["red", "blue", "black", "orange", "green", "purple"]
y_position = [-100, -50, 0, 50,100,150]
all_turtles = []

for turtle_index in range(0,6):
    tom = Turtle(shape="turtle")
    tom.penup()
    tom.goto(x=-470, y=y_position[turtle_index])
    tom.color(colors[turtle_index])
    all_turtles.append(tom)


if user_bet:
    is_race = True

while is_race:

    for t in all_turtles:
        if t.xcor() > 470:
            is_race = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You have won {winning_color}, turtle is winner!")
            else:
                print(f"winner color is {winning_color}")
            break
        rand_distance = random.randint(1,11)
        t.forward(rand_distance)

screen.exitonclick()

#
# jom = Turtle(shape="turtle")
# jom.penup()
# jom.goto(x=-470, y=50)
# jom.color(random.choice(colors))
#
# jimmy = Turtle(shape="turtle")
# jimmy.penup()
# jimmy.goto(x=-470, y=100)
# jimmy.color(random.choice(colors))
#
# jimmy = Turtle(shape="turtle")
# jimmy.penup()
# jimmy.goto(x=-470, y=150)
# jimmy.color(random.choice(colors))
#
# jimmy = Turtle(shape="turtle")
# jimmy.penup()
# jimmy.goto(x=-470, y=-50)
# jimmy.color(random.choice(colors))
#
# jimmy = Turtle(shape="turtle")
# jimmy.penup()
# jimmy.goto(x=-470, y=-100)
# jimmy.color(random.choice(colors))
