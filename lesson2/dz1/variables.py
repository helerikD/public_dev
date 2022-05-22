# объект описания через переменные 
from typing import Dict
from pprint3x import pprint

def insert_into_namespace(name, value, name_space=globals()):
    name_space[name] = value

def get_object_description():
    description = {
        'object_name': 'Студент',
        'first_name': 'Василий',
        'age': 21,
        'weight': 65.15,
        'IQ': 100,
        'cash': 11165.15,
        'currency': 'RUR',
        'psy_condition': 'procrastination',
        'avg_academic performance': 4.17,
        'victories on the personal front': -7,
        'list_to_do': ['найти еду', 'найти стажеровку', 'отработать в смену',\
                       'подготовиться к колоквиуму', 'потусить в ночном клубе']

    }
    types = {'str': str,
             'int': int,
             'float': float }
    for i in range(5):
        name_variable = input('Введите имя переменной:\n')
        if name_variable == 'exit':
            break
        value_variable = input('Введите значение переменной:\n')
        if value_variable == 'exit':
            break
        type_variable = input(f'Введите тип переменной из списка {types}:\n')
        if type_variable == 'exit':
            break
        if type_variable in types:
            insert_into_namespace(name_variable, types[type_variable](value_variable), locals())
        else:
            insert_into_namespace(name_variable, value_variable, locals())
        description[name_variable] = locals()[name_variable]
        print(name_variable, description[name_variable])
    return description


print(__name__)

if __name__ == "__main__":
    pprint(get_object_description())
