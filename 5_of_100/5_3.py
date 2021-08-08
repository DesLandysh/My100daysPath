# Adding evens
# the sum of even numbers
# use the range()

# reserved code
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]  # input("input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# solution
total = 0
for m in range(0, len(student_scores)):
    if student_scores[m] % 2 == 0:
        total += student_scores[m]
print(total)

# no range solution
print(sum(filter(lambda x: x % 2 == 0, student_scores)))
