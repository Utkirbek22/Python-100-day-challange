from tkinter import *
from PIL import Image,ImageTk

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flash cards")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

canva = Canvas(width=800, height=526)
front_img = PhotoImage(file="./flash-card-project-start/images/card_front.png")
canva.create_image(400,263,image=front_img)
# Label
canva.create_text(400,150,text="title", font=("Ariel", 40,"italic"))
canva.create_text(400,263, text="Word", font=("Ariel", 50, "bold"))
canva.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canva.grid(column=0,row=0,columnspan=2)



# Button

wrong_image = PhotoImage(file="./flash-card-project-start/images/wrong.png")
x_button = Button(image=wrong_image)
x_button.grid(column=0,row=1)

check_mark = PhotoImage(file="./flash-card-project-start/images/right.png")
check_button = Button(image=check_mark)
check_button.grid(column=1,row=1)


window.mainloop()