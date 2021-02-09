#Denis Trushin

"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод."""

import time as t

class Lighter:
    _color = 'красный'

    def __init__(self):
        self._first_call = t.monotonic() #относительное время создания экземпляра.
        self.cycle = 20 #определение длительности цикла

    def running(self):
        now = (t.monotonic()-self._first_call) % self.cycle #время текущего 20 секундного цикла

        if now <= 7:
            Lighter.color = 'красный'
        elif now <= 9:
            Lighter.color = 'жёлтый'
        else:
            Lighter.color = 'зелёный'
        print(f'Время текущего цикла: {round(now, 2)} Сейчас горит {Lighter.color}')

# lighter_1 = Lighter() #создаём светофор
# for index in range(0,18):
#    lighter_1.running() #опрашиваем состояние
#    t.sleep(2)

"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. 
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т"""

class Road:
    def __init__(self, length: int, width: int):
        self._length = length
        self._width = width
        self.thickness = 5
        self.mass = 25

    def calc_asphalt(self):
        return self._width * self._length * self.mass * self.thickness

# kasimovskiy_tract = Road(12,23)
# kasimovskiy_tract.thickness = 12
# print(kasimovskiy_tract.calc_asphalt())

"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""

class Worker:
    def __init__(self, name: str, surname: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.name,self.surname])

    def get_total_income(self):
        return sum(self._income.values())

# im = Position('Denis', 'Trushin', 1234, 4321)
# wife = Position('Irina', 'Trushina', 4467, 9912)
#
# print(im.get_full_name())
# print(wife.get_full_name())
# print(im.get_total_income())
# print(wife.get_total_income())

"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат."""


class Car:
    def __init__(self, color: str, name: str, is_police: bool = False):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        while True:
            try:
                self.speed = int(input("Осторожно, моя машина поехала вперёд!\nС какой скоростью поедем? "))
                break
            except ValueError:
                print("Вы ввели не число. Повторите ввод.")

    def stop(self):
        print("Тормози!")

    def turn(self, direction):
        self.direction = direction
        print(f"На следующем перекрёстке поверните на {self.direction}")

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Вы едете слишком быстро!")
        print(f'Ваша скорость {self.speed}')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Вы едете слишком быстро!")
        print(f'Ваша скорость {self.speed}')

class PoliceCar(Car):
    pass


# my_car = TownCar('Зелёный', 'УАЗ', False)
# print(my_car.name)
# my_car.go()
# my_car.show_speed()
# my_car.go()
# my_car.show_speed()
#
# print("_____")
# work_car = WorkCar('Оранжевый', 'CAT', False)
# print(work_car.name)
# work_car.show_speed()
# work_car.go()
# work_car.show_speed()

"""5. Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” 
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""

class Stationery():
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print("рисуем")

class Pen(Stationery):
    def draw(self):
        print("Пишем ручкой")

class Pencil(Stationery):
    def draw(self):
        print("Пишем карандашом")

class Handle(Stationery):
    def draw(self):
        print("Пишем маркером")


# pen = Pen("Parker")
# pencil = Pencil("KOH-I-NOOR")
# handle = Handle("Uni Mitsubishi")
#
# pen.draw()
# pencil.draw()
# handle.draw()