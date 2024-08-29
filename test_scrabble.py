"""
This is the test file for the scrabble game
"""

import pytest

from exception import EmptyStringError, InvalidDictionaryWordError
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
def test_for_valid_dictionary_word():
    try:
        validate_word("hello")
    except InvalidDictionaryWordError:
        pytest.fail("InvalidDictionaryWordError unexpectedly!")


# Test for invalid word
def test_for_invalid_dictionary_word():
    with pytest.raises(InvalidDictionaryWordError) as e:
        validate_word("Xbause")
    assert str(e.value) == "Invalid dictionary word: Xbause"


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
def test_for_mixed_case_and_special_characters():
    with pytest.raises(InvalidDictionaryWordError) as e:
        validate_word("Xbause@")
    assert str(e.value) == "Invalid dictionary word: Xbause@"


# test for white space handling
def test_for_white_space_handling():
    assert score(" hello") == 8


# Test length of word
# Test for non string input
def test_for_non_string_input():
    assert score(1234) == 10


# Test multiple words
# Test that length of random word is equal to length of user input word
