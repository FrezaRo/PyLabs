group = {
    'Бурнышев Роман' :
    {'age': 35,
    'born_city': 'Perm',
    'height' : 175,
    'weight' : 75},
        'Иванов Иван' :
    {'age': 45,
    'born_city': 'Moscow',
    'height' : 165,
    'weight' : 65},
        'Петров Петр' :
    {'age': 55,
    'born_city': 'SPB',
    'height' : 185,
    'weight' : 85}
}

city_request = input('Из какого города нужен человек? (варианты: Perm, Moscow, SPB) ')

for name, docs in group.items():
    if docs.get('born_city') == city_request:
        print(name)

