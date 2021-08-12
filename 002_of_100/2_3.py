# You have x days, y weeks and z months left
# 90 year is the end

age = "35" # input("What is your current age? ")

rip_time = 90  # years
left_time = rip_time - int(age)
months = left_time * 12
weeks = left_time * 52
days = left_time * 365
print(f"You have {days} days, {weeks} weeks or {months} months left")
