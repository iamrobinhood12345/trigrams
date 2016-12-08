"""This is the test for trigrams.py."""
import pytest
import string

# Punctuation that should be removed.
PARAMS_PUNCTUATION = string.punctuation + '\n'
PARAMS_TEST_DICT = {
    "i wish": ["i", "i"],
    "wish i": ["may", "might"],
    "may i": ["wish"],
    "i may": ["i"]
}
PARAMS_TEST_STRING = "i wish i may i wish i might".split()
PARAMS_NUM_WORDS = 6


def test_open_file():
    """Test open file."""
    from trigrams import open_file
    assert type(open_file('Sherlock_Holmes_short.txt')) is str


def test_string_format_islowercase():
    """Tests string is lowercase."""
    from trigrams import format_text, open_file
    assert format_text(open_file('Sherlock_Holmes_short.txt')).islower()


@pytest.mark.parametrize("n", PARAMS_PUNCTUATION)
def test_string_format_punctuation(n):
    """Tests string formatting."""
    from trigrams import format_text, open_file
    assert n not in format_text(open_file('Sherlock_Holmes_short.txt'))


def test_make_tri_dict():
    """Test tri_dict(), verify format of dictionary"""
    from trigrams import make_tri_dict
    assert make_tri_dict(PARAMS_TEST_STRING) == PARAMS_TEST_DICT


def test_build_text():
    """Test build_text to see if it is the correct number of words"""
    from trigrams import build_text
    assert len(build_text(PARAMS_TEST_DICT, PARAMS_NUM_WORDS).split) == PARAMS_NUM_WORDS

