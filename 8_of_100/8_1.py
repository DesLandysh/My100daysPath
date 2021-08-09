# paint area calc

# instructions:
# 1 can of paint can cover 5 squares meterss of wall. Given random height and width of wall.
#   how many cans of paint you'll need to buy
# rounded in high
from math import ceil


def paint_calc(height, width, cover):
    cans = (height * width) / cover
    return ceil(cans)

# other solution (no print outside foo)
# def p_c(height, width, cover):
#     print(f"You'll need {ceil(height * width / cover)} cans of paint")


test_h = int(input("height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
print(f"You'll need {paint_calc(height=test_h, width=test_w, cover=coverage)} cans of paint")


