from tkinter import *
from PIL import Image,ImageTk


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
# window.minsize(width=1000,height=800)
window.title("Password manager")




canva = Canvas(width=1000,height=800)
img = Image.open("logo.png")
img = img.resize((400,400))
lock_img = ImageTk.PhotoImage(img)
canva.create_image(500,350,image=lock_img)
canva.pack()


window.mainloop()