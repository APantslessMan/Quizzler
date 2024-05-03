import html


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.still_has_questions():
            question = self.question_list[self.question_number]
            q_text = html.unescape(question.text)
            self.question_number += 1
            return f"{self.question_number}. {q_text}"
        else:
            return None

    def check_answer(self, u_answer: bool, c_answer: bool) -> bool:
        if u_answer == c_answer:
            res = True
            print(f'yes, res={res} c={c_answer} u={u_answer}')

            self.score += 1
        else:
            res = False
            print(f'no, res={res} c={c_answer} u={u_answer}')

        print(f"The correct answer was: {c_answer}. ")
        if self.still_has_questions():
            print(f"Your current score is {self.score}/{self.question_number}")
        return res
