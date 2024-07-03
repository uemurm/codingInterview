"""
This is a code quiz at an interview in Morse Micro.
"""
def is_armstrong_number(n):
    """
    Determines if the number is an Armstrong number.
    """
    m = n
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10

    # Should be revised using a generator.
    return sum([n ** len(digits) for n in digits]) == m

for i in range(10000):
    if is_armstrong_number(i):
        print(i)
