names = (input("Введите названия: ").split(", "))
length = int(input("Длина слова: "))
for i in names:
    if len(i) < length:
        print((str(i).lower()), end=' ')