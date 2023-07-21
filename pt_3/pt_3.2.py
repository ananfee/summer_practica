fibonacci = lambda n: [fib(x) for x in range(n)]
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fibonacci(10))
