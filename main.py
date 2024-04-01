"""
1) Task
Есть список ['MOSKOW', 'BISHKEK', 'ALMATY', 'BERLIN', 'ANKARA', 'AMSTERDAM'], 
преоброзовать названия в списке в нижний регистр применяя исключительно 
фукцию map, если хотите можете применить lamba функцию тоже, 
но можно обойтись и без него.
"""


# cities = ['MOSKOW', 'BISHKEK', 'ALMATY', 'BERLIN', 'ANKARA', 'AMSTERDAM']

# def make_to_lower(city_name):
#     return city_name.lower()

# cities_lower = list(map(lambda city_name: city_name.lower(), cities))

# print(cities_lower)


"""
2) Task
Отфильтруйте отобрав в новый список только четные числа 
[4, 3, 6, 8, 9, 7, 1, 2, 34, 5, 56, 76], 
и возведите в третью степень каждую цифру отфильтрованного списка.
"""

# numbers = [4, 3, 6, 8, 9, 7, 1, 2, 34, 5, 56, 76]
# numbers = filter(lambda x: x % 2 == 0, numbers)
# numbers = list(map(lambda x: pow(x, 3), numbers))
# print(numbers)


"""
3) Task
Вычислите сумму элементов списка [34, 5, 23, 68, 56, 890, 123, 564], 
но перед этим отфильтровать только нечетные числа.
"""

# from functools import reduce


# numbers = [34, 5, 23, 68, 56, 890, 123, 564]
# numbers = reduce(lambda x, y: x + y, filter(lambda x: x % 2 != 0, numbers))

# print(numbers)


"""
Task - 4
Удвоение чисел в списке:
Пусть дан список чисел. Удвоить каждое число в списке, используя map.
"""

# from random import randint

# numbers = [randint(1, 101) for x in range(1, 20)]
# print(numbers)
# print(list(map(lambda x: x * 2, numbers)))


"""
Task - 5
Отфильтровать четные числа из списка:
Пусть дан список чисел. Отфильтровать только четные числа из списка, 
используя filter.

Решали
"""

"""
Task - 6
Найти сумму квадратов чисел в списке:
Пусть дан список чисел. Найти сумму квадратов чисел в списке, 
используя reduce.
"""
# from random import randint
# from functools import reduce

# numbers = [randint(1, 3) for x in range(1, 5)]
# print(numbers)
# result = reduce(lambda x, y: x + y**2, numbers)
# print(result)


"""
Task-7
Отфильтровать слова по длине:
Пусть дан список строк. Отфильтровать только те строки, 
которые имеют длину больше 5 символов, используя filter.
"""

# strings = ['apple', 'banana', 'cherry', 'grape', 'watermelon']

# print(list(filter(lambda x: len(x) > 5, strings)))

"""
Task-8
Найти произведение элементов списка:
Пусть дан список чисел. Найти произведение всех элементов списка, 
используя reduce.
"""
# from random import randint
# from functools import reduce


# numbers = [randint(1, 10) for x in range(1, 4)]
# print(numbers)
# print(reduce(lambda x, y: x * y, numbers))


"""
Task-9
Оставить только положительные числа в списке:
Пусть дан список чисел. Оставить только положительные числа, 
используя filter.
"""
# from random import randint


# numbers = [randint(-10, 10) for x in range(1, 10)]
# print(numbers)

# print(list(filter(lambda x: x > 0, numbers)))


"""
Task-10
Преобразовать список целых чисел в строки:
Пусть дан список чисел. Преобразовать каждое число в строку, используя map.
"""

from random import randint

numbers = [randint(1, 10) for x in range(1, 10)]
print(numbers)

print(list(map(lambda x: str(x), numbers)))
