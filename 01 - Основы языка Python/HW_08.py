# 4, 5, 6 задача - это одна задача

print()
print('--- --- Task 1 --- ---')
print()
# Реализовать класс «Дата»,
#   функция-конструктор которого должна
#   принимать дату в виде строки формата «день-месяц-год».
#
# В рамках класса реализовать два метода.
#   Первый, с декоратором @classmethod, должен
#       извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#   Второй, с декоратором @staticmethod, должен
#       проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
#
# Проверить работу полученной структуры на реальных данных.
#
# Доп. информация:
# - Обычные цифры в виде строки
# - Всего-лишь два метода
# - В начале урока была конструкция
# - Можно добавить классические методы
# - Можно перезагрузить __str__
# - Можно создать промежуточный метод, который позволит взаимодействовать двум из задачи


class Date:
    def __init__(self, date='53-10-2020'):
        self.date = date

    # @classmethod
    # def str_to_int(cls, string):
    #     from datetime import datetime
    #     date = datetime.strptime(string, '%d-%m-%Y').date()
    #     print(date)
    #     print(type(date))
    #     return date

    @classmethod
    def str_to_int(cls, string):
        date = []
        for el in string.split('-'):
            date.append(int(el))
        return date

    @staticmethod
    def validation(obj):
        from datetime import datetime
        day = int(obj[0])
        month = int(obj[1])
        year = int(obj[2])

        # date = datetime(day=day, month=month, year=year).date()
        try:
            date = datetime(day=day, month=month, year=year).date()
        except ValueError as error_txt:
            if str(error_txt) == 'day is out of range for month':
                print('День выходит за диапазон месяца')
            elif str(error_txt) == 'month must be in 1..12':
                print('Месяц должен быть в диапазоне 1-12')
            else:
                print(error_txt)
        else:
            print(date)
            print('Дата введена корректно!')


x = Date()
x.date = Date().str_to_int(x.date)
print(x.date)
Date().validation(x.date)


print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 2 --- ---')
print()
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
#
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна
#   корректно обработать эту ситуацию и не завершиться с ошибкой.
#
# Доп. информация:
# - Создать своё исключение
# - Нельзя использовать try except
# - Фильтр, чтобы поймать состояние есть и его нужно использовать


class MyTrueDivError(Exception):
    def __init__(self, txt):
        self.txt = txt


class MyTrueDiv:
    def __init__(self, digit):
        self.digit = digit

    def __truediv__(self, other):
        if other.digit == 0:
            raise MyTrueDivError('Test')
        else:
            print(self.digit / other.digit)


a = MyTrueDiv(6)
b = MyTrueDiv(0)
a / b

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 3 --- ---')
print()
# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
#
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно,
#   пока пользователь сам не остановит работу скрипта,
#   введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
#
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и
#   вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и
#   отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
#
# Доп. информация:
# - Складываем список
# - Если введён текст, то выводим сообщение и продолжаем работу


class MyCheckListError(Exception):
    def __init__(self, txt):
        self.txt = txt


class CheckList:
    def __init__(self):
        self.list = []
        # for el in ('25', '87', '90'):
        for el in ('25', '87', '90', 'dsaasd', 'sdfs', 'stop'):
        # while True:
        #     el = input('Test: ')
            if el.upper() == 'STOP':
                break
            else:
                # try:
                #     x = int(el)
                # except ValueError:
                #     print('Test')
                #     continue
                # else:
                #     self.list.append(x)

                try:
                    if not el.isdigit():
                        raise MyCheckListError(f'Введённое значение ({el}) не является числом.')
                except MyCheckListError as error_text:
                    print(error_text)
                else:
                    self.list.append(int(el))
        print(self.list)


CheckList()


print()
print('---------------------------------------------------------------------')

# print()
# print('--- --- Task 4 --- ---')
# print()
# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе (Оргтехника) определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# Доп. информация:
# - Отдельный класс - Склад оргтехники
# - Родительский класс - Оргтехника
# - Классы потомки - Принтер, Сканер, Ксерокс
# - см. 2-ой урок, 6-ое задание
# - Склад уже должен быть наполнен, чтобы можно было тестировать
# - Не давайте пользователю выбор - используем выбор из списка возможных вариантов


# print()
# print('---------------------------------------------------------------------')

