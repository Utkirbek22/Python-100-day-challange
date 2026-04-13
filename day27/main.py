from tkinter import *
import tkinter

window = tkinter.Tk()
window.title("my first GUI program")
window.minsize(width=1000, height=700)

#  label
my_label = tkinter.Label(text="here is your label !", font=("Arial", 24, "italic"))
my_label.pack()

my_label.config(text="here is new one")
my_label["text"] = "New text"
# er


# button

def get_clicked():
    print("I got clikced")
    new_text = input.get()
    my_label.config(text=new_text)
button = Button(text= "click me", command=get_clicked)
button.pack()


# input

input = Entry()

print(input.get())

input.pack()







window.mainloop()