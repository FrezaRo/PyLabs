#импорт функции сравнения строк методом n-грамм из прошлой лабы
from lab5_3 import string_compare as sc
class Person:
    def __init__(self, name, age, height, weight, city_born):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.city_born = city_born
    
    def __repr__(self):
        return "Person('%s', %s, %s, %s,'%s')" % (self.name, self.age, self.height, self.weight, self.city_born)


#ввод данных
romanb = Person('Роман Бурнышев', 35, 175, 75, 'Пермь')
alexk = Person('Александр Какойтович', 30, 190, 85,'Петербург')
krisb = Person('Кристиан Бэйл', 47, 183, 70, 'Лондон')        

#словарь
people = {
    romanb.name: romanb,
    alexk.name: alexk,
    krisb.name: krisb
}

#функция поиска по росту (+- 2%)
def find_heist(h):
    for i in people.values():
        if 0.98 * h <= i.height <= 1.02 * h: 
            return 'Рост %s см у %s' % (i.height, i.name)
    return 'Нет никого с ростом %s см' % (h)
        
#функция поиска по имени
def find_name(name):
    for i in people.values():
        if sc(str(name), str(i.name)) > 0.6:   #узнать какой кэфф использовать для метода сравнения энграмм
            return i
    return 'Нет никого с именем %s' % (name)

#выбор запроса
#print('1. Ищем по росту' + '\n' )
choice = int(input('1. Ищем по росту \n2. Ищем по имени \nВведите число: '))

#проверка корректности, ввод данных и запуск функций по запросу
if choice == 1:
    height_req = int(input('Ищем людей с ростом Х см. Введите Х:  '))
    print(find_heist(height_req))
elif choice == 2:
    name_req = input('Ищем человека с именем фамилией: ')
    print(find_name(name_req))
else:
    print('Некорректный выбор')

