from question_model import Question
import data
from quiz_brain import QuizBrain
from ui import QuizInterface
data.get_token()

data.get_trivia()
question_bank = []
for i, x in enumerate(data.question_data):
    # question_bank.append(Question(x))
    parse_question = x["question"]
    # print(Question.parse_data(parse_question, parse_question))
    new_question = Question(parse_question, x["correct_answer"])
    question_bank.append(new_question)
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
#
# while quiz.still_has_questions():
#     quiz.next_question()
print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}")
