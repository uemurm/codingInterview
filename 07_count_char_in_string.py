"""
Count a character in a string.
"""
def count_char_in_string(string, char):
    """
    Count a character in a string.
    """
    count = 0
    for ch in list(string):
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

for s, c in strings:
    print(s + ':' + c + ' : ' + str(count_char_in_string(s, c)))
