import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
import time


class Quiz:

    def __init__(self, root):
        self.root = root
        self.root.title("QUIZ")
        self.root.geometry("1350x690+0+0")
        self.root.configure(background = "white")
        self.root.resizable(0,0)
        

#____________________________SET OF QUESTIONS, OPTIONS, CORRECT ANSWERS AND RANDOM QUESTION GENERATOR___________________________


        self.questions=["Which is the sixth planet away from the Sun?",
                        "Which of the following is not one of the 7 Continents?",
                        "Human body consist of how many bones?",
                        "Animals which eat both plants & animals, are called?",
                        "What was the national capital of India before Delhi?",
                        "India celebrated its ____ Independence Day on August 15, 2020?",
                        "How many Newton's law of motion are there?",
                        "Which sport is not a part of the Olympics?",
                        "How many times did India win the Cricket World Cup?",
                        "In which year did India celebrated its first Republic Day?",]

        self.options =[['Uranus','Saturn','Jupiter','Neptune'],
                       ['Africa','Arctic','Europe','North America'],
                       ['208','210','204','206'],
                       ['Herbivores','Carnivores','Insectivores','Omnivores'],
                       ['Calcutta','Madras','Bombay','Hyderabad'],
                       ['73rd','75th','72nd','74th'],
                       ['1','2','3','4'],
                       ['Tennis','Golf','Chess','Football'],
                       ['3','2','1','0'],
                       ['1949','1950','1947','1948']]

        self.correct_answers = [1, 1, 3, 3, 0, 0, 2, 2, 1, 1]
        
        
        # OUR RANDOM QUESTION GENERATOR FUNCTION
        self.answer_index =[]
        def Generator():
            while(len(self.answer_index)<10):
                x = random.randint(0,9)
                if x in self.answer_index:
                    continue
                else:
                    self.answer_index.append(x)
                    
                    
                    
#______________________________________________RESULT INTERFACE, FINAL INTERFACE________________________________________________


        # END OF THE QUIZ DESTROY THE INTERFACE AND DISPLAY RESULT INTERFACE
        def Result(score):
            question_lbl.destroy()
            option_1.destroy()
            option_2.destroy()
            option_3.destroy()
            option_4.destroy()
            quiz_lbl.destroy()
            statusbar_lbl.destroy()
            
        # RESULT IMAGE AND LABEL DEPENDING UPON YOUR SCORE
            if score == 10:
                result_img = ImageTk.PhotoImage(Image.open("quiz_logo_3.jpg"))
                result_lbl = Label(root, image = result_img, bg="white", bd=0, font=("Consolas",20,"bold"), compound=TOP,
                                   text="You Just Nailed It! " + Username + "\nYou Scored " + str(score), fg="#3d3d29")
                result_lbl.image = result_img
                result_lbl.pack(pady=(200,0))
                
            elif score >7 and score <10:
                result_img = ImageTk.PhotoImage(Image.open("quiz_logo_3.jpg"))
                result_lbl = Label(root, image = result_img, bg="white", bd=0, font=("Consolas",20,"bold"), compound=TOP,
                                   text= "You Are Amazing! " + Username + "\nYou Scored " + str(score), fg="#3d3d29")
                result_lbl.image = result_img
                result_lbl.pack(pady=(200,0))
                
            elif score >4 and score <8:
                result_img = ImageTk.PhotoImage(Image.open("quiz_logo_3.jpg"))
                result_lbl = Label(root, image = result_img, bg="white", bd=0, font=("Consolas",20,"bold"), compound=TOP,
                                   text= "You Can Do Better! " + Username + "\nYou Scored " + str(score), fg="#3d3d29")
                result_lbl.image = result_img
                result_lbl.pack(pady=(200,0))
                
            else:
                result_img = ImageTk.PhotoImage(Image.open("quiz_logo_3.jpg"))
                result_lbl = Label(root, image = result_img, bg="white", bd=0, font=("Consolas",20,"bold"), compound=TOP,
                                   text="You Need To Improve! " + Username + "\nYou Scored " + str(score), fg="#3d3d29")
                result_lbl.image = result_img
                result_lbl.pack(pady=(200,0))
                
                

