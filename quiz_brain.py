class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def next_question(self):
        try:
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            return f"Q.{self.question_number}: {self.current_question.text}"
        except IndexError:
            return False

    def check_answer(self, user_answer):
        if str(user_answer) == self.current_question.answer:
            self.score += 1
            return True
        else:
            return False

class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer