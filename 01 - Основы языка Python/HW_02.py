#Pull request
#Pull request
#Pull request

print()
print('--- --- Task 1 --- ---')
print()
# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

print()
print('--- Ver. 1 - Моя ---')
print()

global L1
global L2
global L3

my_list_1 = [
    123,    # int
    10.5,   # float
    'XYZ',  # str
    True,   # bool
    [1, 10.5, 'XYZ', True,
        [1, 10.5, 'XYZ', True],
        (1, 10.5, 'XYZ', True),
        {'int': 1, 'float': 10.5, 'str': 'XYZ', 'bool': True}],  # list
    (1, 10.5, 'XYZ', True,
        [1, 10.5, 'XYZ', True],
        (1, 10.5, 'XYZ', True),
        {'int': 1, 'float': 10.5, 'str': 'XYZ', 'bool': True}),  # tuple
    {'int': 1, 'float': 10.5, 'str': 'XYZ', 'bool': True,
        'list': [1, 10.5, 'XYZ', True],
        'tuple': (1, 10.5, 'XYZ', True),
        'dict': {'int': 1, 'float': 10.5, 'str': 'XYZ', 'bool': True}}   # dict
]

for i in my_list_1:
    L1 = my_list_1.index(i)
    print('Индекс:   ', my_list_1.index(i))
    print('Значение: ', i)
    print('Класс:    ', type(i))
    print()

    if type(i) in (list, tuple):
        for x in i:
            L2 = i.index(x)
            print(' - ' * 3, 'Индекс:   ', f'{L1}.{i.index(x)}')
            print(' - ' * 3, 'Значение: ', x)
            print(' - ' * 3, 'Класс:    ', type(x))
            print()

            if type(x) in (list, tuple):
                for y in x:
                    L3 = i.index(y)
                    print(' - ' * 6, 'Индекс:   ', f'{L1}.{L2}.{i.index(y)}')
                    print(' - ' * 6, 'Значение: ', y)
                    print(' - ' * 6, 'Класс:    ', type(y))
                    print()

            elif type(x) == dict:
                for n, (key, val) in enumerate(x.items(), 0):
                    print(' - ' * 6, 'Индекс:   ', f'{L1}.{L2}.{n}')
                    print(' - ' * 6, 'Ключ:     ', key)
                    print(' - ' * 6, 'Значение: ', val)
                    print(' - ' * 6, 'Класс:    ', type(val))
                    print()

            else:
                continue

    elif type(i) == dict:
        for n, (key, val) in enumerate(i.items(), 0):
            print(' - ' * 3, 'Индекс:   ', f'{L1}.{n}')
            print(' - ' * 3, 'Ключ:     ', key)
            print(' - ' * 3, 'Значение: ', val)
            print(' - ' * 3, 'Класс:    ', type(val))
            print()

            if type(val) in (list, tuple):
                for y in val:
                    print(' - ' * 6, 'Индекс:   ', f'{L1}.{L2}.{val.index(y)}')
                    print(' - ' * 6, 'Значение: ', y)
                    print(' - ' * 6, 'Класс:    ', type(y))
                    print()
            elif type(val) == dict:
                for n, (key, val) in enumerate(val.items(), 0):
                    print(' - ' * 6, 'Индекс:   ', f'{L1}.{L2}.{n}')
                    print(' - ' * 6, 'Ключ:     ', key)
                    print(' - ' * 6, 'Значение: ', val)
                    print(' - ' * 6, 'Класс:    ', type(val))
                    print()

            else:
                continue

    else:
        continue

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 2 --- ---')
print()
# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print()
print('--- Ver. 1 - Моя ---')
print()

my_list_2 = [3, 2, 5, 9, 10, 6, 13, 34, 56, 78]
print(my_list_2)
print()

for x in my_list_2[0::2]:
    i = my_list_2.index(x)

    if len(my_list_2[i:]) < 2:
        break

    element_1 = my_list_2[i]
    element_2 = my_list_2[i+1]
    my_list_2[i] = element_2
    my_list_2[i+1] = element_1
    print(my_list_2)

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 3 --- ---')
print()
# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

print()
print('--- Ver. 1 - Моя - Список ---')
print()

# month = int(input('Введите месяц: '))
month = 11

if month in [12, 1, 2]:
    print('Зима')
elif month in [3, 4, 5]:
    print('Весна')
elif month in [6, 7, 8]:
    print('Лето')
elif month in [9, 10, 11]:
    print('Осень')
else:
    print('Error! \n'
          'Вы ввели некорректное число!')

print()
print('--- Ver. 2 - Моя - Словарь ---')
print()

# month = int(input('Введите месяц: '))
month = 12
months = {(12 or 1 or 2): 'Зима', (3 or 4 or 5): 'Весна', (6 or 7 or 8): 'Лето', (9 or 10 or 11): 'Осень'}

if month not in months:
    print('Error! \n'
          'Вы ввели некорректное число!')
else:
    print(months.get(month))

print()
print('--- Ver. 3 - Моя - Список и словарь ---')
print()

print('Мне не удалось придумать варианта, при котором либо список, либо словарь не были добавлены ради галочки.')

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 4 --- ---')
print()
# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

print()
print('--- Ver. 1 - Моя ---')
print()

