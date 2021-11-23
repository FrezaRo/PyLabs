from random import choice

question = input('Напиши свой вопрос: ')
questions_dict = {}

while question != 'нет':
    if question in questions_dict.keys():
        print (questions_dict[question])
    else:
        answer = choice(['Да', 'Нет'])
        questions_dict[question] = answer
        print (answer)
    
    question = input('Напиши следующий вопрос или "нет" для остановки: ')

