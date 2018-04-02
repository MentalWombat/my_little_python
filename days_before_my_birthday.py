from datetime import date


birth_day = int(input("Enter your birthday day: "))
birth_month = int(input("Enter your birthday month: "))
birth_year = int(input("Enter your birthday year: "))

now_date = date.today()
bd_date = date(now_date.year, birth_month, birth_day)
next_bd_date = bd_date.replace(year=now_date.year + 1)


def days_before(a, b):
    if a < b:
        days = (bd_date - now_date).days
    elif a == b:
        days = 0
    else:
        days = (next_bd_date - now_date).days
    return days


def print_result():
    days = days_before(now_date, bd_date)
    if days > 1:
        print("Your birthday is in {0} days.".format(days))
    elif days == 0:
        print("Your birthday is today. Congrats!")
    else:
        print("Your birthday is tomorrow.")


print_result()
