def fibonacci(n):
    """
    Calculate Fibonacci numbers.
    """
    previous = 0
    current = 1
    n = n - 2
    print(0)
    print(1)
    while n > 0:
        next_number = current + previous
        print(next_number)
        previous = current
        current = next_number
        n -= 1

fibonacci(5)
