class GameBrain:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0

    def check_answer(self, user_choice, correct_answer):
        if user_choice == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}")

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        print(f"Category: {current_question.category}")
        print(f"Difficulty: {current_question.difficulty}")
        user_choice = input(f"Question #{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(user_choice, current_question.answer)

    def questions_left(self):
        return self.question_number < len(self.questions_list)
