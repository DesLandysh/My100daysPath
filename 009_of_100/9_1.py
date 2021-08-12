# Grading program
# database of student_scores in dict names: scores
# write a program that converts their scores to grades. -> new dict
# DO NOT modify student_score dict
# DO NOT write any print statements.
# scores 91 - 100 = "Outstanding"
# scores 81 - 90 = "Excedds Expectations"
# Scores 71 - 80 = "Acceptable"
# scored 70 or lower: Grade = "Fail"

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif 80 < student_scores[key] <= 90:
        student_grades[key] = "Exceeds Expectation"
    elif 70 < student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
