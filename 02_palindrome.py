'''
Doc
'''
def reverse(string):
    """
    Return a reversed string.
    """
    ret = ''
    size = len(string)
    for i in range(0, size):
        ret += string[size - 1 - i]
    return ret

def is_palindrome(string):
    '''
    Determine if it's a palindrome.
    '''
    return True if string == reverse(string) else False

strings = ['madam', 'Madam', 'M', '']

for s in strings:
    print(str(is_palindrome(s)) + '\t:' + s)
