#Трушин Денис
#Задание к первому уроку

#1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
# несколько чисел и строк и сохраните в переменные, выведите на экран.

one = 'Привет!'
onemore = 2.76
greeting = one
user_data = input(greeting+" Введите строку: ")
print(f'Вы ввели "{user_data}"')


# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

user_data = int(input("Введите время в секундах: "))
seconds = user_data%60
minuts = (user_data//60)%60
ours = (user_data)//3600
print(f'{user_data} секунд - это {ours} часов {minuts} минут {seconds} секунд')


# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

user_data = input("Введите целое число: ")

if user_data[0] != "-":
    # умножаем строку, приводим к числу. Работает для любых натуральных чисел
    print(int(user_data*3)+int(user_data*2)+int(user_data))
else: #для отрицательных
    user_data = str(-1 * int(user_data)) #приводим к положительному
    print(-1*(int(user_data * 3) + int(user_data * 2) + int(user_data))) #домножаем на -1

#если на входе именно число, а не строка
user_data = int(input("Введите целое число: "))
Multiplicator = 10
copy_user_data = user_data  # сначала используем как делимое в цикле определения порядков, потом для расчёта конечного числа

while copy_user_data // 10 > 0:  # считаем сколько порядков в числе. Готовим мультипликатор.
    Multiplicator *= 10
    copy_user_data //= 10

# nn = user_data * Multiplicator + user_data
# nnn = nn * Multiplicator + user_data
# copy_user_data = (user_data * Multiplicator + user_data) * Multiplicator + user_data + (user_data * Multiplicator + user_data) + user_data
copy_user_data = user_data * Multiplicator * Multiplicator + 2 * user_data * Multiplicator + 3 * user_data  # раскрыты скобки, упрощено выражение
print(copy_user_data)


#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

user_data = int(input("Введите натуральное число: "))  # 67324765345321
max_digital = user_data % 10

while user_data // 10 > 0:
    if (user_data // 10) % 10 > max_digital:
        max_digital = (user_data // 10) % 10
    user_data //= 10

print(f'Максимальная цифра {max_digital}')

# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input("Введите размер выручки: "))
loss = int(input("Введите размер издержек: "))
gain = revenue - loss

if gain > 0:
    print(f'Ваша компания прибыльна.\nДоходность {round(gain/revenue * 100,2)}%')
    workers_count = int(input("Введите количество сотрудников: "))
    print(f'Доходность на одного сотрудника {round(gain/workers_count,2)}')
else:
    print("Ваша компания убыточна.")


#Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

odometer = int(input("Введите результат первого дня: "))
target = int(input("Введите целевой результат: "))
progress = odometer ##прогресс тренеровок
days = 1            ##требуемые для достижения дни

while progress < target:
    days += 1
    progress += progress / 10

print(f'Для достижения результата {target} км с начального результата {odometer}, потребуется {days} дней')