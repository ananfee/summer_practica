total_sum = 0

while True:
    number = int(input("Введите число: "))

    if number < 0:
        break

    total_sum += number

print("Сумма чисел равна:", total_sum)
