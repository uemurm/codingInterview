def are_mutual_rotation(str0, str1):
    """
    docstring
    """
    if not len(str0) == len(str1):
        return False
    concat = str0 + str0
    return str1 in concat

pairs = (
    ('', ''),
    ('', 'a'),
    ('a', ''),
    ('foo', 'ofo')
)
for pair in pairs:
    print(pair[0] + ', ' + pair[1] + ': ' + str(are_mutual_rotation(pair[0], pair[1])))
