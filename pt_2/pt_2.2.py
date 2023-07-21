arr = ['Мужское женское', '4 свадьбы',
       'Пусть говорят', 'Орёл и решка']
for i in range(len(arr)):
    s = arr[i]
    print(s)
name = str(input('Введите название: '))
num = int(input('Введите номер позиции: '))
print()
arr.insert(num - 1, name)
for i in range(len(arr)):
    s = arr[i]
    print(s)
