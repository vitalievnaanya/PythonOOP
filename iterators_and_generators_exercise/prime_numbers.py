from math import sqrt, floor


def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True

    boundary = floor(sqrt(num))
    for i in range(2, boundary + 1):
        if num % i == 0:
            return False
    return True


def get_primes(numbers):
    for num in numbers:
        if is_prime(num):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))