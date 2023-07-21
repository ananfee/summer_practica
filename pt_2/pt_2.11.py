a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

sum = 0

for num in range(a, b + 1):
    sum += num

print("Сумма всех целых чисел от", a, "до", b, "включительно:", sum)
