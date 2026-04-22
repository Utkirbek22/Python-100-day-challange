import smtplib
import datetime as dt

import pandas as pd

import random

my_email = "Socialmedia05112022@gmail.com"
password = "nxnzruzsaxgmnqti"

# print(random_file)
now = dt.datetime.now()
today = (now.month, now.day)

data = pd.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthday_dict)
# print(birthday_dict)
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com",587) as email_con:
        email_con.starttls()
        email_con.login(user=my_email, password=password)
        email_con.sendmail(from_addr=my_email,
                           to_addrs= birthday_person["email"],
                           msg=f"Subject: Happy Birthday!\n\n{content}")

