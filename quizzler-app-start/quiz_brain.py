import html



class QuizBrain:
    def __init__(self,q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.score = 0


    def checking_answer(self, user_answer:str, correct_answer:str)->bool:
        """This function takes the user's answer and the correct answer as an input and
        checks whether both the answers match"""
        if user_answer == correct_answer:
            print("Your answer is correct")
            self.score += 1
            return True
        else:
            print("your answer is not correct")
            return False


    def next_question(self)->tuple:
        """This function will display the next question"""
        new_obj = self.question_list[self.question_number]
        if self.question_number < len(self.question_list):
            self.question_number += 1
            question_to_be_asked = html.unescape(new_obj.text)
            answer = new_obj.answer
        else :
            self.question_number = self.question_number
            question_to_be_asked = html.unescape(new_obj.text)
            answer = new_obj.answer
        return question_to_be_asked,answer

