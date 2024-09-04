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

    if not isinstance(word, str):
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


if __name__ == "__main__":
    pass
