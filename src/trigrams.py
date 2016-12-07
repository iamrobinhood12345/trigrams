"""This module implements the trigrams algorithm for a given text file."""

from __future__ import print_function
import random
import io
import sys

TRI_DICT = {}


def open_file(path):
    """Return a string of the contents of a given file."""
    f = io.open(path)
    data = f.read()
    f.close()
    return data


def main(path, num_words):
    """This function implements the core trigrams algorithm"""
    open_file(path)



if __name__ == '__main__':
    path = sys.argv[1]
    num_words = sys.argv[2]
    main(path, num_words)
