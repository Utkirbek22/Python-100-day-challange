from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 430)
        self.write(f"Score: {self.count}, high score is {self.high_score}", align="center", font=("Arial", 24, "normal") )
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.count} High Score: {self.high_score} ", align="center", font=("Arial", 24, "normal"))
    def reset(self):
        if self.count > self.high_score:
            self.high_score = self.count
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.count = 0
        self.update_score()

    def increase(self):
        self.count += 1
        self.update_score()




    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game over", align="center", font=("Arial", 24, "normal"))



