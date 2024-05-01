#Number guessing game
import random
import tkinter as tk
from tkinter import messagebox

MIN_NUMBER = 1
MAX_NUMBER = 200
MAX_GUESSES = 6

class NumberGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Guessing Game")
        self.geometry("300x200")
        self.number = random.randint(MIN_NUMBER, MAX_NUMBER)
        self.guesses_taken = 0
        
        self.intro_label = tk.Label(self, text="May I ask you for your name?")
        self.intro_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()
        self.start_button = tk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.pack()
        self.guess_label = tk.Label(self, text="Go ahead. Guess!")
        self.guess_label.pack()
        self.guess_entry = tk.Entry(self)
        self.guess_entry.pack()
        self.guess_button = tk.Button(self, text="Submit Guess", command=self.submit_guess)
        self.guess_button.pack()

    def start_game(self):
        self.name = self.name_entry.get()
        messagebox.showinfo("Instructions", f"Hello {self.name}! Guess a number between {MIN_NUMBER} and {MAX_NUMBER}. You have {MAX_GUESSES} guesses.")

    def submit_guess(self):
        try:
            guess = int(self.guess_entry.get())
            if MIN_NUMBER <= guess <= MAX_NUMBER:
                self.guesses_taken += 1
                if guess < self.number:
                    messagebox.showinfo("Result", "The guess is too low")
                elif guess > self.number:
                    messagebox.showinfo("Result", "The guess is too high")
                elif guess == self.number:
                    messagebox.showinfo("Result", f"Good job, {self.name}! You guessed my numpip install mediapipeber in {self.guesses_taken} guesses!")
                    self.reset_game()
            else:
                messagebox.showerror("Error", f"Silly Goose! That number isn't in the range ({MIN_NUMBER} - {MAX_NUMBER})")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

        if self.guesses_taken >= MAX_GUESSES:
            messagebox.showinfo("Result", f"Sorry, {self.name}. You've used all your guesses. The number was {self.number}")
            self.reset_game()

    def reset_game(self):
        self.number = random.randint(MIN_NUMBER, MAX_NUMBER)
        self.guesses_taken = 0
        self.guess_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = NumberGuessingGame()
    app.mainloop()

