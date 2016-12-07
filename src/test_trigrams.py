"""This is the test for trigrams.py."""
import pytest
import string

# Punctuation that should be removed.
PARAMS_PUNCTUATION = string.punctuation + '\n'


def test_open_file():
    """Test open file."""
    from trigrams import open_file
    assert type(open_file('Sherlock_Holmes_short.txt')) is str


def test_string_format_islowercase():
    """Tests string is lowercase."""
    from trigrams import format_text, open_file
    assert format_text(type(open_file('Sherlock_Holmes_short.txt'))).islower()


@pytest.mark.parametrize("n", PARAMS_PUNCTUATION)
def test_string_format_punctuation(n):
    """Tests string formatting."""
    from trigrams import format_text, open_file
    assert n not in format_text(type(open_file('Sherlock_Holmes_short.txt')))