# print()
# print('--- --- Task 5 --- ---')
# print()
# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
#   можно использовать любую подходящую структуру, например словарь.
#
# Доп. информация:
# - Для хранения используем словарь
# - Здесь идёт речь о классе Склад
# - Склад - главный класс - ядро программы. Он отвечает за приём, перемещение, списание и утилизация.
# - Главные операции это приём и перемещение в, например, бухгалтерию или отдел

# print()
# print('---------------------------------------------------------------------')

# print()
# print('--- --- Task 6 --- ---')
# print()
# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
#   изученных на уроках по ООП.
#
# Доп. информация:
# - Получаемые данные должны соответствовать определённым типам.
# - Цена - целочисленное. Если введно некоррекно, то обрабатываем.

print()
print('--- --- Task 4, 5, 6 --- ---')
print()


class Stock:
    data_base_header = [
        {'id': 1, 'number': 111111, 'name': 'JVC 01', 'quantity': 2, 'in_use': 1, 'type': 'Printer'},
        {'id': 2, 'number': 111112, 'name': 'JVC 02', 'quantity': 4, 'in_use': 3, 'type': 'Scanner'},
        {'id': 3, 'number': 111113, 'name': 'JVC 03', 'quantity': 6, 'in_use': 5, 'type': 'Copier'},
        {'id': 4, 'number': 111114, 'name': 'JVC 04', 'quantity': 2, 'in_use': 2, 'type': 'Printer'},
        {'id': 5, 'number': 111115, 'name': 'JVC 05', 'quantity': 2, 'in_use': 2, 'type': 'Scanner'},
        {'id': 6, 'number': 111116, 'name': 'JVC 06', 'quantity': 2, 'in_use': 2, 'type': 'Copier'}
    ]

    data_base_detail = [
        {'id': 1, 'number': 111111, 'inv_number': 100001, 'department': 'Sales'},
        {'id': 2, 'number': 111111, 'inv_number': 100002, 'department': ''},
        {'id': 3, 'number': 111112, 'inv_number': 100003, 'department': 'Stock'},
        {'id': 4, 'number': 111112, 'inv_number': 100004, 'department': ''},
        {'id': 5, 'number': 111112, 'inv_number': 100005, 'department': 'Stock'},
        {'id': 6, 'number': 111112, 'inv_number': 100006, 'department': 'Stock'},
        {'id': 7, 'number': 111113, 'inv_number': 100007, 'department': ''},
        {'id': 8, 'number': 111113, 'inv_number': 100008, 'department': 'Logistics'},
        {'id': 9, 'number': 111113, 'inv_number': 100009, 'department': 'Logistics'},
        {'id': 10, 'number': 111113, 'inv_number': 100010, 'department': 'Logistics'},
        {'id': 11, 'number': 111113, 'inv_number': 100011, 'department': 'Logistics'},
        {'id': 12, 'number': 111113, 'inv_number': 100012, 'department': 'Logistics'},
        {'id': 13, 'number': 111114, 'inv_number': 100013, 'department': 'Sales'},
        {'id': 14, 'number': 111114, 'inv_number': 100014, 'department': 'Sales'},
        {'id': 15, 'number': 111115, 'inv_number': 100015, 'department': 'Stock'},
        {'id': 16, 'number': 111115, 'inv_number': 100016, 'department': 'Stock'},
        {'id': 17, 'number': 111116, 'inv_number': 100017, 'department': 'Logistics'},
        {'id': 18, 'number': 111116, 'inv_number': 100018, 'department': 'Logistics'}
    ]


