num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

max_num = max(num1, num2, num3)

print("Наибольшее число:", max_num)
if max_num == num1:
    print(num1, num2, num3)
elif max_num == num2:
    print(num2, num1, num3)
else:
    print(num3, num2, num1)
