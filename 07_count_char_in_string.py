"""
Count a character in a string.
"""
def count_char_in_string(string, char):
    """
    Count a character in a string.
    """
    count = 0
    for idx, ch in enumerate(string):
        if char == ch:
            count += 1
    return count

strings = (
    ('foo', 'f'),
    ('foo', 'F'),
    ('foo', 'o'),
    (''   , 'f'),
    ('foo', '' ),
)

for string, char in strings:
    print(string + ':' + char + ' : ' + str(count_char_in_string(string, char)))
