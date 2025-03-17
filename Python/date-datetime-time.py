import datetime

birthday = datetime.date(2025, 3, 19) #module datetime, class date
print(birthday)

today = datetime.date.today()
print(today)

if today == birthday:
    print("Its your birthday")

print("Its not your birthday")

###

purchase_data = datetime.datetime.today()
purchase_count = 0

purchase = {}
purchase["Date"] = purchase_data

print(purchase)

###

new_date = datetime.datetime(2025, 3, 19) # 2025-03-19 00:00:00
print(new_date) # time is expected to be 00:00:00 cuz it wasnt informed

hora = datetime.time(18, 30) # 18:30:00
print(hora)

### ADDING TIME IN DATES FORMAT - timedelta

d = datetime.datetime(2023, 3, 19, 13, 45)
print(d)

d = d + datetime.timedelta(days=30) # it can be set by days, weeks
print(d)