import pandas
import smtplib
import datetime as dt
import random

now = dt.datetime.now()
today_tuple = (now.month, now.day)

my_email = '9i6qwwsptp4o2wh@rambler.ru'
my_pass = 'qlknm47HVjT!glpi'

bday_msgs = []
for _ in range(1, 4):
    with open(f'./letter_templates/letter_{_}.txt') as message:
        bday_msgs.append(message.read())

siblings_bday = pandas.read_csv('./birthdays.csv')
bdays = siblings_bday.to_dict(orient='records')
mess_to_send = random.choice(bday_msgs)
for bday in bdays:
    if(bday['day'] == today_tuple[1] and bday['month'] == today_tuple[0]):
        mess_to_send = mess_to_send.replace('[NAME]', bday['name'])
        print(mess_to_send)
        with smtplib.SMTP('smtp.rambler.ru', port= 465) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=bday['email'],
                msg=f'Subject:Bday Wishh\n\n{mess_to_send}'
            )
