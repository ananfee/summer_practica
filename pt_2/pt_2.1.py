transfers = ["4 свадьбы", "Пусть говорят", "Орел и Решка", "Мужское женское"]
for i in transfers:
    print(i)
s = str(input("Введите название телепередачи:"))
id = int(input("Введите позицию:"))
transfers.insert(id, s)
print(transfers)
