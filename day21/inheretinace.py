class Animal:
    def __init__(self):
        self.mouth = 4

    def breathe(self):
        print("I am having problem for breathing")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("I can buy flowers")

    def fly(self):
        print("I can't fly, so i will not focus flying cause i am a fish,"
              "so, I will focus how to swim better")


nemo = Fish()
nemo.fly()
nemo.breathe()
