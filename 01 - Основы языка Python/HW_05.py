# Используем менеджер-контекста
# Работа только с файлами
# Используй файлы примеры

print()
print('--- --- Создать файлы --- ---')
print()

def file_create(name, text, encode):
    open(name, 'w', encoding=encode).write(text)
    open(name).close()
    print(name)
    print(open(name).read())
    print()

file_name = 'text_3.txt'
encode = 'windows-1251'
file_text = 'Иванов      10000.0\n' \
            'Петров      15000.0\n' \
            'Сидоров     25000.1\n' \
            'Иванова     15000.7\n' \
            'Петрова     19000.9\n' \
            'Сидорова    26000.1\n' \
            'Октябрьский 30000.5\n' \
            'Петровский  26000.4\n' \
            'Знаменский  12000.0\n' \
            'Корецкий    31000.9'
file_create(file_name, file_text, encode)

file_name = 'text_4.txt'
encode = 'utf-8'
file_text = 'One    - 1\n' \
            'Two    - 2\n' \
            'Three  - 3\n' \
            'Four   - 4'
file_create(file_name, file_text, encode)

file_name = 'text_6.txt'
encode = 'utf-8'
file_text = 'Fizra:       -     30(пр)  -       \n' \
            'Math:        10(л) 50(пр)  -       \n' \
            'History:     50(л) -       -       \n' \
            'Physics:     70(л) 20(пр)  18(лаб) \n' \
            'Informatics: 40(л) 12(пр)  20(лаб) \n' \
            'Literature:  10(л) -       8 (лаб) \n' \
            'Russian:     -     -       90(лаб)'
file_create(file_name, file_text, encode)

file_name = 'text_7.txt'
encode = 'windows-1251'
file_text = 'Brooms     ПАО 2500000  500000\n' \
            'Tandoor    АО  1245000  1880000\n' \
            'Honey-cake ЗАО 5250000  455000\n' \
            'Matrioshka OOO 4770000  511000\n' \
            'Сказка     ИП  10500000 5000000'
file_create(file_name, file_text, encode)

file_name = 'text_77.json'
encode = 'utf-8'
file_text = \
'[\n'                                   \
'   {\n'                                \
'       "Brooms"    : 2000000,\n'           \
'       "Tandoor"   : -635000,\n'          \
'       "Honey-cake": 4795000,\n'       \
'       "Matrioshka": 4259000,\n'       \
'       "Сказка"    : 5500000\n'            \
'   },\n'                               \
'   {\n'                                \
'       "average_profit": 4138500.0\n'  \
'   }\n'                                \
']'
file_create(file_name, file_text, encode)

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 1 --- ---')
print()
# Создать программно файл в текстовом формате,
#   записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
#
# Доп. информация:
# - Создать новый файл с уникальным именем
# - Бесконечный цикл ввода строк пользователем
# - Завершение цикла и закрытие файла осуществляет вводом пустой строки
# - Файл создаётся в том формате, в котором пользователь вводил данные - т.е. не всё одной строкой

print()
print('--- Ver. 1 ---')
print()

# import os
# os.remove('Task_1_file.txt')
#
# open('Task_1_file.txt', 'w', encoding='utf-8')
# while True:
#     x = input('Введите текст: ')
#     if x == '':
#         break
#     else:
#         open('Task_1_file.txt', 'a', encoding='utf-8').writelines(
#             ['\n' if open('Task_1_file.txt').read(1) != '' else '', str(x)])
# open('Task_1_file.txt').close()
#
# print(open('Task_1_file.txt', 'r', encoding='utf-8').read())

print()
print('--- Ver. 2 ---')
print()

# import os
# os.remove('Task_1_file.txt')

task1_ver2_list = [
    'test 1',
    'Lorem ipsum dolor sit amet,',
    'consectetur adipiscing elit,',
    'sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    'Ut enim ad minim veniam,',
    'quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    'Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
    'Excepteur sint occaecat cupidatat non proident,',
    'sunt in culpa qui officia deserunt mollit anim id est laborum.',
    1
]

open('Task_1_file.txt', 'w', encoding='utf-8')

for x in task1_ver2_list:
    open('Task_1_file.txt', 'a', encoding='utf-8').writelines(
        ['\n' if open('Task_1_file.txt').read(1) != '' else '', str(x)])
open('Task_1_file.txt').close()

print(open('Task_1_file.txt', 'r', encoding='utf-8').read())

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 2 --- ---')
print()
# Создать текстовый файл (не программно),
#   сохранить в нем несколько строк,
#   выполнить подсчет количества строк, количества слов в каждой строке.
#
# Доп. информация:
# - Комбинируем первое и второе задание. В первом создали файл, во втором обратились к нему

