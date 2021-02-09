#Denis Trushin

"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка."""

def typewriter():
    file = open('data\\01Task\\example.txt', 'a')
    while True:
        string = input('Введите строку: ')
        if string == '':
            break
        file.write(string + chr(13)) #chr(13) - перевод строки
    file.close()

#typewriter()

"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
    выполнить подсчет количества строк, количества слов в каждой строке."""

def reader():
    file = open('data/02Task/quote.txt', 'r', encoding='utf-8') ##вид пути изменил пайчарм при рефакторинге
    content = file.readlines()
    print(len(content)) #количество строк в файле
    for line in content:
        print(len(line.strip().split()), end=' ') #без перевода строки
    file.close()

#reader()

"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников."""

def salary():
    file = open('data/03Task/employees.txt', 'r', encoding='utf-8')
    for line in file:
        decode = line.strip().split()
        if float(decode[1]) > 20000:
            print(decode[0])
    file.close()

#salary()

"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл."""

def equals():
    dict_ru = {'1' : 'Один', '2' : 'Два', '3' : 'Три', '4' : 'Четыре', '5' : 'Пять'}

    file = open('data/04Task/dict_en.txt', 'r', encoding='utf-8') #исходник. Требует закрытия.
    with open('data/04Task/dict_ru.txt', 'w', encoding='utf-8') as stream:
        for line in file:
            decode = line.strip().split()
            print(decode[2] + ' - ' + dict_ru[decode[2]], file= stream) #для разнообразия принтим

    file.close()

#equals()

"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

from random import random, randint

def for_no_reason(n:int):
        array = [str(round(random()*randint(10,next+11),3)) for next in range(n)] #генерирует список n чисел

        with open('data/05Task/round_numbers.txt', 'w+', encoding='utf-8') as stream:
            stream.write(' '.join(array)) #пишем в файл одну строку
            stream.seek(0) #перевод "каретки"
            print(sum(map(float, stream.readline().strip().split())))

#for_no_reason(23)

"""6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""

def scool():
    dict_scool = {}
    with open('data/06Task/scool.txt', 'r', encoding='utf-8') as stream:
        for line in stream:                         #Для каждой строки файла
            parse_line = line.strip().split()       #распарсить на массив строк
            summ_hours = 0
            for idx in range(1, len(parse_line)):   #для всех, кроме первого
                try:
                    summ_hours += int(parse_line[idx][0:parse_line[idx].index('(')]) #попытаться вырезать до '('
                except ValueError: # не смогли распарсить - пропускаем. Конвенции надо соблюдать :)
                    pass
            dict_scool[parse_line[0][:-1]] = summ_hours #заполнить словарь
    print(dict_scool)

#scool()

"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""

import json

def farmer():
    farms = {}
    average_dict = {'average_profit': 0.0}
    average_count = 0 #подсчёт фирм с положительным сальдо для вычисления среднего арифмитического

    with open('data/07Task/farmer.txt', 'r', encoding='utf-8') as stream:
        for line in stream:
            decode = line.strip().split()
            farms[decode[0]] = float(decode[2]) - float(decode[3])
            if farms[decode[0]] > 0:
                average_dict['average_profit'] += farms[decode[0]] #копим положительное сальдо
                average_count += 1
    average_dict['average_profit'] /= average_count #ищем среднее

    with open('data/07Task/farmer.json', 'w', encoding='utf-8') as stream:
        json.dump([farms, average_dict], stream)

#farmer()
