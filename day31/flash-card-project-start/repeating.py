from tkinter import Tk, Canvas, PhotoImage, Button

BACKGROUND_COLOR = "#B1DDC6"



window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canva = Canvas(width=800,height=526)
img = PhotoImage(file='images/card_front.png')
photo = canva.create_image(400,263,image=img)

title_text = canva.create_text(400,150,text="Title", font=("Ariel",20,"italic"))
word_text = canva.create_text(400,263,text="Word", font=("Ariel", 30, "bold"))

# Button
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img)

check_mark = PhotoImage(file="images/right.png")
check_button = Button(image=check_mark)

check_button.grid(column=1,row=2)
wrong_button.grid(column=0,row=2)
canva.grid(column=0,row=0,columnspan=2)
window.mainloop()