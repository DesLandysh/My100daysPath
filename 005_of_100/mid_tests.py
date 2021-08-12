fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

"""
fruit = "Apple"
print("Apple")
...
fruit = "Pear"
print("Pear")
"""

"""
Carl Gauss solution
 1  +  2 +  3 +...+ 100
100 + 99 + 98 +...+  1
101 + 101 + 101 +...+ 101 and / 2
50 x 101 = 5050
"""

for number in range(1, 11, 3):  # 11 is not included
    print(number)

total = 0
for num in range(1, 101):
    total += num
print(total)