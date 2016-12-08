"""This module implements the trigrams algorithm for a given text file."""


from __future__ import print_function
import random
import io
import sys
import re


def open_file(path):
    """Return a string of the contents of a given file."""
    f = io.open(path)
    data = f.read()
    f.close()
    return data


def format_text(text):
    """Format string returned from file."""
    text = text.replace('--', ' ')  #Special case.
    text = text.replace('\n', ' ')
    text = re.sub('[^ a-zA-Z]', '', text)

    return text.lower()


def make_tri_dict(word_list):
    """Make key value pairs of pairs of words to a list of words from a
    list of words from the text in order.
    """
    tri_dict = {}

    for i in range(len(word_list) - 2):
        key_pair = word_list[i] + ' ' + word_list[i + 1]
        next_word = word_list[i + 2]
        if key_pair in tri_dict:
            tri_dict[key_pair] += [next_word]
        else:
            tri_dict[key_pair] = [next_word]
    return tri_dict


def build_text(tri_dict, num_words):
    """Build the output text using the trigram dictionary, limited by
    num words.
    """

    """Initialize the output string in list form with first two items
    randomly chosen from keys of tri_dict"""
    output_string = random.choice(list(tri_dict.keys())).split()

    if num_words < 2:
        return output_string[0]

    for i in range(num_words - 2):
        key = output_string[i] + " " + output_string[i + 1]
        if key not in tri_dict:
            key = random.choice(list(tri_dict.keys()))

        new_word = [random.choice(tri_dict[key])]
        output_string += new_word

    return " ".join(output_string)


def main(path, num_words):
    """Implement the core trigrams algorithm."""
    data = open_file(path)
    formatted_text = format_text(data)
    tri_dict = make_tri_dict(formatted_text.split())
    new_story = build_text(tri_dict, num_words)

    print(new_story)


if __name__ == '__main__':
    path = sys.argv[1]
    num_words = int(sys.argv[2])
    main(path, num_words)
