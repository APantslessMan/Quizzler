from tkinter import *
import data
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.score = 0
        # create canvas
        self.canvas = Canvas(width=300, height=250)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.question = self.canvas.create_text(150, 120, width=280, text="Trivia", font=('arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        self.score_label = Label(text=f'Score: {self.score}', bg=THEME_COLOR, fg='white', font=('arial', 20, 'bold'))
        self.score_label.grid(row=0, column=1, padx=20, pady=20)
        self.cat_label = Label(text=f'{data.question_data[0]["category"]}',
                               bg=THEME_COLOR, fg='white', font=('arial', 14, 'bold'))
        self.cat_label.grid(row=0, column=0, padx=20, pady=20)
        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=lambda: self.check_question(True))
        self.false_button = Button(image=false_image, highlightthickness=0, command=lambda: self.check_question(False))
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):

        q_text = self.quiz.next_question()
        print(f'nq={q_text}, {self.quiz.question_list}')
        self.canvas.itemconfig(self.question, text=q_text)

    def check_question(self, answer: bool):

        correct_answer = self.quiz.question_list[self.quiz.question_number-1].answer
        print(f'before result canswer {correct_answer}')
        if correct_answer == "False":
            print('changing canswer to bool 0')
            correct_answer = 0
        elif correct_answer == 'True':
            print('changing canswer to bool 1')
            correct_answer = 1
        print(f'after bool switch c={correct_answer} and u={answer}')
        result = self.quiz.check_answer(answer, bool(correct_answer))
        if result:
            print(f'ui true result={result}')
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.config(bg='green')
            self.window.after(1000, lambda: self.canvas.config(bg='white'))
        else:
            print(f'ui false result={result}')
            self.canvas.config(bg='red')
            self.window.after(1000, lambda: self.canvas.config(bg='white'))
        if self.quiz.still_has_questions():
            self.get_next_question()
        else:
            print("No more questions left")
