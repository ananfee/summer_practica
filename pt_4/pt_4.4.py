import itertools


def number(nums):
    s = ''.join(nums)
    s = int(s)
    return s


a = input('Введите список чисел через пробел: ').split(' ')
summa = int(input('Введите число: '))
for i in range(1, len(a)):
    comb = itertools.combinations(a, i)
    for j in comb:
        n = list(j)
        s_arr = sum(list(map(int, j)))
        if s_arr == summa:
            print(number(n))
