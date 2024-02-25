def count_vowels_consonants(string):
    """
    Count vowels and consonants in a string.
    """
    vowels = 0
    consonants = 0

    for idx, ch in enumerate(string.lower()):
        if ch == 'a' or \
           ch == 'e' or \
           ch == 'i' or \
           ch == 'o' or \
           ch == 'u':
            vowels += 1
        else:
            consonants += 1

    print('Vowel counts: ' + str(vowels))
    print('Consonant counts: ' + str(consonants))

strings = ['foo', 'Foo', 'fOo', 'F', '']
for i, s in enumerate(strings):
    print(s)
    count_vowels_consonants(s)
    print()
