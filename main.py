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

from random import randint

numbers = [randint(1, 101) for x in range(1, 20)]
print(numbers)
print(list(map(lambda x: x * 2, numbers)))
