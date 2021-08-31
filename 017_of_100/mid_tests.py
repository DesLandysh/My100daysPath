class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # Default value
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Des Kitten")
user_2 = User("002", "Mary Kitten")
print(user_1.username)


user_1.follow(user_2)
print(user_1.followers, user_1.following, user_2.following, user_2.followers)


# list of classes from 100days
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

