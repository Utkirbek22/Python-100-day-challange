from pyexpat.errors import messages
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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
generate_password_entry = Button(text="Generate")
generate_password_entry.grid(column=2,row=3)
add_button = Button(text="Add", command=save)
add_button.grid(row=4,column=1, columnspan=2)





window.mainloop()