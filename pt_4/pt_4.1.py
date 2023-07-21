number = int(input("Введите число: "))

number = str(number)
digits = list(number)

digits.sort(reverse=True)
max_number = int(''.join(digits))

print("Наибольшее число, полученное перестановкой цифр:", max_number)
