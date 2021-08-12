def a():
    print("\n" * 2)


print("Hi to the rollercoaster!")
height = int("121")  # int(input("your height in cm? "))

if height >= 120:
    print("go on")
else:
    print("sorry, go out here, snork!")
# == is equility
a()
age = int("18")  # int(input("what's your age? "))
if height >= 120:
    if age > 18:
        bill = 15
        print("Pay $15")
    elif age < 12:
        bill = 5
        print("Pay $5")
    elif age >=45 and age <= 55:
        bill = 0
        print("For free")
    else:
        bill = 7
        print("Pay $7")
    wants_photo = "y"
    if wants_photo == "y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("go out!")
