def is_prime(n1):
    if n1 <= 1:
        return False
    for i in range(2, int(n1 ** 0.5) + 1):
        if n1 % i == 0:
            return False
    return True

n = 20
numbers = [x for x in range(n) if not is_prime(x)]
print(numbers)
