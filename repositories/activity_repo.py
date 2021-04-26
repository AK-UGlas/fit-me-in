# from db.run_sql import run_sql
# from datetime import date
# from models.booking import Booking
# from models.location import Location

# helper functions
def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0:
        if year % 100 == 0:
            return False
        else:
            return True
    return False

def day_of_the_week(day, month, year):
    weekdays = ["Sunday", "Monday", "Tuesday", 
                "Wednesday", "Thursday", "Friday", 
                "Saturday"]
    months = [11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    converted_months = [int((2.6 * month - 0.2) % 7) 
                        for month in months]

    if month > 3:
        year -= 1

    today = (year + int(year/4) - int(year/100) + int(year/400) + 
             converted_months[month-1] + day) % 7
    return weekdays[today]

print(day_of_the_week(30, 4, 2021))