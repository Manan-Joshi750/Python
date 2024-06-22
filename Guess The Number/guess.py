import tkinter as tk
import random
import time

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.target_number = random.randint(1, 100)
        self.attempts = 0
        self.max_attempts = 5

        self.label_hint = tk.Label(master, text="Guess a number between 1 and 100", fg="blue")
        self.label_hint.pack(pady=10)

        self.label_attempts = tk.Label(master, text=f"Attempts left: {self.max_attempts - self.attempts}", fg="green")
        self.label_attempts.pack(pady=5)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.button = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.button.pack(pady=5)

        self.result_label = tk.Label(master, text="", fg="black")
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            remaining_attempts = self.max_attempts - self.attempts
            self.label_attempts.config(text=f"Attempts left: {remaining_attempts}")

            if guess < self.target_number:
                if self.target_number - guess <= 5:
                    self.show_message("Ahh, you're very close!", "orange")
                elif self.target_number - guess <= 10:
                    self.show_message("Alright... you are close.", "brown")
                else:
                    self.show_message("Too low! Try again.", "red")
            elif guess > self.target_number:
                if guess - self.target_number <= 5:
                    self.show_message("Ahh, you're very close!", "orange")
                elif guess - self.target_number <= 10:
                    self.show_message("Alright... you are close.", "brown")
                else:
                    self.show_message("Too high! Try again.", "red")
            else:
                self.show_message(f"Congratulations! You guessed it in {self.attempts} attempts.", "green")
                self.button.config(state=tk.DISABLED)
                return

            if self.attempts >= self.max_attempts:
                self.show_message(f"Sorry, you've run out of attempts. The number was {self.target_number}.", "purple")
                self.button.config(state=tk.DISABLED)
        except ValueError:
            self.show_message("Please enter a valid number.", "blue")

    def show_message(self, message, color):
        self.result_label.config(text=message, fg=color)
        self.master.update()
        time.sleep(2)
        self.result_label.config(text="", fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()