from quiz_brain import QuizBrain, Question
from ui import QuizUI
import requests

response = requests.get(url="https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean")
questions_data = response.json()['results']

question_bank = []
for question in questions_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)