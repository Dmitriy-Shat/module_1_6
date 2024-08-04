my_dict = {'Maximus': 76584, 'Leonid': 45584, 'Petr': 5437}
print('Словарь:', my_dict)
print('Значение:', my_dict['Leonid'])
print('Ключа нет:', my_dict.get('Max'))
print('Изменения1:', my_dict)
my_dict.update({'Anna': 5689, 'Kira': 1234})
a = my_dict.pop('Petr')
print('Значение удаленой пары:', a)
print('Окончательный вариант:', my_dict)

# Множества

my_set = {'a', 'b', 'c', 'd', 'b', 'c', 'a', 1, 2, 3, 4, 3, 2, 1}
print('Множество:', my_set)
my_set.add("String")
my_set.add('@')
my_set.discard('c')
print('Измененное множество:', my_set)

