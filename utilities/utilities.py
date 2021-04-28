import datetime

# helper functions and constants

def date_string():
    date = datetime.datetime.today().replace(second=0, microsecond=0)
    date_str = date.date().strftime("%d-%m-%Y") 
    return (date, date_str)

def make_week(today):
    week = []
    for _ in range(7):
        week.append(today.strftime("%d-%m-%Y"))
        today += datetime.timedelta(days=1)

    return week