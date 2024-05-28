"""
Determine if strings are a mutual rotation.
"""
def are_mutual_rotation(str0, str1):
    """
    Determine if strings are a mutual rotation.
    """
    if not len(str0) == len(str1):
        return False
    concat = str0 + str0
    return str1 in concat

pairs = (
    ('', ''),
    ('', 'a'),
    ('a', ''),
    ('foo', 'ofo'),
)

for s0, s1 in pairs:
    print(f'"{s0}", "{s1}" :\t' + str(are_mutual_rotation(s0, s1)))
