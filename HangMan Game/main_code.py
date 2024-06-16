import random
import os
import tkinter as tk
from tkinter import messagebox

def load_word_library(filename):
    """
    Load word and hint pairs from a text file.

    Args:
        filename (str): Path to the word library file.

    Returns:
        list: A list of tuples containing word and hint pairs.
    """
    word_hint_pairs = []
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, 1):
            parts = line.strip().split(',', maxsplit=1)
            if len(parts) != 2:
                print(f"Error: Line {line_number} in the word library file does not have the correct format. Skipping this line.")
                continue
            word, hint = parts
            word_hint_pairs.append((word.strip().lower(), hint.strip()))
    return word_hint_pairs

def choose_word(word_hint_pairs):
    """
    Choose a random word and hint pair from the given list.

    Args:
        word_hint_pairs (list): List of tuples containing word and hint pairs.

    Returns:
        tuple: A randomly chosen word and hint pair.
    """
    return random.choice(word_hint_pairs)

def display_word(word, guessed_letters):
    """
    Create a display string for the word with guessed letters revealed.

    Args:
        word (str): The word to be guessed.
        guessed_letters (list): List of letters that have been guessed correctly.

    Returns:
        str: A string representing the current state of the word with guessed letters revealed.
    """
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

class WordGuessingGame:
    def __init__(self, root, word, hint):
        self.root = root
        self.word = word
        self.hint = hint
        self.guessed_letters = []
        z = int((1 + len(word)) / 2)
        self.max_attempts = z + 2
        self.remaining_attempts = self.max_attempts
        
        self.setup_gui()
        
    def setup_gui(self):
        self.root.title("Word Guessing Game")
        
        self.hint_label = tk.Label(self.root, text=f"Hint: {self.hint}", font=("Helvetica", 14), fg="black")
        self.hint_label.pack(pady=10)
        
        self.word_label = tk.Label(self.root, text=display_word(self.word, self.guessed_letters), font=("Helvetica", 18))
        self.word_label.pack(pady=10)
        
        self.prompt_label = tk.Label(self.root, text="Enter a character:", font=("Helvetica", 14))
        self.prompt_label.pack(pady=5)
        
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)
        
        self.letter_entry = tk.Entry(self.input_frame, font=("Helvetica", 14))
        self.letter_entry.grid(row=0, column=0, padx=5)
        
        self.guess_button = tk.Button(self.input_frame, text="Guess", command=self.make_guess, font=("Helvetica", 14))
        self.guess_button.grid(row=0, column=1, padx=5)
        
        self.feedback_label = tk.Label(self.root, text="", font=("Helvetica", 14))
        self.feedback_label.pack(pady=10)
        
        self.attempts_label = tk.Label(self.root, text=f"Attempts remaining: {self.remaining_attempts}", font=("Helvetica", 14))
        self.attempts_label.pack(pady=10)
        
        self.stickman_canvas = tk.Canvas(self.root, width=300, height=200, bg="white")
        self.stickman_canvas.pack(pady=10)
        
        self.draw_stickman()

    def make_guess(self):
        guess = self.letter_entry.get().lower()
        self.letter_entry.delete(0, tk.END)
        
        if len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                self.feedback_label.config(text="You already guessed that letter!", fg="orange")
                self.root.after(2000, lambda: self.feedback_label.config(text=""))
            elif guess in self.word:
                self.guessed_letters.append(guess)
                self.word_label.config(text=display_word(self.word, self.guessed_letters))
                self.feedback_label.config(text="Correct Guess!", fg="green")
                self.root.after(2000, lambda: self.feedback_label.config(text=""))
                
                if set(self.guessed_letters) >= set(self.word):
                    messagebox.showinfo("Congratulations!", f"You guessed the word '{self.word}'!")
                    self.root.quit()
            else:
                self.remaining_attempts -= 1
                self.attempts_label.config(text=f"Attempts remaining: {self.remaining_attempts}")
                self.feedback_label.config(text="Incorrect Guess!", fg="red")
                self.root.after(2000, lambda: self.feedback_label.config(text=""))
                self.draw_stickman()
                
                if self.remaining_attempts == 0:
                    messagebox.showinfo("Game Over", f"Sorry, you ran out of attempts. The word was '{self.word}'.")
                    self.root.quit()
        else:
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")

    def draw_stickman(self):
        self.stickman_canvas.delete("all")
        stickman_parts = [
            "  _______",
            " |/      |",
            " |      (o)",
            " |     --|--",
            " |       |",
            " |      / \\",
            " |",
            "_|___"
        ]
        
        fraction = (self.max_attempts - self.remaining_attempts) / self.max_attempts
        parts_to_display = int(fraction * len(stickman_parts))
        
        for i in range(parts_to_display):
            self.stickman_canvas.create_text(150, 20 + i * 20, text=stickman_parts[i], font=("Courier", 14, "bold"), anchor="w")

def main():
    print("Welcome to the Word Guessing Game!")
    word_library_path = input("Enter the path to the word library file: ")

    if not os.path.isfile(word_library_path):
        print("Error: Word library file not found.")
        return

    word_hint_pairs = load_word_library(word_library_path)
    word, hint = choose_word(word_hint_pairs)

    root = tk.Tk()
    game = WordGuessingGame(root, word, hint)
    root.mainloop()

if __name__ == "__main__":
    main()
