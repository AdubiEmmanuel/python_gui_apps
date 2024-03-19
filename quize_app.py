import tkinter as tk

questions = {
    "What is 2+2?": "4",
    "What is the capital of France?": "Paris",
    "What is the largest mammal?": "Blue whale",
    "What is the closest planet to the Sun?": "Mercury",
}

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Quiz App")

        self.question_label = tk.Label(root, text="", font=("Arial", 12))
        self.question_label.pack()

        self.answer_entry = tk.Entry(root)
        self.answer_entry.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.score_label = tk.Label(root, text="")
        self.score_label.pack()

        self.questions = list(questions.items())
        self.current_question = -1
        self.score = 0
        self.next_question()

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            question, answer = self.questions[self.current_question]
            self.question_label.config(text=question)
        else:
            self.question_label.config(text="Quiz Finished")
            self.score_label.config(text=f"Your score: {self.score}/{len(self.questions)}")

    def check_answer(self):
        answer = self.answer_entry.get()
        _, correct_answer = self.questions[self.current_question]
        if answer.lower() == correct_answer.lower():
            self.score += 1
        self.next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
