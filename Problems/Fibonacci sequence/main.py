def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 1
    while True:
        if counter > n:
            return
        yield a
        a, b = b, a + b
        counter += 1