#_________________________________________________IMPORTANT FUNCTIONS___________________________________________________________

                
        # FUNCTION TO CROSS CHECK SELECTED ANSWERS WITH CORRECT ANSWERS AND TALLY THE SCORE
        def FinalScore():
            x=0
            score=0
            for i in self.answer_index:
                if self.selected_answers[x] == self.correct_answers[i]:
                    score += 1
                x+=1
            Result(score)
            
            
        # FUNCTION TO ITERATE THROUGH QUESTIONS AND STORE YOUR SELECTED ANSWERS
        self.selected_answers = []
        self.current_question = 1
        def Selected():
            global option_var, question_lbl, option_1, option_2, option_3, option_4
            x = option_var.get()
            self.selected_answers.append(x)
            option_var.set(-1)
            if self.current_question < 10:
                question_lbl.config(text=self.questions[self.answer_index[self.current_question]])
                option_1["text"] = self.options[self.answer_index[self.current_question]][0]
                option_2["text"] = self.options[self.answer_index[self.current_question]][1]
                option_3["text"] = self.options[self.answer_index[self.current_question]][2]
                option_4["text"] = self.options[self.answer_index[self.current_question]][3]
                self.current_question += 1
                statusbar_lbl["text"] = "Question " + str(self.current_question) + " of 10"
            else:
                FinalScore() # CALLING THE FUNCTION ONCE ALL QUESTIONS ARE OVER
                
                
                
#________________________________________QUIZ TIME THE QUESTIONNAIRE INTERFACE__________________________________________________                


        # YOU ARE NOW INTO QUIZ
        def IntoQuiz():
            
            global question_lbl, option_1, option_2, option_3, option_4, quiz_lbl, option_var,statusbar_lbl
            
            # QUIZ TIME IMAGE
            quiz_img = ImageTk.PhotoImage(Image.open("quiz_time.jpg"))
            quiz_lbl = Label(root, image = quiz_img, bd=0, bg="white")
            quiz_lbl.image = quiz_img
            quiz_lbl.pack(pady=(30,20))
            
            # QUESTION LABEL
            question_lbl = Label(root, text=self.questions[self.answer_index[0]], font = ("Consolas",26,"bold"),
                                 width=500, justify="center", bg="white", fg="#3d3d29")
            question_lbl.pack(pady=(20,50))
            
            
            # FOR OPTIONS WE ARE TAKING RADIOBUTTONS
            option_var = IntVar()
            option_var.set(-1)
            option_1 = Radiobutton(root, text=self.options[self.answer_index[0]][0], command=Selected,
                                   font = ("Consolas",18,"bold"), value=0, variable = option_var, bg="white", fg="#3d3d29" )
            option_1.place(x=220, y=520)

            option_2 = Radiobutton(root, text=self.options[self.answer_index[0]][1], command=Selected,
                                   font = ("Consolas",18,"bold"), value=1, variable = option_var, bg="white", fg="#3d3d29" )
            option_2.place(x=490, y=520)

            option_3 = Radiobutton(root, text=self.options[self.answer_index[0]][2], command=Selected,
                                   font = ("Consolas",18,"bold"), value=2, variable = option_var, bg="white", fg="#3d3d29" )
            option_3.place(x=760, y=520)

            option_4 = Radiobutton(root, text=self.options[self.answer_index[0]][3], command=Selected,
                                   font = ("Consolas",18,"bold"), value=3, variable = option_var , bg="white", fg="#3d3d29")
            option_4.place(x=1030, y=520)
            
            # STATUS BAR LABEL TO KEEP COUNT OF QUESTIONS
            statusbar_lbl = Label(root,text="Question 1 of 10",font = ("Consolas",20,"bold"), bg="white", fg="#3d3d29")
            statusbar_lbl.pack(side=BOTTOM, pady=(0,20))
            
            
            
