import datetime as dt
import random
import smtplib
import pandas

##################### Extra Hard Starting Project ######################

from_email = 'YOUR EMAIL ID'
password = 'YOUR PASSWORD'
status = False

# 1. Update the birthdays.csv
data = pandas.read_csv('birthdays.csv')
data_dict = data.to_dict(orient='records')

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
for birthdate in data_dict:
    if now.day == birthdate['day'] and now.month == birthdate['month']:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

        random_num = random.choice(range(1, 4))
        with open(f"./letter_templates/letter_{random_num}.txt") as letter_file:
            letter = letter_file.read()
        final_letter = letter.replace('[NAME]', birthdate['name'])

# 4. Send the letter generated in step 3 to that person's email address.

        connection = smtplib.SMTP('smtp.gmail.com',port=587)
        connection.starttls()
        connection.login(user=from_email,password=password)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=birthdate['email'],
            msg=f"Subject:Birthday Wish\n\n"
                f"{final_letter}")


