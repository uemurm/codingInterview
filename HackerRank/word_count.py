"""
Count valid words.
"""
import sys
import re

VOWELS = 'aeiouAEIOU'

def is_valid_word(word):
    """
    Determine a valid word.
    """
    if not re.match(r'^[a-zA-Z0-9]{3,}$', word):
        return False

    return has_vowel_and_consonant(word)

def has_vowel_and_consonant(word):
    """
    Determine if the word has both a vowel and a consonant.
    """
    has_vowel = False
    has_consonant = False

    for ch in word:
        if ch.isalpha():
            if ch in VOWELS:
                has_vowel = True
            else:
                has_consonant = True
        if has_vowel and has_consonant:
            return True
    return False

def list_words(string):
    for word in string.split():
        print(is_valid_word(word), '\t', end='')
        print(word)
    print()

def count_valid_words(string):
    """
    The method in question.
    """
    valid_words = [word for word in string.split() if is_valid_word(word)]
    return len(valid_words)

debug = '--debug' in sys.argv or \
             '-d' in sys.argv

while True:
    try:
        line = input()
        if debug:
            list_words(line)
        else:
            result = count_valid_words(line)
            print(result)
    except EOFError:
        break