#_____________________INSTRUCTIONS INTERFACE, THIS IS THE SECOND INTERFACE YOU SEE AFTER WELCOME INTERFACE______________________
        
    
        # DESTROY THE WELCOME INTERFACE AND START THE INSTRUCTIONS INTERFACE
        def Start():
            self.username_txt.destroy()
            self.quiz_txt.destroy()
            self.quiz_lbl.destroy()
            self.name_txt.destroy()
            self.start_btn.destroy()
            
            # WELCOME LABEL
            welcome_lbl = Label(root, font=("Consolas", 20, "bold"), fg="#3d3d29", bg="white",
                                text="Welcome, "+Username+"!")
            welcome_lbl.pack(pady=(80,50))
            
            # INSTRUCTION LABEL
            instructions_lbl = Label(root,text='''The Quiz consist of 10 questions.\nThere is no time limit to the quiz.
You will get only one chance to select an answer.\nOnce selected the choice cannot be undone so think twice before selecting.
For every correct answer you will get 1 point.\nYour total score will be displayed at last.\nClick "START" when you are ready.''',
                              width=100, font=("Consolas", 20, "bold"), fg="#3d3d29", bg="white")
            instructions_lbl.pack()

            # DESTROY INSTRUCTION INTERFACE AND MOVE TO THE QUIZ
            def QuizStart():
                welcome_lbl.destroy()
                instructions_lbl.destroy()
                time_lbl.destroy()
                start_btn.destroy()
                Generator() # CALLING THE FUNCTION TO GENERATE QUESTIONS RANDOMLY
                IntoQuiz() # YOU MOVE INTO THE QUIZ
            
            # START BUTTON
            start_img = ImageTk.PhotoImage(Image.open("start_2.jpg"))
            start_btn = Button(root, image = self.start_img, relief=FLAT, bd=0, bg="white", command=QuizStart)
            start_btn.pack(pady = (50,50))

            # DATETIME FUNCTION
            def Clock():
                time_lbl.config(text=time.strftime("%c"))
                time_lbl.after(1000, Clock)
                
            # DATETIME LABEL
            time_lbl = Label(root, font=("Consolas", 20, "bold"), fg="#3d3d29", bg="white")
            time_lbl.pack()
            Clock()
            
            
            
#_____________________WELCOME INTERFACE, THIS IS THE FIRST INTERFACE YOU SEE WHEN YOU RUN THE PROGRAM___________________________


        # USERNAME VALIDATION
        def User():
            global Username
            Username = self.name_txt.get()
            if Username != "":
                Start() # AFTER USERNAME VALIDATION YOU MOVE TO INSTRUCTIONS INTERFACE
            else:
                messagebox.showerror("Invalid Username", "Username cannot be empty..!")        

        # WELCOME LABEL
        self.quiz_txt = Label(self.root, text="Welcome To The", font=("Consolas", 30, "bold"), bg = "white", fg="#3d3d29")
        self.quiz_txt.pack(pady=30)
        
        # QUIZ IMAGE
        self.quiz_img = ImageTk.PhotoImage(Image.open("quiz_logo_2.jpg"))
        self.quiz_lbl = Label(self.root, image = self.quiz_img, bg = "white")
        self.quiz_lbl.pack(pady=10)

        # USERNAME LABEL
        self.username_txt = Label(self.root, text="Enter Your Name & Click Start", font=("Consolas", 15, "bold"), bg = "white")
        self.username_txt.pack(pady=20)
        
        # USERNAME TEXTBOX
        self.name_txt = Entry(self.root, font=("Consolas", 16, "bold"), width=18, justify=CENTER, bg="#70db70", bd=0)
        self.name_txt.pack(pady=10)
        self.name_txt.get()

        # START BUTTON
        self.start_img = ImageTk.PhotoImage(Image.open("start_2.jpg"))
        self.start_btn = Button(self.root, image = self.start_img, relief=FLAT, bd=0, bg="white", command=User)
        self.start_btn.pack(pady=20)

#_______________________________________________________________________________________________________________________________      


if __name__ == "__main__":
    root = Tk()
    application = Quiz(root)
    root.mainloop()
