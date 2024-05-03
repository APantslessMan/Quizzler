class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    # def parse_data(self, question):
    #     if question.find("&#039;"):
    #         question.replace("&#039;", "'")
    #     if question.find("&quot;"):
    #         question.replace("&quot;", "'")
    #         print(question)
    #     return question
