def reverse_array(array):
    """
    Create a reversed array then return it.
    """
    for i in range(0, int(len(array) / 2)):
        size = len(array)
        tmp = array[(size - 1) - i]
        array[(size - 1) - i] = array[i]
        array[i] = tmp
    return ''.join(array)

string = 'ABCDE'
print(string + ' : ' + reverse_array(list(string)))
