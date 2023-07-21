def is_vowel(letter1):
    vowels = "aeiouyAEIOUY"
    return letter1 in vowels

string = input("Введите строку: ")

letter_dict = {}

for letter in string:
    is_vowel_letter = is_vowel(letter)
    letter_dict[letter] = is_vowel_letter

print("Словарь с гласными и согласными буквами:")
for key, value in letter_dict.items():
    print(key, ":", value)
