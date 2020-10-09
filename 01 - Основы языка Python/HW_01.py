# Pull request

print()
print('--- --- Task 1 --- ---')
print()
# Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

print()
print('--- Ver. 1 - Моя ---')
print()

var_int = 123
var_float = 123.06
var_str = '123'
var_bool = True
var_list = [1, 2, 3]
var_tuple = (2, 2.4, 'Hello')
var_dict = {'name': 'Вася', 'age': 10}

print(var_int, type(var_int))
print(var_float, type(var_float))
print(var_str, type(var_str))
print(var_bool, type(var_bool))
print(var_list, type(var_list))
print(var_tuple, type(var_tuple))
print(var_dict, type(var_dict))

# var_int_1 = int(input('Введите число 1: '))
# var_int_2 = int(input('Введите число 2: '))
# var_int_3 = int(input('Введите число 3: '))
# var_text_1 = str(input('Введите строку 1: '))
# var_text_2 = str(input('Введите строку 2: '))
# var_text_3 = str(input('Введите строку 3: '))

# print(var_int_1, type(var_int_1))
# print(var_int_2, type(var_int_2))
# print(var_int_3, type(var_int_3))
# print(var_text_1, type(var_text_1))
# print(var_text_2, type(var_text_2))
# print(var_text_3, type(var_text_3))

print()
print('--- Ver. 2 - Преподаватель ---')
print()

a = "hello"
b = "world!"
print(f"{a}, {b}")
numb1 = int(input("Enter any number: "))
numb2 = int(input("Enter any number one more time: "))
print(f"You have choosen the numbers {numb1} and {numb2}")
word = input("Enter any word: ")
print(f"{word} - it's good choice")

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 2 --- ---')
print()
# Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

print()
print('--- Ver. 1 - Моя ---')
print()

# 15:37:39
# 56259

t = 56259

ch = 3600
cm = 60

h = t // ch
m = (t % ch) // cm
s = t % ch % cm

print(f'{h}:{m}:{s}')

print()
print('--- Ver. 2 - Преподаватель_1 ---')
print()

time = int(input("Enter the time in seconds: "))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")

print()
print('--- Ver. 3 - Преподаватель_2 ---')
print()

s = int(input("Введите время в секундах, для пересчёта в формат чч:mm;cc: "))
m = int(s / 60)
h = int(m / 60)

print(f"{h:02}:{m % 60:02}:{s % 60:02}")

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 3 --- ---')
print()
# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

print()
print('--- Ver. 1 - Моя ---')
print()

# n = input('Введите число: ')
n = 3

n1 = n
n2 = int(str(f'{n}{n}'))
n3 = int(str(f'{n}{n}{n}'))

n_sum = n1 + n2 + n3
print(n_sum)

print()
print('--- Ver. 2 - Преподаватель ---')
print()

n = input("Enter an integer: ")
print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 4 --- ---')
print()
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

print()
print('--- Ver. 1 - Моя ---')
print()

numbers = 123485780
n_max = 0

print(numbers, '\n')

while numbers != 0:
    number = numbers % 10
    print(number)

    if number > n_max:
        n_max = number

    numbers //= 10
    print(numbers, '\n')

print('Самое большое число: ', n_max)

print()
print('--- Ver. 2 - Преподаватель_1 ---')
print()

num_init = int(input("Введите целое положительное число: "))
greatest_dig = 0 # Переменная для хранения текущего максимума
num = num_init # Переменная для хранения оставшейся части числа (см цикл)

while num > 0: # Выполняем цикл, пока отсечения цифр числа (см ниже) его не обнулили
    digit = num % 10 # Опеределяем последнюю цифру
    if digit > greatest_dig: # Сравниваем её с ткущим максимумом
        greatest_dig = digit # При необходимости меняем текущий максимум
        if greatest_dig == 9: # Это условие не обязательно, но экономит время исполнения
            break
    num = num // 10 # Отсекаем от числа последнюю цифру

print()
print('--- Ver. 3 - Преподаватель_2 ---')
print()

# Функция с рекурсией
def num_max(num):
    if num < 10:
        print(num)
    else:
        num_max(num // 10)
        print(num % 10)
num_max(int(input("Введите число: ")))

print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 5 --- ---')
print()
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.

print()
print('--- Ver. 1 - Моя ---')
print()

# earnings = int(input('Введите сумму выручки: '))
# expenses = int(input('Введите сумму издержек: '))

employees = 12
earnings = 500000
expenses = 400000
print('Выручка: ', earnings)
print('Издержки: ', expenses)

result = earnings - expenses
if result < 0:
    print(f'Вы работаете в убыток ({result})')
elif result == 0:
    print(f'Вы работаете в ноль')
else:
    print(f'Вы работаете в прибыль (+{result})')
    profitability = result / earnings
    print(f'Рентабельность: {int(profitability * 100)}%')
    # employees = int(input('Введите количество сотрудников: '))
    print('Количество сотрудников: ', employees)
    print('Прибыль на 1 сотрудника: %.2f руб.' % (result / employees))

print()
print('--- Ver. 2 - Преподаватель ---')
print()

revenue = float(input("Введите значение выручки (тугрики) - "))
costs = float(input("Введите значение издержек (тугрики) - "))
result = revenue - costs
if result > 0:
    print(f"Поздравляю! Ваша компания работает с прибылью {result} тугриков!")
    print(f"Рентабельность выручки составила {result / revenue:.3f}")
    personal_n = int(input("Сколько счастливых целочисленных сотрудников работает в Вашей компании? "))
    print(f"Если Вы раздадите прибыль компании сотрудникам, то каждый получит по {result / personal_n:.3f} тугриков.")
elif result < 0:
    print(f"Увыб Ваша компания пока сработала с убытком {-result} тугриков! Старайтесь, у Вас всё получится!")
else:
    print(f"Ноль - это тоже хороший результат! Попросите у друга тугрик и пропейте его вместе за стабильность!")


print()
print('---------------------------------------------------------------------')

print()
print('--- --- Task 6 --- ---')
print()
# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить
# не менее b километров. Программа должна принимать значения параметров a и b и
# выводить одно натуральное число — номер дня.
#
# Например: a = 2, b = 3.
#
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
#
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

print()
print('--- Ver. 1 - Моя ---')
print()

day = 1
current_km = 2
goal_km = 3

print('История:')
while current_km < goal_km:
    print(f'День {day}: %.2f км.' % current_km)
    day += 1
    current_km *= 1.10
print()

print('Результат:')
print(f'На {day}-й день спортсмен достиг целевого результата ({goal_km} км.), в итоге пробежав %.2f км.' % current_km)

print()
print('--- Ver. 2 - Преподаватель ---')
print()

while True:
    days = 1
    start_km = int(input("Стартовый результат: "))
    last_km = int(input("Финальный результат: "))
    if start_km <= 0 or last_km < 0: # Это для тех случаев, если пользователь введёт отрицательное число
        print("Результаты должны быть больше нуля. Стартовое значение != 0.")
    else:
        while start_km < last_km:
            start_km += start_km * 0.1
            days += 1

        print(f"Спортсмен добьётся результата за {days} дней")
        break
