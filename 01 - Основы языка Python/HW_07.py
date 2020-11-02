print()
print('--- --- Task 1 --- ---')
print()
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
#   который должен принимать данные (список списков) для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин,
#   расположенных в виде прямоугольной схемы.
#
# Примеры матриц вы найдете в методичке.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
#
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
#   Matrix (двух матриц). Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно —
#   первый элемент первой строки первой матрицы складываем с
#   первым элементом первой строки второй матрицы и т.д.
#
# Доп. информация:
# - конструктор
# - матрица - список списков
# 1 2
# 3 4
# 5 6

matrix_3x2 = [
    [31, 22],
    [37, 43],
    [51, 86]
]
print('matrix_3x2:', matrix_3x2)

matrix_3x3 = [
    [3, 5, 32],
    [2, 4, 6],
    [-1, 64, -8]
]
print('matrix_3x3:', matrix_3x3)

matrix_2x4 = [
    [3, 5, 8, 3],
    [8, 3, 7, 1]
]
print('matrix_2x4:', matrix_2x4)
print()


class Matrix:
    def __init__(self, m_list):
        self.m_list = m_list

    def __str__(self):
        temp_str = ''
        for x in self.m_list:
            n_max = 0
            for i, y in enumerate(x, 0):
                n_max = i
            for n, y in enumerate(x, 0):
                temp_str += f'{y} ' if n != n_max else f'{y}\n'
        return temp_str

    def __add__(self, other):
        t3 = []
        t3_l2 = []

        for t1_i, t1_x in enumerate(self.m_list):
            t3_l2.clear()
            for t1_ii, t1_y in enumerate(t1_x, 0):
                try:
                    t2_y = other[t1_i][t1_ii]
                except IndexError:
                    t2_y = 0
                t3_l2.append(t1_y + t2_y)
                # print(f't1_y: {t1_y} t2_y: {t2_y}')
                # print(t3_l2)
                # print()
            # print(t3_l2)
            t3.append(list(t3_l2))
        print(t3)
        # print()


print(Matrix(matrix_3x2))
print(Matrix(matrix_3x3))
print(Matrix(matrix_2x4))

Matrix(matrix_3x2).__add__(matrix_3x2)
Matrix(matrix_3x3).__add__(matrix_3x3)
Matrix(matrix_2x4).__add__(matrix_2x4)
print()

Matrix(matrix_3x2).__add__(matrix_3x2)
Matrix(matrix_3x2).__add__(matrix_3x3)
Matrix(matrix_3x2).__add__(matrix_2x4)
print()

Matrix(matrix_3x3).__add__(matrix_3x2)
Matrix(matrix_3x3).__add__(matrix_3x3)
Matrix(matrix_3x3).__add__(matrix_2x4)
print()

Matrix(matrix_2x4).__add__(matrix_3x2)
Matrix(matrix_2x4).__add__(matrix_3x3)
Matrix(matrix_2x4).__add__(matrix_2x4)

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 2 --- ---')
print()
# Реализовать проект расчета суммарного расхода ткани на производство одежды.
#   Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#   К типам одежды в этом проекте относятся пальто и костюм.
#   У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
#   Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы:
#   для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
#   Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани.
#   Проверить на практике полученные на этом уроке знания:
#   реализовать абстрактные классы для основных классов проекта,
#   проверить на практике работу декоратора @property.
#
# Доп. информация
# - Использовать декоратор @property

print()
print('--- Ver. 1 ---')
print()


class Clothes_v1:
    def __init__(self, name=''):
        self.name = name
        if self.name.upper() == 'КОСТЮМ' or self.name.upper() == 'COSTUME':
            self.costume()
        elif self.name.upper() == 'ПАЛЬТО' or self.name.upper() == 'COAT':
            self.coat()
        else:
            print('Обратитесь к консультанту за тканью')

    def costume(self):
        size = 15
        # size = int(input('Введите размер: '))
        size = (size / 6.5 + 0.5)
        print(f'Вам необходимо {size} ткани')
        return size

    def coat(self):
        height = 15
        # height = int(input('Введите рост: '))
        height = (2 * height + 0.3)
        print(f'Вам необходимо {height} ткани')
        return height


x = Clothes_v1('Костюм')
y = Clothes_v1('Пальто')

print()
print('--- Ver. 2 - Учитель ---')
print()

from abc import ABC, abstractmethod


