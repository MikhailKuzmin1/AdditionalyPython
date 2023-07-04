#Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
first_number = 2
second_number = 2
while first_number <=9:
    while second_number <= 10:
        print (f'{first_number}*{second_number} = {first_number*second_number}')
        second_number += 1
    first_number += 1
    second_number =2