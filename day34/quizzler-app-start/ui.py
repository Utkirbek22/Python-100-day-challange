from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(pady=20,padx=20, bg=THEME_COLOR)

        self.score_label = Label(text="score:0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canva = Canvas(width=300,height=250,bg="white")

        self.canva.create_text(150,125,text="hello", font=("Ariel", 24, "italic"),fill=THEME_COLOR)



        # buttons
        self.img_wrong_button_ = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.img_wrong_button_)
        self.wrong_button.grid(column=0,row=2)

        # self.false_img = self.canva.create_image(100,50,image=self.wrong_button)

        self.img_photo_true = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=self.img_photo_true)
        self.correct_button.grid(column=1,row=2)

        # self.true_img = self.canva.create_image(100,60,image=self.correct_button)

        self.canva.grid(column=0, row=1,columnspan=2,pady=50)
        self.window.mainloop()
