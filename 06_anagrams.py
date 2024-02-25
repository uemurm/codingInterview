def are_anagrams(str0, str1):
    """
    docstring
    """
    str0 = str0.replace(' ', '')
    str1 = str0.replace(' ', '')
    if not len(str0) == len(str1):
        return False

    return ''.join(sorted(str0)) == ''.join(sorted(str1))

strings = (
    ('', ''),
    ('', 'a'),
    ('a', 'b'),
    ('a', 'a'),
    ('cheater', 'teacher'),
    ('god', 'dog'),
    ('planter', 'replant'),
    ('lampshade', 'headlamps'),
    ('bust', 'stub'),
    ('roots', 'torso'),
    ('rail', 'liar'),
    ('donate', 'atoned'),
    # Multiple words
    ('quiet down', 'quote wind'),
    # Should spaces be ignored?
    ('Horatio Nelson', 'Honor est a Nilo'),
    ('Florence Nightingale', 'Flit on cheering angel')
)


for pair in strings:
    STR0 = pair[0]
    STR1 = pair[1]
    print('"' + STR0 + '" and "' + STR1 + '" are ', end='')
    if not are_anagrams(STR0, STR1):
        print('not ', end='')
    print('anagrams.')
