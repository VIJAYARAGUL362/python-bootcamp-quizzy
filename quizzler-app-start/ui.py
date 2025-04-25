import tkinter
from tkinter import Canvas, Label, PhotoImage, Button
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self,obj:QuizBrain):
        self.timer : int
        self.quiz_object = obj
        self.window = tkinter.Tk()
        self.window.title("Quizzy")
        self.correct_image = PhotoImage(file="./images/true.png")
        self.wrong_image = PhotoImage(file="./images/false.png")
        self.canvas = Canvas(width=500,height=500,highlightthickness=0)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.question_id = self.canvas.create_text(250, 250, text="",width=450)
        self.window.config(bg=THEME_COLOR,pady=20,padx=20)
        self.button_makers()
        self.label_maker()
        self.real_answer = ""
        self.questions()
        self.window.mainloop()

    def true_answer(self)->None:
        """This function check the answer and call give feedback function"""
        user_answer = True
        state = self.quiz_object.checking_answer(str(user_answer),self.real_answer)
        self.give_feedback(state)


    def false_answer(self)->None:
        """This function check the answer and call give feedback function"""
        user_answer = False
        state = self.quiz_object.checking_answer(str(user_answer),self.real_answer)
        self.give_feedback(state)


    def give_feedback(self,is_right)->None:
        """This function will change the background of the canvas based on the answer and call the questions function"""
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        timer = self.window.after(1000,func=self.questions)


    def button_makers(self)->None:
        """This function creates two buttons"""
        self.button1 = Button(image=self.correct_image,bg=THEME_COLOR,command=self.true_answer)
        self.button1.grid(row=2,column=0)
        self.button2 = Button(image=self.wrong_image,bg=THEME_COLOR,command=self.false_answer)
        self.button2.grid(row=2,column=1)

    def questions(self)->None:
        """This function put questions into the canvas and one's the questions are over it will disable the buttons"""
        self.canvas.config(bg="white")
        self.label_maker()
        question, answer = self.quiz_object.next_question()
        self.real_answer = answer
        if self.quiz_object.question_number < len(self.quiz_object.question_list):
            self.canvas.itemconfig(self.question_id, text=question,font=("Arial",30,"italic"))
        else:
            self.canvas.itemconfig(self.question_id,text="YOU REACHED THE END OF THE QUIZ",font=("Arial",30,"italic"))
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")


    def label_maker(self)->None:
        """This will make the label"""
        label1 = Label(text=f"Score: {self.quiz_object.score}",bg=THEME_COLOR,fg="white",font=("Arial",20,"italic"))
        label1.grid(row=0,column=1)



