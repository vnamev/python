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

# удалить значение с ключом ['Vasek'] из словаря
dictionary = {'Max': 'Developer', 'Vasek': 'NeDeveloper'}
del dictionary['Vasek']
print(dictionary)

############
# методы словарей dict
#


# dict.update()
# Если нужно изменить и/или добавить несколько пар сразу.
dictionary.update({
    'Max': 'Developer by Python',
    'спит': 'отдыхает и набирается богатырской силушкой',
    'ест': 'пополняет жировые запасы...жирбаза, вали а бассик'
})

# dict.get()
# возвращает значение по ключу. Если указанного ключа не существует, метод вернёт None.
dictionary.get('Max') # {'Max': 'Developer'}
dictionary.get('Nekto') # None
dictionary.get('Nekto', 'Не существует ключа') # Значение по умолчанию "Не суще..." если данного ключа нет

# dict.pop()
# удаляет ключ и возвращает соответствующее ему значение. Принимает только один ключ.
dictionary.pop('Max') # Удалит ключ и значение  - Вернёт -> Developer by Python

# dict.keys()
# возвращает коллекцию ключей
dictionary.keys() # dict_keys(['спит', 'ест'])

# dict.values()
# возвращает коллекцию значений
dictionary.values() # dict_values(['отдыхает и набирается богатырской силушкой', 'пополняет жировые запасы...жирбаза, вали а бассик'])


# dict.items()
# возвращает пару ключ - значение
print(dictionary.items()) # dict_items([('спит', 'отдыхает и набирается богатырской силушкой'), ('ест', 'пополняет жировые запасы...жирбаза, вали а бассик')])
print(dictionary)


# dict.clear()
# удаляет весь словарь
print(dict_list.clear())



############
# Итерация словаря по for in
#

# по ключу key. Можно использовать имя словаря
for key in dictionary:
    print(key) # спит ест

# по ключу key. Можно использовать метод .keys()
for key in dictionary.keys():
    print(key) # спит ест

# по методу .items - получаем пару "ключ-значение" на каждую итерацию
for key, value in dictionary.items():
    print(key + " : " + value) # спит : отдыхает и набирается богатырской силушкой
                                # ест : пополняет жировые запасы...жирбаза, вали а бассик

for value in dictionary.values():
    print(value) #отдыхает и набирается богатырской силушкой
                 # пополняет жировые запасы...жирбаза, вали а бассик

