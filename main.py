"""
1) Task
Есть список ['MOSKOW', 'BISHKEK', 'ALMATY', 'BERLIN', 'ANKARA', 'AMSTERDAM'], 
преоброзовать названия в списке в нижний регистр применяя исключительно 
фукцию map, если хотите можете применить lamba функцию тоже, 
но можно обойтись и без него.
"""


cities = ['MOSKOW', 'BISHKEK', 'ALMATY', 'BERLIN', 'ANKARA', 'AMSTERDAM']

# def make_to_lower(city_name):
#     return city_name.lower()

cities_lower = list(map(lambda city_name: city_name.lower(), cities))

print(cities_lower)
