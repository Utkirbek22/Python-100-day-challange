import random
from tkinter import *
import pandas
from pandas import DataFrame

timer_reset = None
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
original_data = {}
try:
    data = pandas.read_csv('./flash-card-project-start/data/learn_words.csv')
except FileNotFoundError:
    original_data =pandas.read_csv("./flash-card-project-start/data/french_words.csv")
    data = pandas.read_csv("./flash-card-project-start/data/french_words.csv")
    to_learn =original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

print(data)

# French function
def next_card():
    global current_card,flip_timer
    current_card = random.choice(to_learn)
    window.after_cancel(flip_timer)

    print(current_card["French"])
    canva.itemconfig(card_title,text="French",fill="black")
    canva.itemconfig(card_word, text = current_card["French"],fill="black")
    canva.itemconfig(background_image,image=card_front_img)
    flip_timer = window.after(3000, func=english_card)

def english_card():
    canva.itemconfig(card_title,text="English",fill="white")
    canva.itemconfig(card_word,text=current_card["English"],fill="white")
    canva.config(bg=BACKGROUND_COLOR)
    canva.itemconfig(background_image,image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    next_card()
    data1 = pandas.DataFrame(to_learn)
    # data1.to_csv("./flash-card-project-start/data/learn_words.csv")
    # FIX HERE
    data1.to_csv("./flash-card-project-start/data/learn_words.csv", index=False)

window = Tk()

flip_timer = window.after(3000, func=english_card)


window.title("Flash cards")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

canva = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(file="./flash-card-project-start/images/card_back.png")

front_img = PhotoImage(file="./flash-card-project-start/images/card_front.png")
background_image = canva.create_image(400,263,image=front_img)
# Label

card_title = canva.create_text(400,150,text="title", font=("Ariel", 40,"italic"))
card_word = canva.create_text(400,263, text="word", font=("Ariel", 24, "bold"))
canva.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canva.grid(column=0,row=0,columnspan=2)

# Button
wrong_image = PhotoImage(file="./flash-card-project-start/images/wrong.png")
x_button = Button(image=wrong_image,command=next_card)
x_button.grid(column=0,row=1)

check_mark = PhotoImage(file="./flash-card-project-start/images/right.png")
check_button = Button(image=check_mark, command=is_known)
check_button.grid(column=1,row=1)

next_card()
window.mainloop()