import smtplib
import datetime as dt
import random

my_email = "Socialmedia05112022@gmail.com"
password = "nxnzruzsaxgmnqti"

now = dt.datetime.now()

day = now.weekday()
if day == 1:
    with open("quotes.txt") as quote_file:
        all_quote = quote_file.readlines()
        quote = random.choice(all_quote)
        print(quote)

connection = smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()
connection.login(user=my_email,password=password)

connection.sendmail(to_addrs=my_email,
                    from_addr="utkirbbeekk@gmail.com",
                    msg=f"Subject: Monday motivation\n\n{quote}")
connection.close()


