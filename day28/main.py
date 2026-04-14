from tkinter import *
from PIL import Image, ImageTk
import math



# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_reset = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer_reset
    window.after_cancel(timer_reset)
    timer.config(text="Timer", fg=GREEN)
    canva.itemconfig(timer_text, text="00:00")
    mark_label.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60


    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canva.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_reset
        timer_reset = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✓"
            mark_label.config(text=mark)



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
timer_text = canva.create_text(400,300, text="00:00", font=(FONT_NAME, 35, "bold"))
canva.grid(column=1,row=1)


timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,50))
timer.grid(column=1,row=0)

mark_label = Label(text="✓", fg=GREEN)
mark_label.grid(column=1,row=3)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset", command=reset)
reset_button.grid(column=2,row=2)








window.mainloop()