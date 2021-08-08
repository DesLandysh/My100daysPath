# average height
"""
calculate the avg student height from a List of heights.
eg student_heights = [180, 124, 165, 173, 189, 169, 146]

180+...+146 = 1146
total 7 num
1146/7 = 163.71...
whole number is 164
"""
# reserved code
student_heights = input("input a list of student heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)

# main solution
#total = sum(student_heights)
#print("Average height is:", round(total/len(student_heights)))


# another solution
#total = 0
#for m in student_heights:
#    total += m
#result = round(total/len(student_heights))
#print(result)


# no sum() & no len() solution
total = 0
count = 0
for m in student_heights:
    total += m
    count += 1
result = round(total/count)
print(result)
