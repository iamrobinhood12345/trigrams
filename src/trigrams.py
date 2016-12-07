"""This module implements the trigrams algorithm for a given text file."""

from __future__ import print_function
import random
import io
import sys
import re

TRI_DICT = {}


def open_file(path):
    """Return a string of the contents of a given file."""
    f = io.open(path)
    data = f.read()
    f.close()
    return data


def format_text(text):
    """Format string return from file to remove punctuation, newlines, and capital letters."""
    text = text.replace('--', ' ')  #special case
    text = text.replace('\n', ' ')
    text = re.sub('[^ a-zA-Z]', '', text)

    return text


def main(path, num_words):
    """This function implements the core trigrams algorithm"""
    format_text(open_file(path))




if __name__ == '__main__':
    path = sys.argv[1]
    num_words = sys.argv[2]
    main(path, num_words)
