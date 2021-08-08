# The highest Score
# Calculate the highest score from list of score
# eg. student_score = [78, 65, 89, 86, 55, 91, 64, 89]
# not allowed to use min/max functions
# output: "The highest score in the class is: x"

# reserved code
student_scores = input("Input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# solution
high = 0
for score in student_scores:
    if score < high:
        continue
    high = score
print(f"The highest score in the class is: {high}")

# max() solution
print(max(student_scores))

# stolen
student_scores.sort()
print(f"The highest score in the class is: {student_scores[-1]}")