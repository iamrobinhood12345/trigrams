"""This is the test for trigrams.py."""
import pytest


def test_open_file():
    """Test open file."""
    from trigrams import open_file
    assert type(open_file('Sherlock_Holmes_short.txt')) is str
