"""
This is the test file for the scrabble game
"""

from unittest.mock import patch

import pytest

from exception import (
    EmptyStringError,
    InvalidDictionaryWordError,
    MultipleWordError,
    NonStringInputError,
    DuplicateInputError,
    InvalidInputLengthError,
)
from main import ScrabbleGame
from main import score, validate_word


# Test for valid score
@pytest.mark.parametrize(
    "word, expected",
    [
        ("a", 1),
        ("z", 10),
        ("dog", 5),
        ("cat", 5),
        ("WORLD", 9),
    ],
)
def test_for_score(word, expected):
    assert score(word) == expected


# Test for invalid score
@pytest.mark.parametrize(
    "word, expected",
    [
        ("dog", 0),
        ("cat", 0),
        ("WORLD", 0),
    ],
)
def test_invalid_score(word, expected):
    assert score(word) != expected


# Test for valid dictionary word
def test_for_valid_dictionary_word():
    try:
        validate_word("hello", [], 5)
    except InvalidDictionaryWordError:
        pytest.fail("InvalidDictionaryWordError unexpectedly!")


# Test for invalid word
def test_for_invalid_dictionary_word():
    with pytest.raises(InvalidDictionaryWordError) as e:
        validate_word("Xbause", [], 6)
    assert str(e.value) == "Invalid dictionary word: Xbause"


# Test uppercase letter and lowercase letter are the same
@pytest.mark.parametrize(
    "word",
    [
        ("a"),
        ("z"),
        ("dog"),
        ("cat"),
        ("WORLD"),
    ],
)
def test_score_for_uppercase_and_lowercase(word):
    assert score(word.upper()) == score(word.lower())


# Test for empty string exception
def test_empty_string():
    with pytest.raises(EmptyStringError):
        validate_word("", [], 1)


# Test with mixed case and special characters
def test_for_mixed_case_and_special_characters():
    with pytest.raises(InvalidDictionaryWordError) as e:
        validate_word("Xbause@", [], 7)
    assert str(e.value) == "Invalid dictionary word: Xbause@"


# test for white space handling
def test_for_white_space_handling():
    assert score(" hello") == 8


# Test for non string input
def test_for_non_string_input():
    word_list = []
    with pytest.raises(NonStringInputError) as exc:
        validate_word(12345, word_list, 5)
    assert str(exc.value) == "Non string input is not allowed"


# Test multiple words
def test_for_multiple_words():
    word_list = []
    with pytest.raises(MultipleWordError) as exc:
        validate_word("hello world", word_list, 5)
    assert str(exc.value) == "Only one word is allowed"


# Test for duplicate input
def test_for_duplicate_input():
    random_number = 5
    with pytest.raises(DuplicateInputError) as exc:
        word_list = ["hello"]
        validate_word("hello", word_list, random_number)
    assert str(exc.value) == "Duplicate input: hello was mentioned before"


@pytest.mark.parametrize(
    "word, word_list,random_number",
    [
        ("hello", [], 2),
        ("world", ["hello"], 6),
        ("world", ["hello", "worlds"], 6),
    ],
)
def test_validate_input_length_with_random_length(word, word_list, random_number):

    with pytest.raises(InvalidInputLengthError) as exc:
        validate_word(word, word_list, random_number)
    assert (
        str(exc.value)
        == f"Invalid input length: word length should be {random_number} characters"
    )


def test_timer():
    # Mock the Tkinter GUI
    with patch("tkinter.Tk") as MockTk:
        game = ScrabbleGame()
        assert game.ctr + 1 == 15
        assert MockTk.called
