def is_armstrong_number(numb):
    num_str = str(numb)
    num_digits = len(num_str)
    sum_of_digits = 0

    for digit in num_str:
        sum_of_digits += int(digit) ** num_digits

    if sum_of_digits == numb:
        return True
    else:
        return False


number = int(input("Введите число: "))

if is_armstrong_number(number):
    print(number, "является числом Армстронга.")
else:
    print(number, "не является числом Армстронга.")
