import datetime

# helper functions and constants

def date_string():
    date = datetime.datetime.today().replace(second=0, microsecond=0)
    date_str = date.date().strftime("%d-%m-%Y") 
    return (date, date_str)