print()
print('--- --- Task 1 --- ---')
print()
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# Дополнительные условия:
# - Никаких input()
# - Функция
# - Обработка ошибок
# - Документация

# hours = 168
# salary_per_hour = 750
# bonus = 5000

from sys import argv

script_name, hours, salary_per_hour, bonus = argv

def salary(argv):
    print('-' * 7, ' ДАНО ', '-' * 7)
    print(f'Название скрипта: {script_name[-11:]}')
    print(type(script_name))
    print(f'Отработано часов: {hours}')
    print(type(hours))
    print(f'Ставка: {salary_per_hour} р./час.')
    print(type(salary_per_hour))
    print(f'Премия: {bonus} р.')
    print(type(bonus))
    print()

    print(f'{int(hours) * int(salary_per_hour) + int(bonus)}')

salary(argv)

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 2 --- ---')
print()
# Представлен список чисел. Необходимо вывести элементы исходного списка,
#   значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
#   Для формирования списка использовать генератор.
#
# Пример исходного списка:
#   [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат:
#   [12, 44, 4, 10, 78, 123].

# Дополнительные условия:
# - Тестируем на указанных списках, а потом заменяем на генератор
# - Функция
# - Генератор условий

print()
print('--- Ver. 1 ---')
print()

task2_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
task2_list_new = []

def task2_func_1():
    for x in task2_list:
        if x == task2_list[0]:
            continue
        elif x > task2_list[task2_list.index(x)-1]:
            task2_list_new.append(x)
    return task2_list_new

print(task2_func_1())

print()
print('--- Ver. 2 ---')
print()

import random

def task2_func_2():
    task2_list.clear()
    task2_list_new.clear()

    count = 1

    while count < 50:
        x = random.randint(0, 1000)

        if task2_list_new == []:
            task2_list_new.append(x)
            # print(f'{x} - ОК')
        elif x > task2_list[-1]:
            task2_list_new.append(x)
            # print(f'{x} - ОК')
        else:
            task2_list_new.append('-' * (len(str(x))-2))
            # print(f'{x} - Не добавлено')
        task2_list.append(x)

        count += 1

    print(task2_list)
    print(task2_list_new)

task2_func_2()

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 3 --- ---')
print()
# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
#
# Подсказка: использовать функцию range() и генератор.

# Генератор списка
# Список один

start = 20
end = 241
numbers = (20, 21)

my_list = list(range(start, end))

print(f'Оригинальный списк:\n'
      f'{my_list}\n'
      f'')

my_list.clear()

print(f'Не универсальный список:\n'
      f'{[x for x in list(range(20, 241)) if x % 20 == 0 or x % 21 == 0]}'
      f'\n')

print(f'Универсальное решение:\n'
      f'{[x for x in list(range(start, end)) for y in numbers if x % y == 0]}'
      f'\n')

print('Тестирование:')
for x in list(range(start, end)):
    for y in numbers:
        if x % y == 0:
            my_list.append(x)
print(my_list)

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 4 --- ---')
print()
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
#
# Пример исходного списка:
#   [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат:
#   [23, 1, 3, 10, 4, 11]

# Не применяем множество
# В одну строку

task4_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([x for x in task4_list if task4_list.count(x) == 1])

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 5 --- ---')
print()
# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
#
# Подсказка: использовать функцию reduce().

task5_list = [x for x in list(range(100, 151)) if x % 2 == 0]
print(task5_list)
multiplier = 1

print()
print('--- Ver. 1 ---')
print()

for x in task5_list:
    # print(f'{multiplier} * {x} = {multiplier * x}')
    multiplier *= x
print(multiplier)

print()
print('--- Ver. 2 ---')
print()

from functools import reduce
task5_list = reduce((lambda x, y: x * y), task5_list)
print(task5_list)

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 6 --- ---')
print()
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
#     Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
#     Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

# Не бесконечный цикл
# Третий вариант решение включающее оба и без break

print()
print('--- count() ---')
print()

from itertools import count

for x in count(7, 2):
    if x > 15:
        break
    else:
        print(x)

print()
print('--- cycle() ---')
print()

from itertools import cycle

с = 0
for x in cycle(range(1, 5+1)):
    if с > 10:
        break
    print(x)
    с += 1

print()
print('--- count() + cycle() ---')
print()

from itertools import count
from itertools import cycle

start = 7
end = 15
step = 2

def task6_func(arg_1, arg_2, arg_3):
    temp_list = []
    for x in count(arg_1, arg_3):
        if x > arg_2:
            break
        else:
            temp_list.append(x)
    return temp_list

с = 0
c_end = 15
for x in cycle(task6_func(arg_1=start, arg_2=end, arg_3=step)):
    if с > c_end:
        break
    print(x)
    с += 1

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 7 --- ---')
print()
# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа,
#   а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
#
# Подсказка: факториал числа n — произведение чисел от 1 до n.
# Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

def task7_func(end):
    y = 1
    for x in count(1, 1):
        if x > end:
            break
        else:
            yield f'{x} ({y * x})'
            y *= x

n = 7

print(type(task7_func(n)))

for x in task7_func(n):
    print(x)

