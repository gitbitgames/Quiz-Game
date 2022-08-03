import tkinter as tk

THEME_COLOR = "#375362"

class QuizUI:
    def __init__(self, quiz_list):
        self.quiz = quiz_list
        self.game_over = False
        self.root = tk.Tk()
        self.root.title('Trivia Game')
        self.root.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = tk.Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Hello',
            fill=THEME_COLOR,
            font=("arial", 20, "italic")
        )

        true_image=tk.PhotoImage(file="images/true.png")
        false_image=tk.PhotoImage(file="images/false.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0, command=lambda: self.check_answer(True))
        self.false_button = tk.Button(image=false_image, highlightthickness=0, command=lambda: self.check_answer(False))
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        q_text = self.quiz.next_question()
        if q_text is False:
            self.end_game()
            self.game_over = True
            return
        self.canvas.itemconfig(self.question_text, text=q_text)

    def check_answer(self, boolean):
        if self.game_over == True:
            return
        checking = self.quiz.check_answer(boolean)
        if checking:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.root.after(1000, self.get_next_question)

        
    def end_game(self):
        game_end = f"Your final score is: {self.quiz.score}/{self.quiz.question_number}"
        self.canvas.itemconfig(self.question_text, text=game_end)