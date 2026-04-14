from tkinter import *
from PIL import Image, ImageTk



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=400)
window.config(padx=100, pady=50, bg=YELLOW)


canva = Canvas(width=800, height=600, bg=YELLOW, highlightthickness=0)
img = Image.open("tomato.png")
img = img.resize((400, 400))
tomoto_img = ImageTk.PhotoImage(img)
canva.create_image(400, 250, image=tomoto_img)
canva.create_text(400,300, text="00:00", font=(FONT_NAME, 35, "bold"))

canva.grid(column=1,row=1)


timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,50))
timer.grid(column=1,row=0)

mark_label = Label(text="✓", fg=GREEN)
mark_label.grid(column=1,row=3)

start_button = Button(text="Start")
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2,row=2)








window.mainloop()