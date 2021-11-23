from random import choice
question = input('Напиши свой вопрос: ')
while question != 'нет':
    print (choice(['Да', 'Нет']))
    question = input('Напиши следующий вопрос или "нет" для остановки: ')
