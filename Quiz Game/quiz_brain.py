# Quiz functionality Class

class QuizBrain:

    def __init__(self, questions):
        self.question_num = 0
        self.question_list = questions
        self.score = 0



    def next_question(self):

        current = self.question_list[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {current.text} (True or False?: ")
        self.check_answer(user_answer, current.answer)

    def still_has_questions(self):

        if self.question_num == len(self.question_list):

            return False

        else:

            return True

    def check_answer(self, user_answer, correct):

        if user_answer.lower() == correct.lower():
            print('Correct!')
            self.score += 1
        else:
            print("That's wrong.")
            print(f"The correct answer was: {correct}.")
        print(f"Your current score is: {self.score}/{self.question_num}")
        print("\n")
