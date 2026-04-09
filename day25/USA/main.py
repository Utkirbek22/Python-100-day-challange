import turtle
import pandas
from PIL import Image

img = Image.open("profile_img.gif")

img = img.convert("RGB")
img.save("profile_img.gif")

screen = turtle.Screen()
screen.title("USA. States Games")

image = "/home/jack/code/Pyhton-100/day25/USA/profile_img.gif"
screen.addshape(image)
turtle.shape(image)

pandas.read_csv()

tryme = screen.textinput(title="Guess me", prompt="WHat is your guess")
print(tryme)


screen.exitonclick()
screen.mainloop()