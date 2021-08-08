#BMI 2.0
"""
    under 18.5 - underweight
    18.5 - 25 - normal weight
    25-30 overweight
    30-35 obese
    above 35 clinically obese
"""

def a():
    print("\n" * 2)


height = float("1.75")
weight = float("84")

bmi = round(weight / height ** 2, 1)
print("Your BMI is", bmi)
if bmi < 18.5:
    print("You are underweight")
elif 18.5 <= bmi <= 25:
    print("You have the normal weight")
elif 25 < bmi <= 30:
    print("You are overweight")
elif 30 < bmi <= 35:
    print("You have obese")
else:
    print("This is clinically obese")

a()

def p_result(i):
    tup = ('underweight', 'normal weight', 'overweight', 'obese', 'clinically obese')
    word = tup[i]
    print(f"Your BMI is {bmi}, so your are {word}")

if bmi < 18.5:
    p_result(0)
elif bmi <= 25:
    p_result(1)
elif bmi <= 30:
    p_result(2)
elif bmi <= 35:
    p_result(3)
else:
    p_result(4)
