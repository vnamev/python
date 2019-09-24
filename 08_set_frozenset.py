"""
Множество (set - frozenset) в python
     - “контейнер”, содержащий не повторяющиеся элементы в случайном порядке
"""

many_in_set = 'hello Maxxxon4eg'
new_many_in_set = set(many_in_set)
print(new_many_in_set)  # {'M', 'x', 'g', 'l', 'e', 'o', 'h', 'n', 'a', ' ', '4'}

# set удаляет повторяющиеся элементы из списка
many_list_set = ["max", "maxon", "maxon4eg", "ma", "max"]
print(set(many_list_set))  # {'max', 'maxon4eg', 'maxon', 'ma'}

# frozenset - НЕизменяемый тип данных
fro = frozenset(many_list_set)
print(fro.add(1)) # AttributeError: 'frozenset' object has no attribute 'add'
