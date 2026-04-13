import tkinter

window = tkinter.Tk()
window.title("my first GUI program")
window.minsize(width=1000, height=700)

my_label = tkinter.Label(text="here is your label !", font=("Arial", 24, "italic"))
my_label.pack()














window.mainloop()