str_4 = 'Aut et voluptatem totam. Et id quia ad. Et beatae sit nam perspiciatis neque modi et. Qui beatae culpa quaerat quidem illum.'
str_4 = list(str_4.split(' '))

for n, x in enumerate(str_4, 1):
    print(n, x[0:10:1]) if len(x) > 10 else print(n, x)

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 5 --- ---')
print()
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка.
# Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
#
# Используем другой тип данных, чтобы увидеть куда вставилась оценка
# Нельзя использовать reversed() и sorted()
# Работаем с индексами, методами

print()
print('--- Ver. 1 - Моя ---')
print()

input_rating = 1
max_rating = 9

while input_rating <= max_rating:

    rating = [7, 5, 3, 3, 2]
    text = []

    for i, x in enumerate(rating, 0):
        text.append(f'{x} ({i})')
    print(text)
    text.clear()

    print('Input Rating: ', input_rating)

    if rating[0] < input_rating and input_rating is not rating:
        insert_index = 0
    elif rating[-1] > input_rating and input_rating is not rating:
        insert_index = rating.index(rating[-1]) + 1
    else:
        for i, x in enumerate(rating, 0):
            if x == input_rating:
                insert_index = i + 1
            elif x > input_rating and input_rating is not rating:
                insert_index = i + 1

    print('Insert Index: ', insert_index)
    rating.insert(insert_index, input_rating)

    for i, x in enumerate(rating, 0):
        text.append(f'{x} ({i})')
    print(text)

    input_rating += 1
    print()

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 6 --- ---')
print()
# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
#
# Пример готовой структуры:
# - Список с кортежами
# - Номер товара - автоматически увеличивается
# - Словарь в котором сохраняем по 4 атрибутам
# - Можем добавить проверку
#
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Необходимо собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
#
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
#
# Пользователь заходит и мы у него спрашиваем сколько товаров он хочет ввести
# Он говорит 3
# Мы три раза выводим все атрибуты
# Автоматически выводим аналитику
#
# Второй способ:
# - Заходит
# - Хочешь добавить товар?
# - Ок
# - Выводим атрибуты
# - Вводит
# - Спрашиваем:
# * аналитику
# * ещё товар
# * выйти

print()
print('--- Ver. 1 - Моя ---')
print()

data_base = [
    (1, {'Название': 'Компьютер', 'Цена': 20000.00, 'Количество': 5, 'Единица измерения': 'шт.'}),
    (2, {'Название': 'Принтер', 'Цена': 6000.00, 'Количество': 2, 'Единица измерения': 'шт.'}),
    (3, {'Название': 'Сканер', 'Цена': 2000.00, 'Количество': 7, 'Единица измерения': 'шт.'})]

data_base_input = [
    ('Монитор', 7000.00, 6),
    ('Xbox elite controller', 9000.00, 3),
    ('Xbox elite controller 2', 15000.00, 3),
    ('Quake IV', 429.00, 5),
    ('Far Cry', 599.00, 5),
    ('Far Cry 2', 599.00, 5),
    ('Far Cry 3', 999.00, 5),
    ('Far Cry 4', 1499.00, 5),
    ('Far Cry 5', 1999.00, 5),
    ('Far Cry: New Dawn', 1999.00, 5),
    ('Planetary Annihilation: TITANS', 725.00, 5),
    ('Nintendo Switch. ver. 1', 18000.00, 5),
    ('Nintendo Switch. ver. 2', 23000.00, 5),
    ('Nintendo Switch. Lite', 16000.00, 5),
    ('Mortal Kombat 1', 100.00, 5),
    ('Mortal Kombat 2', 100.00, 5),
    ('Mortal Kombat 3', 100.00, 5),
    ('Mortal Kombat 4', 100.00, 5),
    ('Mortal Kombat 9', 100.00, 5),
    ('Mortal Kombat 10', 1500.00, 5),
    ('Mortal Kombat 11', 1500.00, 5)
]

while True:

    answer = str(input('Хотите внести товар (Y/N)? '))

    if answer in ('y', 'Y', 'yes', 'Yes'):
        for x in data_base:
            print(x)
        print()

        count = int(input('Сколько товаров хотите внести? '))
        # count = 5
        good = 0
        print('Количество товаров на внесение:', count)
        print()

        while good < count:

            # id = date_base[-1][0] + 1
            # name = str(input('Введите название товара: '))
            # price = float(input('Введите цену товара: '))
            # quantity = int(input('Введите количество товара: '))
            # unit = str(input('Введите единицу измерения: ')) or 'шт.'

            id = data_base[-1][0] + 1
            name = data_base_input[good][0]
            price = data_base_input[good][1]
            quantity = data_base_input[good][2]
            unit = 'шт.'

            print('ID:', id)
            print('Название товара:', name)
            print('Цена:', price)
            print('Количество:', quantity)
            print('Ед. измерения:', unit)
            print()

            data_base.append((
                id,
                {
                    'Название': name,
                    'Цена': price,
                    'Количество': quantity,
                    'Единица': unit
                }))

            for x in data_base:
                print(x)

            good += 1
            print()

        print('АНАЛИТИКА')
        name = []
        price = []
        quantity = []

        for x in data_base:
            name.append(x[1].get('Название'))
            price.append(x[1].get('Цена'))
            quantity.append(x[1].get('Количество'))

        print(name)
        print(price)
        print(quantity)
        print()

    else:
        print('До свидания!')
        break