class OfficeEquipment:
    @staticmethod
    def __init__(__menu_item):
        if __menu_item == 1:
            OfficeEquipment.check_item()
        elif __menu_item == 2:
            OfficeEquipment.stock_to_department()
        elif __menu_item == 3:
            OfficeEquipment.department_to_stock()
        elif __menu_item == 4:
            OfficeEquipment.info_hdr()
        elif __menu_item == 5:
            OfficeEquipment.info_dtl()

    @staticmethod
    def check_item():
        print('--- check_item ---\n')
        # item = 111123
        item = int(input('Введите номер товара: '))

        for el in Stock.data_base_header:
            if el.get('number') != item and el != Stock.data_base_header[-1]:
                continue
            elif el.get('number') != item and el == Stock.data_base_header[-1]:
                print('Такого товара нет!')
                msg = input('Внести товар (Y/N)? ')
                # msg = 'Y'
                # msg = 'N'
                if msg.upper() == 'Y':
                    print('\n')
                    OfficeEquipment.new_item()
                    break
                else:
                    print('\n')
                    break
            else:
                print('Товар найден!')
                print('\n')
                OfficeEquipment.change_quantity(el.get('id'))
                break

    @staticmethod
    def new_item():
        print('--- new_item ---\n')
        print(Stock.data_base_header[-1])

        # number = 111117
        # name = 'JVC 07'
        # quantity = 3
        number = int(input('Введите номер товара: '))
        name = input('Введите название товара: ')
        quantity = int(input('Введите количество: '))

        # type_item = 'Printer'
        print()
        type_item = None
        while True:
            type_item = input(
                        '1. Printer\n'
                        '2. Scanner\n'
                        '3. Copier\n'
                        )
            if type_item == '1':
                type_item = 'Printer'
                break
            elif type_item == '2':
                type_item = 'Scanner'
                break
            elif type_item == '3':
                type_item = 'Copier'
                break
            else:
                print()
                print('Ошибка! Введите одну из цифр.')
                print()
                continue
        print(type_item)

        item_hdr = {
            'id': Stock.data_base_header[-1].get('id') + 1,
            'number': number,
            'name': name,
            'quantity': quantity,
            'in_use': 0,
            'type': type_item
        }

        Stock.data_base_header.append(item_hdr)
        print(Stock.data_base_header[-1])
        print()

        print(Stock.data_base_detail[-1])

        # inv_number = [100019, 100020, 100021]
        inv_number = []
        for el in range(1, quantity+1):
            inv_number.append(int(input('Введите инвентаризационный номер: ')))
        for el in inv_number:
            item_dtl = {
                'id': Stock.data_base_detail[-1].get('id') + 1,
                'number': number,
                'inv_number': el,
                'department': ''
            }
            Stock.data_base_detail.append(item_dtl)
        for el in range(quantity, 0, -1):
            print(Stock.data_base_detail[-el])
        print('\n')

    @staticmethod
    def change_quantity(id):
        print('--- change_quantity ---\n')
        # quantity = 5
        quantity = int(input('На какое количество изменить количество товара? '))
        for el in Stock.data_base_header:
            if el['id'] == id:
                print(el)
                el['quantity'] = (el.get('quantity') + quantity)
                print(el)
        print('\n')

    @staticmethod
    def stock_to_department():
        print('--- stock_to_department ---\n')
        # item = 111112
        item = int(input('Введите номер товара: '))

        for el in Stock.data_base_header:
            if el.get('number') == item:
                free_stock = el.get('quantity') - el.get('in_use')
                if free_stock <= 0:
                    print('Нет свободных единиц товара!')
                    break
                else:
                    print(el)
                    el['in_use'] += 1
                    print(el)
                    print()

                    # department = 'Sales'
                    department = input('Введите наименование департамента: ')
                    for el in Stock.data_base_detail:
                        if el.get('number') == item and el.get('department') == '':
                            print(el)
                            print(f'Выдать товар с инвентаризационным номером: {el.get("inv_number")}')
                            el['department'] = department
                            print(el)
                            break
        print('\n')

    @staticmethod
    def department_to_stock():
        print('--- department_to_stock ---\n')
        # inv_number = 100003
        inv_number = int(input('Введите инвентаризационный номер: '))
        # department = 'Stock'
        # department = input('Введите название отдела: ')

        number = None
        for el in Stock.data_base_detail:
            # if el['inv_number'] == inv_number and el['department'] == department:
            if el['inv_number'] == inv_number:
                print(el)
                el['department'] = ''
                number = el['number']
                print(el)
                break
        print()

        for el in Stock.data_base_header:
            if el['number'] == number:
                print(el)
                el['in_use'] -= 1
                print(el)
        print()

    @staticmethod
    def info_hdr():
        print('--- info_hdr ---\n')
        print(f'|   id   |   number   |   name   |   quantity   |   in_use   |   type   |')
        for el in Stock.data_base_header:
            print(f'     {el.get("id")}'
                  f'       {el.get("number")}'
                  f'      {el.get("name")}'
                  f'         {el.get("quantity")}'
                  f'              {el.get("in_use")}'
                  f'        {el.get("type")}')
        print('\n')

    @staticmethod
    def info_dtl():
        print('--- info_dtl ---\n')
        print(f'|   id   |   number   |   inv_number   |   department   |')
        for el in Stock.data_base_detail:
            print(f'{"    " if el.get("id") < 10 else "   "}{el.get("id")}'
                  f'        {el.get("number")}'
                  f'         {el.get("inv_number")}'
                  f'           {el.get("department")}')
        print('\n')


