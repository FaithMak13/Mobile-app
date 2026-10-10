import random
import tkinter as tk
from tkinter import messagebox

# Language Learning App Dataset
vocabulary = {
    "Spanish": [
        {"word": "Hello", "translation": "Hola"},
        {"word": "Thank you", "translation": "Gracias"},
        {"word": "Goodbye", "translation": "Adiós"},
        {"word": "Please", "translation": "Por favor"},
        {"word": "Good morning", "translation": "Buenos días"},
    ],
    "French": [
        {"word": "Hello", "translation": "Bonjour"},
        {"word": "Thank you", "translation": "Merci"},
        {"word": "Goodbye", "translation": "Au revoir"},
        {"word": "Please", "translation": "S'il vous plaît"},
        {"word": "Good morning", "translation": "Bonjour"},
    ],
    "Shona": [
        {"word": "Hello", "translation": "Mhoro"},
        {"word": "Thank you", "translation": "Ndatenda"},
        {"word": "Goodbye", "translation": "Sara zvakanaka"},
        {"word": "Please", "translation": "Ndapota"},
        {"word": "Good morning", "translation": "Mangwanani"},
    ],
}


class LanguageApp:
    def __init__(self, root):
        """Initialize the application window and launch the first screen."""
        self.root = root
        self.root.title("Language Learning App")
        self.root.geometry("450x500")
        
        # Application state tracking variables
        self.selected_language = "Spanish"
        self.quiz_questions = []
        self.current_question_index = 0
        self.quiz_score = 0
        self.correct_answer = ""
        self.option_buttons = []

        # Start the application on the Main Menu Screen
        self.show_main_menu_screen()

    def clear_screen(self):
        """Destroy all active widgets to prepare for drawing a new screen view."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_main_menu_screen(self):
        """Draw Screen 1: The main menu interface with language selection options."""
        self.clear_screen()

        # Header Label
        title_label = tk.Label(self.root, text="LANGUAGE LEARNING APP", font=("Arial", 16, "bold"), fg="#2C3E50")
        title_label.pack(pady=20)

        # Language Selection UI dropdown frame
        lang_frame = tk.LabelFrame(self.root, text=" 1. Select Target Language ", font=("Arial", 10, "bold"), padx=15, pady=15)
        lang_frame.pack(pady=10, fill="x", padx=40)

        self.lang_var = tk.StringVar(value=self.selected_language)
        for lang in vocabulary.keys():
            radio = tk.Radiobutton(lang_frame, text=lang, variable=self.lang_var, value=lang, font=("Arial", 11))
            radio.pack(anchor="w", pady=2)

        # Action Buttons frame
        action_frame = tk.LabelFrame(self.root, text=" 2. Choose Mode ", font=("Arial", 10, "bold"), padx=15, pady=15)
        action_frame.pack(pady=20, fill="x", padx=40)

        learn_btn = tk.Button(action_frame, text="Learn Vocabulary Screen", font=("Arial", 11), bg="#3498DB", fg="white", command=self.navigate_to_vocabulary)
        learn_btn.pack(fill="x", pady=5)

        quiz_btn = tk.Button(action_frame, text="Take a Quiz Screen", font=("Arial", 11), bg="#2ECC71", fg="white", command=self.navigate_to_quiz_setup)
        quiz_btn.pack(fill="x", pady=5)

        exit_btn = tk.Button(self.root, text="Exit Application", font=("Arial", 10), bg="#E74C3C", fg="white", command=self.root.quit)
        exit_btn.pack(pady=10)

    def navigate_to_vocabulary(self):
        """Save the chosen language state and transition to the vocabulary screen."""
        self.selected_language = self.lang_var.get()
        self.show_vocabulary_screen()

    def show_vocabulary_screen(self):
        """Draw Screen 2: Vocabulary Display layout detailing word translations."""
        self.clear_screen()

        # Title block
        title_text = f"Learn {self.selected_language}"
        header = tk.Label(self.root, text=title_text, font=("Arial", 16, "bold"), fg="#2C3E50")
        header.pack(pady=15)

        # Dynamic Grid container for tracking dictionary item output
        grid_frame = tk.Frame(self.root, padx=10, pady=10)
        grid_frame.pack(fill="both", expand=True, padx=40)

        # Header row columns for table
        tk.Label(grid_frame, text="English Word", font=("Arial", 11, "bold"), borderwidth=1, relief="solid", width=15, bg="#ECF0F1").grid(row=0, column=0, sticky="nsew")
        tk.Label(grid_frame, text="Translation", font=("Arial", 11, "bold"), borderwidth=1, relief="solid", width=15, bg="#ECF0F1").grid(row=0, column=1, sticky="nsew")

        # Iterating data into table grid structures
        for index, item in enumerate(vocabulary[self.selected_language], start=1):
            tk.Label(grid_frame, text=item["word"], font=("Arial", 11), borderwidth=1, relief="solid", padx=5, pady=5).grid(row=index, column=0, sticky="nsew")
            tk.Label(grid_frame, text=item["translation"], font=("Arial", 11, "italic", "bold"), fg="#2980B9", borderwidth=1, relief="solid", padx=5, pady=5).grid(row=index, column=1, sticky="nsew")

        # Back Button navigation linking back to main menu
        back_btn = tk.Button(self.root, text="← Back to Main Menu", font=("Arial", 11), bg="#7F8C8D", fg="white", command=self.show_main_menu_screen)
        back_btn.pack(pady=25)

    def navigate_to_quiz_setup(self):
        """Set up quiz parameters, shuffle questions, and transition to the quiz screen."""
        self.selected_language = self.lang_var.get()
        self.quiz_questions = vocabulary[self.selected_language][:]
        random.shuffle(self.quiz_questions)
        
        self.current_question_index = 0
        self.quiz_score = 0
        self.show_quiz_screen()

    def show_quiz_screen(self):
        """Draw Screen 3: Interactive Quiz window with dynamic multiple-choice buttons."""
        self.clear_screen()

        # Guard evaluation block checking if all questions are finished
        if self.current_question_index >= len(self.quiz_questions):
            self.show_quiz_results()
            return

        current_item = self.quiz_questions[self.current_question_index]
        self.correct_answer = current_item["translation"]

        # Status tracking tracking numbers
        progress_text = f"Question {self.current_question_index + 1} of {len(self.quiz_questions)}"
        progress_lbl = tk.Label(self.root, text=progress_text, font=("Arial", 10, "italic"), fg="#7F8C8D")
        progress_lbl.pack(pady=5)

        # Question text prompt mapping
        prompt_text = f"What is '{current_item['word']}' in {self.selected_language}?"
        prompt_lbl = tk.Label(self.root, text=prompt_text, font=("Arial", 13, "bold"), fg="#2C3E50", wraplength=350)
        prompt_lbl.pack(pady=15)

        # Generate multiple-choice options lists
        wrong_answers = [
            entry["translation"] for entry in vocabulary[self.selected_language]
            if entry["translation"] != self.correct_answer
        ]

        options = [self.correct_answer]
        if wrong_answers:
            options.append(random.choice(wrong_answers))

        for entry in vocabulary[self.selected_language]:
            answer = entry["translation"]
            if answer not in options:
                options.append(answer)
            if len(options) == 3:
                break

        random.shuffle(options)

        # Draw response choice buttons onto UI
        self.option_buttons = []
        for opt in options:
            btn = tk.Button(self.root, text=opt, font=("Arial", 11), bg="#F1C40F", activebackground="#F39C12", pady=8, command=lambda o=opt: self.evaluate_quiz_choice(o))
            btn.pack(fill="x", padx=60, pady=6)
            self.option_buttons.append(btn)

        # Cancel link button back out to menu
        cancel_btn = tk.Button(self.root, text="Cancel Quiz", font=("Arial", 10), bg="#95A5A6", fg="white", command=self.show_main_menu_screen)
        cancel_btn.pack(pady=30)

    def evaluate_quiz_choice(self, user_selection):
        """Check if selection matches the solution, display feedback popups, and advance index."""
        if user_selection == self.correct_answer:
            self.quiz_score += 1
            messagebox.showinfo("Result", "Correct! Well done.")
        else:
            messagebox.showerror("Result", f"Not quite. The correct answer is '{self.correct_answer}'.")

        # Step to next index element and redraw the quiz pane screen
        self.current_question_index += 1
        self.show_quiz_screen()

    def show_quiz_results(self):
        """Display final quiz performance metrics and options to return home."""
        self.clear_screen()

        header = tk.Label(self.root, text="Quiz Completed!", font=("Arial", 18, "bold"), fg="#27AE60")
        header.pack(pady=30)

        total_questions = len(self.quiz_questions)
        percentage = (self.quiz_score / total_questions) * 100

        score_text = f"Your Score: {self.quiz_score} / {total_questions}"
        score_lbl = tk.Label(self.root, text=score_text, font=("Arial", 14, "bold"))
        score_lbl.pack(pady=10)

        pct_text = f"Result Percentage: {percentage:.0f}%"
        pct_lbl = tk.Label(self.root, text=pct_text, font=("Arial", 14), fg="#2980B9")
        pct_lbl.pack(pady=10)

        return_btn = tk.Button(self.root, text="Return to Main Menu", font=("Arial", 12, "bold"), bg="#34495E", fg="white", pady=5, command=self.show_main_menu_screen)
        return_btn.pack(pady=40)


def main():
    """Instantiate the root app configuration window and launch loops."""
    root = tk.Tk()
    app = LanguageApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

