print()
print('--- --- Task 1 --- ---')
print()
# Создать класс TrafficLight (светофор) и
#   определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
#
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность
#   первого состояния (красный) составляет 7 секунд,
#   второго (желтый) — 2 секунды,
#   третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов,
#   и при его нарушении выводить соответствующее сообщение и завершать скрипт.
#
# Доп. информация:
# красный - жёлтый - зелёный - жёлтый - красный
# библиотека time метод sleep
# Библиотека Turtle
# Библиотека Tkinter
# https://all-python.ru/osnovy/tsvetnoj-vyvod-teksta.html
# https://en.wikipedia.org/wiki/ANSI_escape_code
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python

print()
print('--- Ver. 1 - Алгоритм ---')
print()

import time


class TrafficLight:
    __colors = ('Red', 'Yellow', 'Green', 'Yellow')

    def running(self, red, yellow, green):
        tl_list = self.__colors
        counter = 0
        while counter < 2:
            tl = iter(tl_list)
            print(next(tl))
            time.sleep(red)
            print(next(tl))
            time.sleep(yellow)
            print(next(tl))
            time.sleep(green)
            print(next(tl))
            time.sleep(yellow)
            counter += 1


t_red = 0
t_yellow = 0
t_green = 0

x = TrafficLight()
x.running(t_red, t_yellow, t_green)

print()
print('--- Ver. 2 - Turtle ---')
print()

# import datetime
# import time
# import turtle
# import itertools
#
# class TrafficLight:
#     __time_red = 7
#     __time_yellow = 2
#     __time_green = 5
#     __circle_size = 50
#     __yellow_period = {'Start': (0, 30), 'End': (0, 50)}
#     __colors = (
#         ('Red', __time_red),
#         ('Yellow', __time_yellow),
#         ('Green', __time_green),
#         ('Yellow', __time_yellow)
#     )
#
#     def running(self):
#         tt = turtle
#         tt.speed(10)
#         tt.bgcolor('Black')
#
#         for i in itertools.cycle(self.__colors):
#             t = datetime.datetime.now()
#
#             if (t.hour >= self.__yellow_period.get('Start')[0] and t.minute >= self.__yellow_period.get('Start')[1]) and (t.hour <= self.__yellow_period.get('End')[0] and t.minute <= self.__yellow_period.get('End')[1]):
#                 for i in ('Yellow', 'Black'):
#                     tt.color(i)
#                     tt.begin_fill()
#                     tt.circle(self.__circle_size)
#                     tt.end_fill()
#             else:
#                 for i in self.__colors:
#                     tt.color(i[0])
#                     tt.begin_fill()
#                     tt.circle(self.__circle_size)
#                     tt.end_fill()
#                     time.sleep(i[1])
#
# tl = TrafficLight()
# tl.running()

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 2 --- ---')
print()


# Реализовать класс Road (дорога), в котором определить атрибуты:
#   * length (длина),
#   * width (ширина).
#
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
#
# Использовать формулу: длина * ширина * масса асфальта
#   для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
#   Проверить работу метода.
#
# Например: 20м (Длина) * 5000м (Ширина) * 25кг * 5см = 12500 т
#
# Доп. информация:
# - Незабываем в конце поделить, чтобы перевести в тонны
# - Класс содержит два метода:
# * Конструктор
# * Расчёт массы асфальта
# - Внутри метода расчёта могут находиться локальные переменные для 25 кг и 5см
# - Также можем прописать их в return или в виде констант

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        m = 25
        t = 5
        print(int((self._width * self._length * m * t) / 1000), 'т')


r_length = 5000
r_width = 20

Road(r_length, r_width)

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 3 --- ---')
print()


# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
#   name,
#   surname,
#   position (должность),
#   income (доход).
#
# Последний атрибут должен быть защищенным и ссылаться на словарь,
#   содержащий элементы: оклад и премия,
#   например, {"wage": wage, "bonus": bonus}.
#
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
#   и дохода с учетом премии (get_total_income).
#
# Проверить работу примера на реальных данных
#   (создать экземпляры класса Position,
#   передать данные,
#   проверить значения атрибутов,
#   вызвать методы экземпляров).
#
# Доп. информация:
# - get_full_name - конкатенация

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Postion(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(sum(self._income.values()))


name = 'Meliodas'
surname = 'Redfox'
position = 'CEO'
wage = 50000
bonus = 10000

Postion(name, surname, position, wage, bonus).get_full_name()
Postion(name, surname, position, wage, bonus).get_total_income()

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 4 --- ---')
print()
# Реализуйте базовый класс Car.
#   У данного класса должны быть следующие атрибуты:
#       speed,
#       color,
#       name,
#       is_police (булево).
#
#   А также методы:
#       go,
#       stop,
#       turn(direction),
#   которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#
# Опишите несколько дочерних классов:
#   TownCar,
#   SportCar,
#   WorkCar,
#   PoliceCar.
#
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
#
# Доп. информация:
# - В метод turn(direction) передаём направление (Left, Right), (Север, Запад, Юг, Восток, Юго-восток и т.д.)
# - Для определения направления используем random
# - Метод show_speed переопределяем в TownCar и WorkCar

t_sleep = 0


class Car():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_info(self):
        print(f'Класс авто:     {self.__class__.__name__}')
        print(f'Модель авто:    {self.name}')
        print(f'Цвет:           {self.color}')
        print(f'Полицейская?    {self.is_police}')
        print('')

    def start_engine(self):
        print('- start_engine -')
        self.speed = 0
        print('Speed:', self.speed)
        print('')

    def go(self):
        print('- go -')
        while self.speed < 25:
            time.sleep(t_sleep)
            self.speed += 1
            print('Speed:', self.speed)
        print('')

    def accelerate(self, goal_speed):
        print('- accelerate -')
        while self.speed < goal_speed:
            time.sleep(t_sleep)
            self.speed += 1
            print('Speed:', self.speed)
        print('')

    def slow_down(self, goal_speed):
        print('- slow_down -')
        while self.speed > goal_speed:
            time.sleep(t_sleep)
            self.speed -= 1
            print('Speed:', self.speed)
        print('')

    def stop(self):
        print('- stop -')
        while self.speed > 0:
            time.sleep(t_sleep)
            self.speed -= 1
            print('Speed:', self.speed)
        print('')

    def turn(self, direction):
        print('- turn -')
        print(f'Turn: {direction}')
        x = self.speed - 10
        while self.speed > x:
            time.sleep(t_sleep)
            self.speed -= 1
            print('Speed:', self.speed)
        print('Direction: Forward')
        print('')

    def show_speed(self):
        print('- show_speed - ')
        print('Speed:', self.speed)
        print('')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Speed:', self.speed)
            print('Превышение скорости')
        else:
            print('Speed:', self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Speed:', self.speed)
            print('Превышение скорости')
        else:
            print('Speed:', self.speed)


class PoliceCar(Car):
    def show_info(self):
        print(f'Класс авто:     {self.__class__.__name__}')
        print(f'Модель авто:    {self.name}')
        print(f'Цвет:           {self.color}')
        self.is_police = True
        print(f'Полицейская?    {self.is_police}')
        print('')


var_speed = 70
var_color = 'White'
var_name = 'Lexus'
var_is_police = False

var_accelerate = 75
var_slow_down = 30
var_turn = 'Right'
var_turn = 'Left'

# var_class = TownCar
# var_class = SportCar
# var_class = WorkCar
var_class = PoliceCar

call_class = var_class(var_speed, var_color, var_name, var_is_police)
class_name = call_class.__class__.__name__

print('-' * 3, f'{class_name}:', '-' * 3)
call_class.show_info()
call_class.start_engine()
call_class.go()
# call_class.accelerate(int(input('Введите целевую скорость:')))
# call_class.slow_down(int(input('Введите целевую скорость:')))
call_class.turn(var_turn)
call_class.accelerate(var_accelerate)
call_class.show_speed()
call_class.slow_down(var_slow_down)
call_class.stop()

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 5 --- ---')
print()


# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
#
# Создать три дочерних класса
#   Pen (ручка),
#   Pencil (карандаш),
#   Handle (маркер).
#
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
#
# Доп. информация:
# зачем нужен title и как можно переопределять в потомках

class Stationery:
    def __init__(self, title='Something that can draw'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки!')


class Pen(Stationery):
    def __init__(self):
        self.title = self.__class__.__name__

    def draw(self):
        print('Pen(Stationery):', self.title)


class Pencil(Stationery):
    def __init__(self):
        self.title = self.__class__.__name__

    def draw(self):
        print('Pencil(Stationery):', self.title)


class Handle(Stationery):
    def __init__(self):
        self.title = self.__class__.__name__

    def draw(self):
        print('Handle(Stationery):', self.title)


obj_1 = Stationery()
obj_1.draw()

obj_2 = Pen()
obj_2.draw()

obj_3 = Pencil()
obj_3.draw()

obj_4 = Handle()
obj_4.draw()
