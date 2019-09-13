# Dict {} - список
create_dict = {}
d = {'dict': 1, 'dictionary': 2}

# создать словарь dict
dict_list = dict(short='dict', long='dictionary')
print(dict_list) # {'short': 'dict', 'long': 'dictionary'}

# с помощью функции dict:
dict_key = dict([(1, 1), (2, 4)])
print(dict_key) # {1: 1, 2: 4}

# с помощью метода fromkeys:
dict_fromkeys_1 = dict.fromkeys(['a', 'b'])
dict_fromkeys_2 = dict.fromkeys(['a', 'b'], 100)
print(dict_fromkeys_1) # {'a': None, 'b': None}
print(dict_fromkeys_2) # {'a': 100, 'b': 100}

# с помощью генераторов словарей
dict_generate = {a: a ** 2 for a in range(7)}
print(dict_generate) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

# узнаем значение по ключу
dict_key = {1: 2, 2: 4, 3: 9}
print(dict_key[1]) # 2
dict_key[4] = 16
print(dict_key) # {1: 2, 2: 4, 3: 9, 4: 16}

############
# методы словарей dict
#

dict.clear()
dict.copy()
dict.get()
dict.items()
dict.keys()
dict.pop()
dict.popitem()
dict.setdefault()
dict.update()
dict.values()