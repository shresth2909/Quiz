class Quizbrain:
    def __init__(self,question_list):
        self.question_no = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        if self.question_no < len(self.question_list):
            return True

    def ask_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        answer = input(f'Q.No.{self.question_no} {current_question.text} The answer is true/false?')
        self.check_answer(answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
         if user_answer.lower() == correct_answer.lower():
            print(f'You got it right! The correct answer is {correct_answer}')
            self.score += 1
         else:
            print(f'You got it wrong! The correct answer is {correct_answer}')
         print(f'Your score is {self.score}/{self.question_no}')

