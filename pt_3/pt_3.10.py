text = "Hello"

count = {}

for letter in text:
    if letter.isalpha() and letter != " ":
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

print(count)
