#Denis Trushin

# В теле программы есть вызовы всех процедур

"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
    Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

def divide(dividend,denominator):
    try:
        return dividend/denominator
    except ZeroDivisionError:
        return "Неопределённость"
    except TypeError:
        return "Неправильный тип аргументов"
    except Exception as ex:
        return ex

"""2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
    имя, фамилия, год рождения, город проживания, email, телефон. 
    Функция должна принимать параметры как именованные аргументы. 
    Реализовать вывод данных о пользователе одной строкой."""

def personal_data(first_name:str, last_name:str, year_of_birth:int, place:str, email:str=None, mobile:int=None):
    print(f'Товарищ {last_name} {first_name} {year_of_birth} года рождения,'
          f'проживающий в {place}. E-mail: {email}, телефон: {mobile}')

"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, 
    и возвращает сумму наибольших двух аргументов."""

def sum_two_out_three(a, b, c):
    try:
        temp = sorted([a, b, c], reverse=True)
        return temp[0] + temp[1]
    except TypeError:
        return "нельзя сравнивать строки и числа"

"""4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла."""

def power(a, b):
    result = a
    for index in range(1,abs(b)):
        result *= a
    if b < 0:
        try:
            return 1/result
        except Exception as ex:
            return ex
    elif b > 0:
        return result
    else:
        return 1 # n^0

"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, 
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
Но если вместо числа вводится специальный символ, выполнение программы завершается. 
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной 
ранее сумме и после этого завершить программу."""

def typewriter():
    summ = 0 #Набегающая сумма
    while True:
        #получение обрезка, разбиение строки
        input_string = input("Введите строку из чисел через пробел.\n "
                             "Для завершения введите любой символ или слово: ").strip().split(' ')
        try: #попытка привести к числу и сложить
            input_string = list(map(int, input_string)) #приведение к числу
            summ += sum(input_string)
            print(f'Промежуточная сумма: {summ}. \n')
        except ValueError:
            break
    #если в последовательности есть строки, то сичтаем сумму до них
    for item in input_string:
        try:
            summ += int(item)
        except ValueError:
            print(f'Конечная сумма: {summ}. \nРабота завершена')
        except Exception as ex:
            print(ex)

"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
    но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text."""

def capital_leter(text:str):
    return text.capitalize() #smile

def capital_leter_v2(text:str):
    return text[0].upper()+text[1:]

def capital_leter_v3(text:str):
    #ord('A') = 65, ord('a') = 97 -- 97-65=32
    first_letter = ord(text[0])
    if first_letter >= 97:
        return chr(first_letter-32)+text[1:]
    return text

"""Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, 
но каждое слово должно начинаться с заглавной буквы. 
Необходимо использовать написанную ранее функцию int_func()."""

def capitaliser(text:str):
    return ' '.join(list(map(capital_leter,text.strip().split(' '))))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

       print(divide(3,5))

#    personal_data("Denis", "Trushin", 1981, "г. Балашиха")

#    print(sum_two_out_three("a",7,"c"))

#    print(power(3,-3))

#    typewriter()

#    print(capital_leter('vasily'))
#    print(capital_leter_v2('vasily'))
#    print(capital_leter_v3('vasily'))

#    print(capitaliser("Как тебе такое илон маск?"))