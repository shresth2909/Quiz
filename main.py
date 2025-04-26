from question_model import Question
from data import question_data
from quiz_brain import Quizbrain


Question_bank = []
for each in question_data:
    question = Question(text=each['question'], answer=each['correct_answer'])
    Question_bank.append(question)


quiz = Quizbrain(Question_bank)
while quiz.still_has_question():
    quiz.ask_question()
print(f"you are done with the quiz and your final score is {quiz.score}/{quiz.question_no}")

















'''
for question_object in Question_bank:
    print(f"Question: {question_object.text}")
    print(f"Answer: {question_object.answer}")
    print("-" * 20)  # Separator for better readability
'''
