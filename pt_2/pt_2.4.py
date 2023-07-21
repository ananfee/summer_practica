import math

a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

Discr = b ** 2 - 4 * a * c

if Discr < 0:
    print("Корней нет")
elif Discr == 0:
    x = -b / (2 * a)
    print("Один корень: x =", x)
else:
    x1 = (-b + math.sqrt(Discr)) / (2 * a)
    x2 = (-b - math.sqrt(Discr)) / (2 * a)
    print("Два корня: x1 =", x1, " x2 =", x2)
