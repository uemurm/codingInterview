def is_prime(n):
    """
    Determine a prime number.
    """
    if n <= 1:
        return False
    div = 2
    while div <= n / 2:
        if n % div == 0:
            return False
        div += 1
    return True

for num in range(20):
    print(str(num) + ' : ' + str(is_prime(num)))

print(is_prime(991))
