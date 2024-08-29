from wordfreq import word_frequency

from exception import (
    EmptyStringError,
    InvalidDictionaryWordError,
    MultipleWordError,
    NonStringInputError,
)

alphabeth = {
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


def validate_word(word: str) -> None:
    """
    validate the word to ensure it is a valid dictionary word,
    a single word and a string and not empty
    :param word:
    :return: None
    """

    if not word:
        raise EmptyStringError("Empty string is not allowed")

    if not isinstance(word, str):
        raise NonStringInputError("Non string input is not allowed")
    word = word.strip()
    if len(word) > 1:
        raise MultipleWordError("Only one word is allowed")

    meaning = word_frequency(word, "en")
    if meaning <= 0:
        raise InvalidDictionaryWordError(f"Invalid dictionary word: {word}")


def score(word: str) -> int:
    """
    Calculate the score of a word based on the scrabble game
    :param word:
    :return: int
    """
    validate_word(word)
    total = sum(
        [alphabeth.get(i.upper()) for i in word]
    )  # pylint: disable=consider-using-generator
    return total
