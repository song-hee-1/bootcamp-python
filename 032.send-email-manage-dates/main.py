import smtplib
import datetime as dt
import random

my_email = "email_address"
password = "password"

now = dt.datetime.now()
today_of_week = now.weekday()

if today_of_week == 3:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
    quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as conneciton:
        conneciton.starttls()
        conneciton.login(user=my_email, password=password)
        conneciton.sendmail(from_addr=my_email,
                        to_addrs="to_email_address",
                        msg=f"Subject:Today Motivation! \n\n {quote}")
