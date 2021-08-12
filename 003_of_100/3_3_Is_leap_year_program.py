# Leap year
# Високосный год
# on every year that is evenly divisible by 4
    # except evry that that is evenly divisible by 100
    #    unless the year is also evenly divisible be 400


year = int("2020")  # int(input("which year do you want to check? "))

def p_leap(t_f):
    if t_f:
        print("this is the leap year")
    else:
        print("this is not the leap year")

year4 = year % 4
year100 = year % 100
year400 = year % 400

if year4 == 0:
    if year400 != 0 and year100 == 0:
        p_leap(False)
    else:
        p_leap(True)
else:
    p_leap(False)
