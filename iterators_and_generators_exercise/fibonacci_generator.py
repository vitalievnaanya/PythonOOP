def fibonacci():
    fib1 = 0
    fib2 = 1

    yield fib1
    yield fib2

    while True:
        fib = fib1 + fib2
        yield fib
        fib1, fib2 = fib2, fib


generator = fibonacci()
for i in range(5):
    print(next(generator))

generator = fibonacci()
for i in range(1):
    print(next(generator))