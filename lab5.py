group_list = [['Roman', 'Burnyshev', 35, 'Perm', 200],['Alex', 'Kakoitovich', 40, 'Moscow', 183],['Dmitriy', 'Tretiy', 55, 'SPeterburg', 165]]

group_dict = {
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


def max_height_in_list(s1):
    max_height = s1[0][4]
    highest = s1[0][0] + ' ' + s1[0][1]
    for i in range(1, len(s1)):
        if s1[i][4] > max_height:
            highest = s1[i][0] + ' ' + s1[i][1]
    return(highest)


def max_height_in_dict(s1):
    max_height = 0
    highest = list(s1.keys())[0]
    count = 0
    for name, age in s1.items():
        if age.get('height') > max_height:
            max_height = age.get('height')
            highest = list(s1.keys())[count]
        count += 1
    return(highest)



#запускаем функции поиска в списке и словаре
print(max_height_in_list(group_list))
print(max_height_in_dict(group_dict))

#сравниваем результаты поиска и выводим результат