class Clothes_v2(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat_v2(Clothes_v2):
    @property
    def consumption(self):
        print(f'Consumption of fabric for sewing a coat - {round(self.param / 6.5) + 0.5}')
        return round(self.param / 6.5) + 0.5


class Costume_v2(Clothes_v2):
    @property
    def consumption(self):
        print(f'Consumption of fabric for sewing a costume - {(2 * self.param + 0.3) / 100}')
        return (2 * self.param + 0.3) / 100


coat = Coat_v2(42)
costume = Costume_v2(170)
print(coat + costume)

print()
print('--- Ver. 3 - Учитель ---')
print()

from abc import ABC, abstractmethod


class Clothes_v3(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def raschet(self):
        pass

    def __add__(self, other):
        return self.raschet + other.raschet


class Coat_v3(Clothes_v3):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            print('На детей не шьём. Начнём с сорокового.')
            self.__size = 40
        elif size > 58:
            print('Не многовато ли? 58 - МАКСИМУМ, для него и посчитаем.')
            self.__size = 58
        else:
            self.__size = size

    @property
    def raschet(self):
        return self.__size / 6.5 + 0.5


class Costume_v3(Clothes_v3):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 100:
            print('На детей не шьём.')
            self.__height = 150
        elif height > 240:
            print('Не многовато ли? 240 - МАКСИМУМ, для него и посчитаем.')
            self.__height = 240
        else:
            self.__height = height

    @property
    def raschet(self):
        return 2 * (self.__height / 100) + 0.3


# coat_1 = Coat_v3(int(input('Введите размер пальто для рассчёта:')))
# print(f'Вам потребуется {coat_1.raschet:.2f} метров ткани на пальто {coat_1.size} размер ')
# costume_1 = Costume_v3(int(input('Введите рост для костюма для рассчёта (как обычно, в сантиметрах):')))
# print(f'Вам потребуется {costume_1.raschet:.2f} метров ткани на костюм {costume_1.height} роста ')
# print(f'Всего вам потребуется {coat_1 + costume_1:.2f} метров ткани')

print()
print('--- Ver. 4 - Учитель ---')
print()

from abc import ABC, abstractmethod


class MyAbstractClass(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Clothes_v4(MyAbstractClass):
    def __init__(self, param=100):
        self.param = param

    @property
    def consumption_Coat(self, param):
        pass

    @property
    def consumption_Costume(self, param):
        pass

    @property
    def consumption(self):
        return self.consumption_Coat + self.consumption_Costume


class Coat_v4(Clothes_v4):
    @property
    def consumption(self):
        result = round(self.param / 6.5 + 0.5, 2)
        Clothes_v4.consumption_Coat = result
        return f'Расход ткани для пальто - {self.param} размера = {round(self.param / 6.5 + 0.5, 2)}'


class Costume_v4(Clothes_v4):
    @property
    def consumption(self):
        result = round(2 * self.param + 0.3, 2)
        Clothes_v4.consumption_Costume = result
        return f'Расход ткани для пальто - {self.param} размера = {round(2 * self.param + 0.3, 2)}'


# my_1 = Clothes_v4()
# my_2 = Coat_v4(35)
# print(my_2.consumption)
# my_3 = Costume_v4(183)
# print(my_3.consumption)
# print(f'Общий расход ткани = {my_1.consumption}')

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 3 --- ---')
print()
# Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка.
#   В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
#   В классе должны быть реализованы методы перегрузки арифметических операторов:
#       - сложение (__add__()),
#       - вычитание (__sub__()),
#       - умножение (__mul__()),
#       - деление (__truediv__()).
#   Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
#       умножение и обычное (не целочисленное) деление клеток, соответственно.
#   В методе деления должно осуществляться округление значения до целого числа.
#
# Сложение.
#   Объединение двух клеток.
#   При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
#
# Вычитание.
#   Участвуют две клетки.
#   Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
#       иначе выводить соответствующее сообщение.
#
# Умножение.
#   Создается общая клетка из двух.
#   Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
#
# Деление.
#   Создается общая клетка из двух.
#   Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(),
#   принимающий экземпляр класса и количество ячеек в ряду.
#   Данный метод позволяет организовать ячейки по рядам.
#
# Метод должен возвращать строку вида *****\n*****\n*****...,
#   где количество ячеек между \n равно переданному аргументу.
#   Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
#
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
#   Тогда метод make_order() вернет строку:
#       *****\n
#       *****\n
#       **.
#
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
#   Тогда метод make_order() вернет строку:
#       *****\n
#       *****\n
#       *****.
#
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.
# https://pythonworld.ru/osnovy/peregruzka-operatorov.html
#
# Доп. информация:
# - перегрузить сумму
# - см. урок

print()
print('--- Ver. 1 ---')
print()

from math import ceil

class Cell:
    # def __init__(self, cells_count=int(input('Введите количество ячеек: ')))):
    def __init__(self, cells_count=15):
        self.cells_count = cells_count

    # def make_order(self, cells_in_a_row=int(input('Введите количество ячеек в ряде: '))):
    def make_order(self, cells_in_a_row=5):
        rows = ceil(self.cells_count / cells_in_a_row)
        # print(rows)
        table = ''
        for el in range(1, rows+1):
            if el == rows and (self.cells_count % cells_in_a_row) > 0:
                table += f'{el}. {"*" * (self.cells_count % cells_in_a_row)}'
            else:
                table += f'{el}. {"*" * cells_in_a_row}\n'
        print(table)

    def __add__(self, other):
        count = self.cells_count + other.cells_count
        print(f'Общее количество клеток (__add__): {count}')

    def __sub__(self, other):
        count = self.cells_count - other.cells_count
        print(f'Общее количество клеток (__sub__): {count if count > 0 else "Количество ячеек 0 или меньше - вычитание невозможно!"}')

    def __mul__(self, other):
        count = self.cells_count * other.cells_count
        print(f'Общее количество клеток (__mul__): {count}')

    def __truediv__(self, other):
        count = round(self.cells_count / other.cells_count)
        print(f'Общее количество клеток (__truediv__): {count}')


obj_cell_1 = Cell()
obj_cell_2 = Cell()

obj_cell_1 + obj_cell_2
# obj_cell_1 + 3
obj_cell_1 - obj_cell_2
# obj_cell_1 - 3
obj_cell_1 * obj_cell_2
# obj_cell_1 * 3
obj_cell_1 / obj_cell_2
# obj_cell_1 / 3
print()

obj_cell_1.make_order()