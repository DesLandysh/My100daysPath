from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()

print(f"You've complete the quiz\nYour final score was: {quiz.score}/{quiz.q_number}")
