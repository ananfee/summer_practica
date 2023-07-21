tv_shows = ["Орел и решка", "Спокойной ночи, малыши", "Давай поженимся", "Беременна в 16"]

print("Список передач:")
print('\n'.join(tv_shows))

new_show = input("Введите название новой передачи: ")
position = int(input("Введите позицию для вставки (от 1 до {}): ".format(len(tv_shows) + 1)))

tv_shows.insert(position - 1, new_show)

print("Обновленный список передач:")
print('\n'.join(tv_shows))
