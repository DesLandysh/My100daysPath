# tip calculator

# input bill $XXX.YY :float(.2f)
# input percentage 10, 12, 15 :int
# input how many people to split the bill? :int
# output $XX.YY :float(.2f)

total_bill = float("150")  # float(input("What was the total bill? $"))
percentage_tip = int("12") # int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_to_split = int("5") # int(input("How many person to split the bill? "))
tip_sum = total_bill * percentage_tip / 100
to_pay = round((total_bill + tip_sum) / people_to_split, 2)
to_pay = "{:.2f}".format(to_pay)
print(f"Each person should pay: ${to_pay}")

# (150 / 5) * 1.12
to_pay_alt = round((total_bill / people_to_split) * (percentage_tip / 100 + 1), 2)
print(to_pay_alt)