task2_list = open('Task_1_file.txt', 'r', encoding='utf-8').read().split('\n')
open('Task_1_file.txt').close()

print('Количество строк: ', len(task2_list))
print()

for x in task2_list:
    print(f'Количество символов в {task2_list.index(x)+1} строке: ', len(x))

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 3 --- ---')
print()
# Создать текстовый файл (не программно),
#   построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
#   вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
#
# Пример файла:
# Иванов 23543.12
# Петров 13749.32
#
# Доп. информация:
# - Учитываем, что числа из примера float
# - Именно средняя величина, а не медианная, но можно и медианную, если хочется.
# - Используем уже существующий файл

# import os
# os.remove('Task_3_file.txt')

employee_list = [
    ('Employee_01', 11000.00),
    ('Employee_02', 10000.00),
    ('Employee_03', 15000.00),
    ('Employee_04', 20000.00),
    ('Employee_05', 25000.00),
    ('Employee_06', 30000.00),
    ('Employee_07', 35000.00),
    ('Employee_08', 40000.00),
    ('Employee_09', 45000.00),
    ('Employee_10', 50000.00),
    ('Employee_11', 11000.00),
    ('Employee_12', 12000.00),
    ('Employee_13', 13000.00),
    ('Employee_14', 14000.00),
    ('Employee_15', 15000.00),
    ('Employee_16', 16000.00),
    ('Employee_17', 17000.00),
    ('Employee_18', 18000.00),
    ('Employee_19', 19000.00)
]

# Да, я вижу, что не программно, но я не вижу смысла в пункте упражнения, где надо ручками создать файл

open('Task_3_file.txt', 'w', encoding='windows-1251')

for x in employee_list:
    open('Task_3_file.txt', 'a', encoding='windows-1251').writelines(
        ['\n' if open('Task_3_file.txt').read(1) != '' else '',
         f'{str(employee_list[employee_list.index(x)][0])} - %.2f' % (int(employee_list[employee_list.index(x)][1]))])
open('Task_3_file.txt').close()

print(open('Task_3_file.txt', 'r', encoding='windows-1251').read())

print()
print('---------------------------------')
print()

# task3_list = open('Task_3_file.txt', 'r', encoding='utf-8').read().split('\n')
# open('Task_3_file.txt').close()
# print(task3_list)
# print()
#
# task3_dict = {}
#
# for x in task3_list:
#     temp = x.split(' - ')
#     task3_dict.update({str(temp[0]): float(temp[1])})
# print(task3_dict)
# print()

print()
print('---------------------------------')
print()

task3_list = open('text_3.txt', 'r', encoding='windows-1251').read().split('\n')
open('text_3.txt').close()
print(task3_list)
print()

task3_dict = {}

from itertools import count

for x in task3_list:
    temp = x.split(' ' * x.count(' '))
    task3_dict.update({str(temp[0]): float(temp[1])})
print(task3_dict)

print()
print('-----------------------------------------------------------------------------')
print()

print('Список сотрудников чья З/П ниже 20 тыс.:')
for x in task3_dict:
    if task3_dict.get(x) < 20000.0:
        print(x)
print()

print('Средний размер З/П: %.2f' % (sum(task3_dict.values()) / len(task3_dict)))
print()

import statistics

print('Медианная З/П:', statistics.median(task3_dict.values()))

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 4 --- ---')
print()
# Создать (не программно) текстовый файл со следующим содержимым:
#   One — 1
#   Two — 2
#   Three — 3
#   Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
#
# Доп. информация:
# - Считать, перевести на русский, записать в новый файл
# - Использовать встроенный переводчик в python
# - Задание со звёздочкой. Вместо арабских цифр сделать римские. Один - I
# - Задание со звёдочкой. Универсальное решение.

from googletrans import Translator

print('Оригинальный текст:')
print(open('text_4.txt', 'r').read())
# for line in open('text_4.txt', 'r').readlines():
#     print(line, end='')
open('text_4.txt').close()
print()

with open('text_4.txt', 'r') as task4_text:
    open('text_4_new.txt', 'w')
    for x in task4_text:
        temp_str = x
        temp_digit = temp_str[:temp_str.find(' ')]
        new_str = f'{Translator().translate(temp_digit, dest="ru").text} - {temp_str[temp_str.rfind(" ") + 1:]}'
        open('text_4_new.txt', 'a', encoding='utf-8').write(new_str)

    print('Новый текст:')
    print(open('text_4_new.txt', 'r', encoding='utf-8').read())
    print()

