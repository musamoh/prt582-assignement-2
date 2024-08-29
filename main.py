from wordfreq import word_frequency

from exception import EmptyStringError, InvalidDictionaryWordError, NonStringInputError

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

    if not word:
        raise EmptyStringError("Empty string is not allowed")

    if not isinstance(word, str):
        raise NonStringInputError("Non string input is not allowed")
    word = word.strip()
    meaning = word_frequency(word, "en")
    if meaning <= 0:
        raise InvalidDictionaryWordError(f"Invalid dictionary word: {word}")


def score(word: str) -> int:
    validate_word(word)
    total = sum([alphabeth.get(i.upper()) for i in word])
    return total
