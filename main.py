from game_brain import *
from game_model import *
from data import question_data
import logo

question_bank = []

for i in range(len(question_data)):
    question = question_data[i]
    question_bank.append(GameModel(question["question"], question["correct_answer"], question["difficulty"], question["category"]))

game = GameBrain(question_bank)
print(logo.banner_logo)

while game.questions_left():
    print(logo.question_logo)
    game.next_question()

print(f"Your total score is: {game.score}/{len(question_bank)}")
print("Have a Good Day!!!!!!")

