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


#ищем самого высокого
max_height = 0
highest = list(group.keys())[0]
count = 0
for name, age in group.items():
    if age.get('height') > max_height:
        max_height = age.get('height')
        highest = list(group.keys())[count]
    count += 1

print(highest + ' - самый высокий')
#    if group.get('height') > max_height:
#        pass
     #   max_height = 





