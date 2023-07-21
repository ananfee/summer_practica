def rot13(string):
    encoded_string1 = ""
    for char in string:
        if char.isalpha():
            if char.isupper():
                encoded_char = chr((ord(char) - 65 + 13) % 26 + 65)
            else:
                encoded_char = chr((ord(char) - 97 + 13) % 26 + 97)
        else:
            encoded_char = char
        encoded_string1 += encoded_char
    return encoded_string1


input_string = input("Введите строку: ")
encoded_string = rot13(input_string)
print("Закодированная строка:", encoded_string)
