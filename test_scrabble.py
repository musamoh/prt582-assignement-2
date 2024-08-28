"""
This is the test file for the scrabble game
"""

import pytest

from exception import EmptyStringError
from main import score, validate_word


# Test for valid score
@pytest.mark.parametrize(
    "word, expected",
    [
        ("a", 1),
        ("z", 10),
        ("dog", 5),
        ("cat", 5),
        ("dogcat", 10),
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
        ("dogcat", 0),
        ("WORLD", 0),
    ],
)
def test_invalid_score(word, expected):
    assert score(word) != expected


# Test for valid dictionary word
@pytest.mark.parametrize(
    "word, expected",
    [
        ("a", True),
        ("z", True),
        ("Gombe", False),
        ("Hakimi", False),
        ("dog", True),
        ("cat", True),
        ("dogcat", True),
        ("WORLD", True),
    ],
)
def test_valid_dictionary_word(word, expected):
    assert validate_word(word) == expected


# Test for invalid word
# Test uppercase letter and lowercase letter are the same
@pytest.mark.parametrize(
    "word",
    [
        ("a"),
        ("z"),
        ("dog"),
        ("cat"),
        ("dogcat"),
        ("WORLD"),
    ],
)
def test_score_for_uppercase_and_lowercase(word):
    assert score(word.upper()) == score(word.lower())


# Test for empty string exception
def test_empty_string():
    with pytest.raises(EmptyStringError):
        validate_word("")


# Test with mixed case and special characters
# test for white space handling
# Test length of word
# Test for non string input
# Test multiple words
# Test that length of random word is equal to length of user input word
