#Трушин Денис

if __name__ == '__main__':

#1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

    any_list = [None,
                2,
                'n',
                8.34,
                ('к', 'о', 'р', 'т', 'э', 'ж'),
                {'пуля':'дура', 'штык':'молодец'},
                ['ещё один список']]
    for item in any_list:
        print(f'переменная {item} имеет тип {type(item)}')

#2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

    next = None
    any_list = []

    while True:
        next = input("Введите список поэлементно (пусто для завершения ввода): ")
        if next != '':
            any_list.append(next)
        else:
            break

    print(any_list)

    for index in range(len(any_list) // 2): #опорным индексом будет range(len // 2) * 2 --0,2,4,6...
        any_list[index * 2], any_list[index * 2 + 1] = any_list[index * 2 + 1], any_list[index * 2]

    print(any_list)

#3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

    sezons_list = ['Зима', 'Весна', 'Лето', 'Осень']
    sezons_dict = {1:'Зима', 2:'Зима', 3:'Весна', 4:'Весна', 5:'Весна', 6:'Лето', 7:'Лето',
                   8:'Лето', 9:'Осень', 10:'Осень', 11:'Осень', 12:'Зима',}

    month = int(input("Введите номер месяца: "))

    print("\nЧерез лист")

    if month == 1 or month == 2 or month == 12:
        print(sezons_list[0])
    elif month == 3 or month == 4 or month == 5:
        print(sezons_list[1])
    elif month == 6 or month == 7 or month == 8:
        print(sezons_list[2])
    elif month == 9 or month == 10 or month == 11:
        print(sezons_list[3])
    else:
        print("Вы ввели неверный номер")

    print("\nЧерез словарь")

    print(sezons_dict.get(month, "Такого месяца нет"))

#4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

    input_string = input("Введите произвольную строку: ") #'  Пример моей строки с пробелами '
    index = 1

    for item in input_string.strip().split(' '): #тримаем пробелы с концов строки перед разбиением
        print(f'{index} {item[:10]}')
        index += 1

#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

    my_list = [7, 5, 3, 3, 2]
    number = int(input("введите натуральное число: "))
#"должен разместиться после них" не отличим от результата "перед ними" или "между ними" пока мы не используем
# ссылочные типы.  "+ my_list.count(number)" добавлен именно из-за этого условия задачи.
    my_list.insert(my_list.index(number) + my_list.count(number), number)
    print(my_list)

#6. Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#Пример готовой структуры:
#[
#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
#]


    my_merch = [
            (1, {"цена":"большая", "производитель":"нормальный", "приблуды":True}),
            (2, {"цена":"средняя", "производитель":"такое себе", "приблуды":False}),
            (3, {"цена":"малая", "производитель":"no name", "приблуды":False})
                    ]
    next_pice = None
    index = len(my_merch) #

    while True:
        next_pice = input("\nВведите цену (пусто для завершения): ")
        if next_pice != '':
            my_merch.append((index+1, {"цена": next_pice, "производитель": None, "приблуды": None}))
            my_merch[index][1]['производитель'] = input("Введите название производителя: ")
            my_merch[index][1]['приблуды'] = bool(input("Укажите наличие приблуд (True or False): "))
        else:
            break

    for item in my_merch:
        print(f'цена {item[1].get("цена")}, '
              f'производитель "{item[1].get("производитель")}", '
              f'приблуды {item[1].get("приблуды")};')