from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 430)
        self.write(f"Score: {self.count}", align="center", font=("Arial", 24, "normal") )
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.count} High Score: {self.high_score} ", align="center", font=("Arial", 24, "normal"))
    def increase(self):
        self.count += 1
        self.clear()
        self.write(f"Score: {self.count}", align="center", font=("Arial", 24, "normal") )
    def reset(self):
        if self.count > self.high_score:
            self.high_score = self.count

        self.count = 0
        self.update_score()



    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game over", align="center", font=("Arial", 24, "normal"))



