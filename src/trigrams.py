"""This module implements the trigrams algorithm for a given text file."""


from __future__ import print_function
import random
import io
import sys
import re


# TRI_DICT = {}


def open_file(path):
    """Return a string of the contents of a given file."""
    f = io.open(path)
    data = f.read()
    f.close()
    return data


def format_text(text):
    """Format string return from file to remove punctuation, 
    newlines, and capital letters."""
    text = text.replace('--', ' ')  #special case
    text = text.replace('\n', ' ')
    text = re.sub('[^ a-zA-Z]', '', text)

    return text.lower()


def make_tri_dict(word_list):
    """Make key value pairs of pairs of words to a list of words from a
    list of words from the text in order."""
    tri_dict = {}
    key_pair = ''
    next_word = ''
    for i in range(len(word_list) - 3):
        key_pair = word_list[i] + ' ' + word_list[i + 1]
        next_word = word_list[i + 2]
        if key_pair in tri_dict:
            tri_dict[key_pair] += next_word
        else:
            tri_dict[key_pair] = next_word
    return tri_dict


def main(path, num_words):
    """This function implements the core trigrams algorithm"""
    make_tri_dict(format_text(open_file(path)).split())


if __name__ == '__main__':
    path = sys.argv[1]
    num_words = sys.argv[2]
    main(path, num_words)
