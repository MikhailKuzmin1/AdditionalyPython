#Нарисовать в консоли ёлку спросив у пользователя количество рядов. 
string_count = int(input("Введите количество ярусов: "))
i = 1
count = 1
space = string_count
while i <= string_count:
    print(" " * space + "*" * count)
    i += 1
    count += 2
    space -= 1