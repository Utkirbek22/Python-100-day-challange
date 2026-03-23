from turtle import Turtle

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.count = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.clear()
        self.write(f"Score: {self.count}", align="center", font=("Arial", 12, "normal"))

    def increase(self):
        self.count += 1
        self.clear()
        self.write(f"Score: {self.count}", align="center", font=("Arial", 12, "normal"))
