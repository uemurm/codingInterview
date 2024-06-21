def is_valid_word(word):
    return word

def countValidWords(string):
    valid_words = [word for word in string.split() if is_valid_word(word)]
    return len(valid_words)

s = input()
result = countValidWords(s)
print(result)
