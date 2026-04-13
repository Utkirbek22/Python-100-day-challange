# from tkinter import *
#
# def km_to_mile():
#     miles = float(miles_input.get())
#     km = miles * 1.609
#     km_number_label.config(text=f"{km}")
#
#
#
# window = Tk()
# window.minsize(width=600, height=400)
# window.title("Miles to km convertor")
# window.config(padx=20, pady=20)
#
# miles_input = Entry()
# miles_input.grid(column=1, row=0)
#
# miles_label = Label(text="Miles")
# miles_label.grid(column=2, row=0)
#
# equel_to_label = Label(text="is equal to")
# equel_to_label.grid(column=0, row=1)
#
# km_number_label = Label(text="0")
# km_number_label.grid(column=1, row=1)
#
# km_label = Label(text="km")
# km_label.grid(column=2, row=1)
#
# calc_button = Button(text="Calculate", command=km_to_mile)
# calc_button.grid(column=1,row=2)
#
# window.mainloop()
















from tkinter import *

def km_to_mile():
    miles = float(inp.get())
    km = miles * 1.609
    num_km_label.config(text=f"{km}")


window = Tk()

window.config(pady=20, padx=20)
window.minsize(width=500, height=400)

inp = Entry()
inp.grid(column=1,row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

num_km_label = Label(text="0")
num_km_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=km_to_mile)
calc_button.grid(column=1, row=2)


window.mainloop()
















