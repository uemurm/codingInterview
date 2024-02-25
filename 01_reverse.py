def reverse(string):
    ret = ''
    size = len(string)
    for i in range(0, size):
        ret += string[size - 1 - i]
    return ret

print(reverse('FOO'))
print(reverse('A'))
print(reverse(''))