open('text_4.txt').close()
open('text_4_new.txt').close()

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 5 --- ---')
print()
# Создать (программно) текстовый файл,
#   записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

print('Исходные данные:')
file_name = 'task_5_file.txt'
encode = 'utf-8'
file_text = '1 2 45 88 22 9 111 557 324 1 1 2 3 4 889 658'
file_create(file_name, file_text, encode)

temp_list = []

print('Сумма:')
with open('task_5_file.txt', 'r') as task5_text:
    text = task5_text.read().split(' ')
    for x in text:
        temp_list.append(int(x))
    text.clear()
    text = temp_list
    print(sum(text))

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 6 --- ---')
print()
# Необходимо создать (не программно) текстовый файл,
#   где каждая строка описывает учебный предмет и наличие
#       лекционных,
#       практических и
#       лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
#
# Примеры строк файла:
#   Информатика: 100(л) 50(пр) 20(лаб).
#   Физика: 30(л) — 10(лаб)
#   Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
#
# Доп. информация:
# - Достать цифры и суммировать, вывести сумму для каждого предмета

print('Исходные данные:')
file_name = 'task_6_file.txt'
encode = 'windows-1251'
file_text = 'Информатика: 100(л) 50(пр) 20(лаб)\n' \
            'Физика: 30(л) - 10(лаб)\n' \
            'Физкультура: - 30(пр) -\n' \
            'Программирование: 30(л) 50(пр) 20(лаб)'
file_create(file_name, file_text, encode)

temp_dict = {}
temp_list_2 = []

with open('task_6_file.txt', 'r', encoding='windows-1251') as f_obj:
    for x in f_obj.readlines():
        temp_str = x
        temp_list = temp_str.split(' ')
        temp_name = temp_list[0][0:-1]
        # print(temp_str)
        # print(temp_list)
        # print(temp_name)

        for z in temp_list[1:]:
            if '-' in z:
                temp_list_2.append(int(0))
            else:
                temp_list_2.append(int(z[:z.find('(')]))
        # print(temp_list_2)
        temp_digit = sum(temp_list_2)

        temp_dict.update({temp_name:temp_digit})
        temp_list_2.clear()
    print(temp_dict)

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 7 --- ---')
print()
# Создать вручную и заполнить несколькими строками текстовый файл,
#   в котором каждая строка должна содержать данные о фирме:
#       название,
#       форма собственности,
#       выручка,
#       издержки.
#
# Пример строки файла: firm_1   ООО   10000   5000.
#
# Необходимо построчно прочитать файл,
#   вычислить прибыль каждой компании,
#   а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
#
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями,
#   а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
#
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджер контекста.

import re
task7_list = []
temp_dict.clear()
temp_list_2.clear()

with open('text_7.txt', 'r', encoding='windows-1251') as task7_text:
    text = str(task7_text.read())
    text = text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text)
    temp_list = text.split(' ')

    for x in temp_list[::4]:
        firm = f'{temp_list[temp_list.index(x)+1]}, {x}'
        gain = int(temp_list[temp_list.index(x)+2]) - int(temp_list[temp_list.index(x)+3])

        temp_dict.update({firm: gain})

    print(temp_dict)
    print()

    print('Прибыльные компании:')
    for x in temp_dict:
        if temp_dict.get(x) > 0:
            print(f'* {x}')
    print()

    for x in temp_dict:
        if temp_dict.get(x) > 0:
            task7_list.append(temp_dict.get(x))
    avg = sum(task7_list) / len(task7_list)
    med = statistics.median(task7_list)

    print('Средняя прибыль: %.2f' % (avg))
    print()

    print('Медианная прибыль:', med)
    print()

    temp_list_2 = [temp_dict]
    temp_list_2.append({'average_profit': int(avg)})
    print(temp_list_2)

open('task7_json.json', 'w', encoding='utf-8').write(str(temp_list_2))


print()
print('---------------------------------------------------------------------')

print()
print('--- --- Удалить все созданные файлы --- ---')
print()

import os
os.remove('text_3.txt')
os.remove('text_4.txt')
os.remove('text_6.txt')
os.remove('text_7.txt')
os.remove('text_77.json')

os.remove('Task_1_file.txt')
os.remove('Task_3_file.txt')
os.remove('task_5_file.txt')
os.remove('task_6_file.txt')

os.remove('text_4_new.txt')
os.remove('task7_json.json')