from pyexpat.errors import messages
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*","(", ")", "-", "_", "=", "+" "[", "]", "{", "}", "|",";", ":", "'", '"', ",", ".", "<", ">", "?","/", "\\", "~", "`"]

    # user_letters = int(input("How many letters would you like to have in your password ?: \n "))
    # user_symbols = int(input("How many symbols do you wanna have ? \n" ))
    # user_nums = int(input("How many numbers would you like to have ?:\n "))
    # #
    # for _ in range(0, user_letters):
    #     my_password.append(random.choice(letters))

    letter_password = [random.choice(letters)  for _ in range(random.randint(1,6))]

    # for _ in range(0, user_symbols):
    #     my_password.append(random.choice(symbols))
    symbol_password = [random.choice(symbols) for _ in range(random.randint(1,4))]

    # for _ in range(0, user_nums):
    #     my_password.append(random.choice(numbers))

    number_password = [random.choice(numbers) for _ in range(random.randint(1,5))]

    big_password = letter_password + number_password + symbol_password
    random.shuffle(big_password)
    # password = ""
    # for char in big_password:
    #     password += char

    password = "".join(big_password)
    password_entry.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.askokcancel(title="OOPs", message="that is empty")
    else:
        is_oaky = messagebox.askokcancel(title=website, message=f"There are details entered: \nEmail: {email}"
                                                                f"Password: {password} \nIs it is to save?")
        if is_oaky:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                entry_website.delete(0,END)
                password_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(pady=100, padx=200)
window.title("Password manager")




canva = Canvas(width=1000,height=800)
img = Image.open("logo.png")
img = img.resize((400,400))
lock_img = ImageTk.PhotoImage(img)
canva.create_image(500,300,image=lock_img)

canva.grid(column=0,row=0, columnspan=3)

# Label
website_label = Label(text="Website")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username")
email_label.grid(column=0,row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# Entry
entry_website = Entry(width=35)
entry_website.grid(column=1,row=1,columnspan=2)
entry_website.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0,"utkirbbeekk@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

#  Button
generate_password_entry = Button(text="Generate", command=gen_pass)
generate_password_entry.grid(column=2,row=3)
add_button = Button(text="Add", command=save)
add_button.grid(row=4,column=1, columnspan=2)





window.mainloop()