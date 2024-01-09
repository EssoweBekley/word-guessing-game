import tkinter as tk
from tkinter import messagebox
import random

# Read words from a text file
with open('words_alpha.txt', 'r') as file:
    word_list = [line.strip() for line in file]

class WordGuessGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Guessing Game")
        self.master.geometry("400x200")  # Set the initial size (width x height)

        self.word_label = tk.Label(master, text="")
        self.word_label.pack()

        self.guess_entry = tk.Entry(master)
        self.guess_entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack()

        self.play_again_button = tk.Button(master, text="Play Again", command=self.play_again)
        self.play_again_button.pack()

        self.difficulty_var = tk.StringVar(master)
        self.difficulty_var.set("Moderate")  # Default difficulty
        self.difficulty_label = tk.Label(master, text="Select Difficulty:")
        self.difficulty_label.pack()
        self.difficulty_menu = tk.OptionMenu(master, self.difficulty_var, "Easy", "Moderate", "Hard")
        self.difficulty_menu.pack()

        self.debug = False

        self.pick_random()
        self.choose_blur()
        self.display_word()

    def pick_random(self):
        difficulty_mapping = {"Easy": 0.2, "Moderate": 0.45, "Hard": 0.65}
        self.difficulty = difficulty_mapping[self.difficulty_var.get()]
        self.word = random.choice(tuple(word_list))
        self.char_list = list(self.word)

    def choose_blur(self):
        self.blurred = round(len(self.char_list) * self.difficulty)
        self.blurred_chars = random.sample(self.char_list, self.blurred)

    def display_word(self):
        displayed_word = ""
        for char in self.char_list:
            if char in self.blurred_chars:
                displayed_word += "_"
            else:
                displayed_word += char
        self.word_label.config(text=displayed_word)

    def check_guess(self):
        guess = self.guess_entry.get()
        if guess == self.word:
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Sorry, the answer was {self.word}")

    def play_again(self):
        self.pick_random()
        self.choose_blur()
        self.display_word()

if __name__ == "__main__":
    root = tk.Tk()
    game = WordGuessGame(root)
    root.mainloop()
