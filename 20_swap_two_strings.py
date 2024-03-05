s0 = 'FOO'
s1 = 'BAR'

print('s0: ' + s0)
print('s1: ' + s1)

s0 = s0 + s1
s1 = s0[0:len(s0) - len(s1)]
s0 = s0[len(s1):]

print('s0: ' + s0)
print('s1: ' + s1)

s0, s1 = s1, s0

print('s0: ' + s0)
print('s1: ' + s1)