def menu():
    print('\n--- STARTING PROGRAM ---\n')
    # for el in ['1']:
    # for el in ['1', '2', '3', '4', '5', 'sdfsdfas', 'stop']:
    #     menu_item = el
    while True:
        menu_item = input(
            '1. Принять новую единицу оргтехники на склад\n'
            '2. Передать единицу оргтехники в отдел\n'
            '3. Вернуть единицу оргтехники на склад\n'
            '4. Посмотреть остаток на складе\n'
            '5. Посмотреть детали склада\n'
            '\n')

        if menu_item in ('1', '2', '3', '4', '5'):
            OfficeEquipment(int(menu_item))
        elif menu_item.upper() == 'STOP':
            print('\n--- ENDING PROGRAM ---\n')
            break
        else:
            print('Ошибка!\n'
                  'Введите одну из цифр в меню.\n')


menu()


print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 7 --- ---')
print()
# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
#   выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
#
# Доп. информация:
# - https://xn--24-6kcaa2awqnc8dd.xn--p1ai/umnozhenie-kompleksnyh-chisel.html
# - Не используем встроенную функцию Комплекс

# print()
# print('--- Ver. 1 ---')
# print()


class Complex:
    def __init__(self, z, zi=1):
        self.z = z
        self.zi = zi

    def __add__(self, other):
        print(f'{"-" * 3} Сложение комплексных чисел: {"-" * 3}\n'
              f'z1 = {self.z}\n'
              f'i1 = {self.zi}\n'
              f'z2 = {other.z}\n'
              f'i2 = {other.zi}\n'
              f'\n'
              f'Процесс расчёта:\n'
              f'(z1, zi1) + (z2, zi2)\n'
              f'((z1 + z2), (zi1 + zi2))\n'
              f'(z3, zi3)\n'
              f'\n'
              f'Расчёт:\n'
              f'({self.z}, {self.zi}) + ({other.z}, {other.zi})\n'
              f'({self.z} + {other.z}), ({self.zi} + {other.zi})\n'
              f'({self.z + other.z}, {self.zi + other.zi})\n'
              f'\n'
              f'z3 = {self.z + other.z}\n'
              f'zi3 = {self.zi + other.zi}\n')

    def __mul__(self, other):
        print(f'{"-" * 3} Умножение комплексных чисел: {"-" * 3}\n'
              f'z1 = {self.z}\n'
              f'zi1 = {self.zi}\n'
              f'z2 = {other.z}\n'
              f'zi2 = {other.zi}\n'
              f'\n'
              f'Процесс расчёта:\n'
              f'(z1, zi1) * (z2, zi2)\n'
              f'(z1 * z2) + (z1 * zi2) + (zi1 * z2) + (zi1 * zi2)\n'
              f'(z3) + (zi3) + (zi4) + ((z * z)**i**2)\n'
              f'(z3) + (zi3) + (zi4) + (zi5**-1)\n'
              f'(z3) + (zi3) + (zi4) + (z4)\n'
              f'((z3 + z4), (zi3 + zi4))\n'
              f'(z5, zi5)\n'
              f'\n'
              f'Расчёт:\n'
              f'({self.z}, {self.zi}) * ({other.z}, {other.zi})\n'
              f'({self.z} * {other.z}) + ({self.z} * {other.zi}) + ({self.zi} * {other.z}) + ({self.zi} * {other.zi})\n'
              f'({self.z * other.z}) + ({self.z * other.zi}) + ({self.zi * other.z}) + (({(self.zi * other.zi)})**i**2)\n'
              f'({self.z * other.z}) + ({self.z * other.zi}) + ({self.zi * other.z}) + (({(self.zi * other.zi)})**-1)\n'
              f'({self.z * other.z}) + ({self.z * other.zi}) + ({self.zi * other.z}) + ({(self.zi * other.zi)**-1})\n'
              f'(({self.z * other.z} + {(self.zi * other.zi)**-1}), ({self.z * other.zi} + {self.zi * other.z}))\n'
              f'({(self.z * other.z) + ((self.zi * other.zi)**-1)}, {(self.z * other.zi) + (self.zi * other.z)})\n'
              f'\n'
              f'z5 = {(self.z * other.z) + ((self.zi * other.zi)**-1)}\n'
              f'zi5 = {(self.z * other.zi) + (self.zi * other.z)}\n')


z1 = Complex(6)
z2 = Complex(2)
z1 + z2
z1 * z2