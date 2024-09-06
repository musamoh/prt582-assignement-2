"""
  This is the main file for the Scrabble Score game using TDD and automated unit testing tool in python

    The main file contains the following functions:
    - validate_word: This function validates the word to ensure it is a valid dictionary word,
    a single word and a string and not empty
    - score: This function calculates the score of a word based on the scrabble game

    Author: Musa Mohammed
    email: s384546@students.cdu.edu.au
"""

from wordfreq import word_frequency
from typing import List, Optional
import random
from tkinter import messagebox
import tkinter as tk

from exception import (
    EmptyStringError,
    InvalidDictionaryWordError,
    MultipleWordError,
    NonStringInputError,
    DuplicateInputError,
    InvalidInputLengthError,
)

ALPHABETS = {
    "A": 1,
    "E": 1,
    "I": 1,
    "O": 1,
    "U": 1,
    "L": 1,
    "N": 1,
    "R": 1,
    "S": 1,
    "T": 1,
    "D": 2,
    "G": 2,
    "B": 3,
    "C": 3,
    "M": 3,
    "P": 3,
    "F": 4,
    "H": 4,
    "V": 4,
    "W": 4,
    "Y": 4,
    "K": 5,
    "J": 8,
    "X": 8,
    "Q": 10,
    "Z": 10,
}


def is_numeric_string(s: str) -> bool:
    """
    Check if a string is numeric
    :param s: str
    :return: bool
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def validate_word(word: str, word_list: List, random_number: Optional[int]) -> None:
    """
    validate the word to ensure it is a valid dictionary word,
    a single word and a string and not empty
    :param word:
    :param word_list:
    :param random_number:
    :return: None
    """

    if not word:
        raise EmptyStringError("Empty string is not allowed")

    if is_numeric_string(word):
        raise NonStringInputError("Non string input is not allowed")
    word = word.strip()
    if len(word.split()) > 1:
        raise MultipleWordError("Only one word is allowed")

    meaning = word_frequency(word, "en")
    if meaning <= 0:
        raise InvalidDictionaryWordError(f"Invalid dictionary word: {word}")
    if word in word_list:
        raise DuplicateInputError(f"Duplicate input: {word} was mentioned before")
    if len(word) != random_number:
        raise InvalidInputLengthError(
            f"Invalid input length: word length should be {random_number} characters"
        )


def score(word: str) -> int:
    """
    Calculate the score of a word based on the scrabble game
    :param word:
    :return: int
    """
    total = sum([ALPHABETS.get(i.upper()) for i in word.strip()])
    return total


class ScrabbleGame:
    def __init__(self):
        self.after_id = None
        self.random_number = None
        self.word_list = []
        self.top = tk.Tk()
        self.top.title("Scrabble Score")
        self.top.geometry("500x400")

        # Center the window
        window_width = self.top.winfo_reqwidth()
        window_height = self.top.winfo_reqheight()
        position_right = int(self.top.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.top.winfo_screenheight() / 2 - window_height / 2)
        self.top.geometry("+{}+{}".format(position_right, position_down))

        # Instruction label
        tk.Label(
            self.top, text="You have 15 seconds to enter a word", bg="lightblue"
        ).pack()

        # Countdown timer label
        self.lab = tk.Label(self.top, width=6, bg="orange")
        self.lab.pack()

        # Separator label
        tk.Label(self.top, text="-" * 30).pack()

        # Display expected word length
        self.prompt_label = tk.Label(self.top, text="", bg="blue")
        self.prompt_label.pack()

        # Input field
        self.entry_1 = tk.Entry(self.top, width=20)
        self.entry_1.pack()
        self.entry_1.focus_set()

        # Submit and Exit buttons
        tk.Button(
            self.top,
            bg="lightyellow",
            text="Submit",
            command=self.entry_get,
            activebackground="lightblue",
        ).pack()
        tk.Button(
            self.top,
            bg="red",
            text="Exit",
            command=self.exit_game,
            activebackground="white",
        ).pack()

        # Score label
        self.score_label = tk.Label(self.top, text="Score: 0", bg="green")
        self.score_label.pack()

        # Initialize variables
        self.ctr = 15
        self.attempts = 0
        self.total_score = 0

        # Generate the first prompt
        self.generate_prompt()

        # Start the countdown timer
        self.start_timer()
        self.top.mainloop()

    def start_timer(self):
        self.cancel_timer()
        self.update_timer()

    def cancel_timer(self):
        if self.after_id is not None:
            self.top.after_cancel(self.after_id)
            self.after_id = None

    def update_timer(self):
        self.ctr -= 1
        self.lab.config(text=str(self.ctr))  # Update the timer display
        if self.ctr > 0:
            self.after_id = self.top.after(1000, self.update_timer)
        else:
            self.game_over()

    def game_over(self):
        print("Time's up!")
        self.entry_get()

    def generate_prompt(self):
        # Generate a random word length between 1 and 15
        self.random_number = random.randint(1, 15)
        # Update the prompt label with the required word length
        self.prompt_label.config(text=f"Enter a word of length {self.random_number}")

    def entry_get(self):
        word = self.entry_1.get()
        try:
            validate_word(word, self.word_list, self.random_number)
            if len(word) == int(self.random_number):

                self.score_label.config(
                    text=f"Correct! You entered: {word}", bg="green"
                )
                self.total_score += score(word)
                if self.ctr > 0:
                    self.total_score += 2
                self.word_list.append(word)
                self.generate_prompt()
            else:
                self.score_label.config(
                    text=f"Incorrect. You entered: {word}", bg="red"
                )
        except (
            EmptyStringError,
            NonStringInputError,
            MultipleWordError,
            InvalidDictionaryWordError,
            NonStringInputError,
            DuplicateInputError,
            InvalidInputLengthError,
        ) as e:
            self.score_label.config(
                text=str(e), bg="red"
            )  # Display exception message on a red background

        self.attempts += 1
        if self.attempts < 10:
            self.entry_1.delete(0, tk.END)
            self.ctr = 15
            self.generate_prompt()
            self.start_timer()
        else:
            self.score_label.config(text=f"Game over! Total score: {self.total_score}")
            self.exit_game()

    def exit_game(self):
        messagebox.showinfo("Final Score", f"Your final score is: {self.total_score}")
        self.top.quit()


if __name__ == "__main__":
    CT = ScrabbleGame()
