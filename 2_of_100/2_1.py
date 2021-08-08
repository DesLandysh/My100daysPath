def p():
    print("\n" * 2)


two_digit_number = "45" # input("type a two digit number: ")

a = int(two_digit_number[0])
b = int(two_digit_number[1])

print("the sum of two digits is", a + b)

p()  # 2 lines space

e = 0
for i in two_digit_number:
    e += int(i)
print("the sum of two digits is", e)

p()

result = int(two_digit_number)
c = result // 10
d = result % 10
print("the sum of two digits is", c + d)
