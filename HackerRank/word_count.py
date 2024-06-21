import sys

ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def is_valid_word(word):
    if len(word) < 3:
        if debug:
            print('Less than 3 chars')
        return False
    if not alphanumeric(word):
        if debug:
            print('non alpha-numeric')
        return False

    return has_vowel(word) and has_consonant(word)

def has_vowel(word):
    for vowel in VOWELS:
        if vowel in word.lower():
            return True
    if debug:
        print('without vowels')
    return False

def has_consonant(word):
    for consonant in CONSONANTS:
        if consonant in word.lower():
            return True
    if debug:
        print('without consonants')
    return False

def alphanumeric(word):
    word = word.lower()
    for ch in list(word):
        if ch not in '0123456789' and \
           ch not in ALPHABETS and \
           ch not in ALPHABETS.upper():
            return False
    return True

def list_words(string):
    for word in string.split():
        print(is_valid_word(word), '\t', end='')
        print(word)

def countValidWords(string):
    valid_words = [word for word in string.split() if is_valid_word(word)]
    return len(valid_words)

debug = '--debug' in sys.argv or \
             '-d' in sys.argv

# list_words(input())
result = countValidWords(input())
print(result)
