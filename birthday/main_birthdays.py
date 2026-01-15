import datetime
import bday_messages

today = datetime.date.today()

birth_month = 4   
birth_day = 1

if (today.month, today.day) <= (birth_month, birth_day):
    year = today.year
else:
    year = today.year + 1

next_birthday = datetime.date(year, birth_month, birth_day)

days_away = (next_birthday - today).days

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f"My next birthday is {days_away} days away!")
