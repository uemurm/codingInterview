'''
foo
'''
def count_char_in_string(string, char):
    """
    Count a character in a string.
    """
    count = 0
    for idx, ch in enumerate(string):
        if char == ch:
            count += 1
    return count

print(count_char_in_string('foo', 'f'))
print(count_char_in_string('foo', 'F'))
print(count_char_in_string('foo', 'o'))
print(count_char_in_string('', 'f'))
print(count_char_in_string('foo', ''))
