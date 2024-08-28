"""
This is the test file for the scrabble game
"""

import pytest

from main import score


# Test for valid score
@pytest.mark.parametrize(
    "word, expected",
    [
        ("a", 1),
        ("z", 10),
        ("dog", 5),
        ("cat", 5),
        ("dogcat", 10),
    ],
)
def test_score(word, expected):
    assert score(word) == expected


# Test for invalid score
# Test for valid dictionary word
# Test for invalid word
# Test uppercase letter and lowercase letter are the same
# Test for empty string exception
# Test with mixed case and special characters
# test for white space handling
# Test length of word
# Test for non string input
# Test multiple words
# Test that length of random word is equal to length of user input word
