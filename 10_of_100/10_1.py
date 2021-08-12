#days in month

def is_leap(year):
    year4 = year % 4
    year100 = year % 100
    year400 = year % 400
    if year4 == 0:
        if year400 != 0 and year100 == 0:
            return False
        else:
            return True
    else:
        return False

def days_in_month(y, m):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(y) == True:
        month_days[1] = 29
        return month_days[m-1]
    return month_days[m-1]


# reserved code
year = int(input("Enter a year: "))
month = int(input("Enter a number of month: "))
days = days_in_month(year, month)
print(days)