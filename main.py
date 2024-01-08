import tkinter as tk
from tkinter import messagebox
import random


class NumberGuessingGame:
    def __init__(self, master, difficulty):
        self.master = master
        self.master.title("Number Guessing Game")

        self.difficulty = difficulty
        self.secret_number = self.generate_secret_number()

        self.label = tk.Label(self.master, text="Guess the number:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.master)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess)
        self.guess_button.pack()

    def generate_secret_number(self):
        if self.difficulty == "easy":
            return random.randint(1, 10)
        elif self.difficulty == "medium":
            return random.randint(1, 50)
        elif self.difficulty == "hard":
            return random.randint(1, 100)
        else:
            return random.randint(1, 50)

    def make_guess(self):
        try:
            guess = int(self.entry.get())

            if guess == self.secret_number:
                messagebox.showinfo("Congratulations!", "Correct! You guessed the number.")
                self.master.destroy()
            elif guess < self.secret_number:
                messagebox.showinfo("Incorrect", "Try a higher number.")
            else:
                messagebox.showinfo("Incorrect", "Try a lower number.")

        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")


def start_game(difficulty):
    game_window = tk.Toplevel(root)
    NumberGuessingGame(game_window, difficulty)


root = tk.Tk()
root.title("Game Selection")

difficulty_label = tk.Label(root, text="Select Difficulty:")
difficulty_label.pack(pady=10)

easy_button = tk.Button(root, text="Easy", command=lambda: start_game("easy"))
easy_button.pack()

medium_button = tk.Button(root, text="Medium", command=lambda: start_game("medium"))
medium_button.pack()

hard_button = tk.Button(root, text="Hard", command=lambda: start_game("hard"))
hard_button.pack()

easy_label = tk.Label(root, text="Easy - guess number between 1-10")
easy_label.pack(pady=5)

medium_label = tk.Label(root, text="Medium - guess number between 1-50")
medium_label.pack(pady=5)

hard_label = tk.Label(root, text="Hard - guess number between 1-100")
hard_label.pack(pady=5)
root.mainloop()
