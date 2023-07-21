import csv

header = ["Книга", "Автор", "Год выпуска"]
rows = [["Чародол", "Наталья Щерба", "2008"],
        ["Вино из одуванчиков", "Рэй Брэдбери", "1957"],
        ["Призрак оперы", "Гастон Леру", "1909"],
        ["Мастер и Маргарита", "Михаил Булгаков", "1937"]]

filename = "prog_books.csv"

with open(filename, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)
