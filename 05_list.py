# Вывод списка по индексу
list_num = [1, 4, 5, 5, 6]
print(list_num[0])
# 1

# Вывод последнего элемента списка по индексу
list_num = [1, 4, 5, 5, 6]
print(list_num[-1])
# 6

# Замена по индексу
list_num[0] = 5
print(list_num)
# [5, 4, 5, 5, 5]

# Конкатенация списка
list_num = list_num + [1, 8, 8]
print(list_num)
# [5, 4, 5, 5, 5, 1, 8, 8]

# Добавление в конец списка .append(x) - только один аргумент
list_num.append(4)
print(list_num)

# Обрезать(slice) список :х - обрезать всё после х числа (начнинаем с 0 не включая x)
list_x_num = list_num[:2]
print(list_x_num)
# [5,4] - было [5, 4, 5, 5, 5, 1, 8, 8, 4]

# Обрезать(slice) список х: - обрезать всё до х числа (начнинаем с 1)
list_y_num = list_num[5:]
print(list_y_num)
# [1, 8, 8, 4] - было [5, 4, 5, 5, 5, 1, 8, 8, 4]

# Создание списка с разными типам данных
typesInList = [3, True, 'Michael', 2.0]
print(typesInList)


############
# Методы и фукции списков python
#

# 1) - Index
z = [4, 1, 5, 4, 10, 4]
print(z.index(4))
# цифра 4 под индексом 0

# 2) - Count
random_list = [4, 1, 5, 4, 10, 4]
print(random_list.count(4))
# 3 - столько раз встречается цифра 4 в списке

# 3) - Sort по числам и строкам
sort_list = [3, 7, 4, 2]
sort_list.sort()  # от меньшего к большему
sort_list.sort(reverse=True)  # от большего к меньшему

sort_names = ['Steve', 'Rachel', 'Michael', 'Adam', 'Jessica', 'Lester']
sort_names.sort()  # сортировка по алфавиту ['Adam', 'Jessica', 'Lester', 'Michael', 'Rachel', 'Steve']

# 4) - Append - добавляет в список 1 элемент в конец
append_list = [7, 4, 3, 2]
new_list = [1, 1, 1]
append_list.append(3)  # [7, 4, 3, 2, 3]
append_list.append(4)  # [7, 4, 3, 2, 3, 4]
append_list.append(5)  # [7, 4, 3, 2, 3, 4, 5]
append_list.append(new_list)  # [7, 4, 3, 2, 3, 4, 5, [1, 1, 1]] - добавляется массив в конец массива

# 5) - Remove - удаляет первое вхождение значения в списке
remove_list = [7, 7, 4, 3, 2, 3]
remove_list.remove(7)  # удалит первый из одинаковых значений, принимает 1 значение

# 6) - Pop - удаляет элемент в укзанном индексе
pop_list = [7, 4, 3, 3]
pop_list.pop(1) # [7, 3, 3]
pop_list.pop() # [7, 3] - без указания индекса удалит последний элемент в списке
print(pop_list)

# 7) - Extend - расширяет список, добавляя элементы в конец. Преимущество над append в том, что могу добавлять списки.
extend_new = ['Vasia', 123]
extend_list = [7, 3, 3]
extend_list.extend([4, 5, 'Max']) # [7, 3, 3, 4, 5, 'Max']
extend_list.extend(extend_new) # [7, 3, 3, 4, 5, 'Max', 'Vasia', 123]

# 8) - Insert - вставляет элемент перед указанным индексом
insert_list = [7, 3, 3, 4, 5]
insert_list.insert(3, ['Max', True]) # где 3 - номер индекса
print(insert_list) #[7, 3, 3, ['Max', True], 4, 5]

# 9) - Copy -поверхностная копия списка
copy_list = [[7, 3, 3, 4, 5], ['Max', 'No More Max', True], 10, 23]
new_copy_list = copy_list.copy()
print(new_copy_list)  # [[7, 3, 3, 4, 5], ['Max', 'No More Max', True], 10, 23]

############
# Простые операции над списками
#

# Есть ли элемент в списке "x in s" - True если элемент x находится в списке
x_list = [2, 4, 9, "Max"]
print('Max' in x_list)  # True - есть в списке

# Есть ли элемент в списке "x in s" - True если элемент x не находится в списке
y_list = [1, 44, 99, "Maxon4eg"]
print('Janeee' not in x_list)  # True - нет в списке

# Конкатенация списков  x + y
list_xy = x_list + y_list
print(list_xy) # [2, 4, 9, 'Max', 1, 44, 99, 'Maxon4eg']

# * копирует список несколько раз. Делаем несколько одинаковых в одном списке
x_list = x_list * 5
print(x_list) # [2, 4, 9, 'Max', 2, 4, 9, 'Max', 2, 4, 9, 'Max', 2, 4, 9, 'Max', 2, 4, 9, 'Max']

# узнать длину списка len(list)
print(len(x_list)) # 20 элементов в индексе

# самый бльшой элемент списка / не может считать, когда есть и троки и числа в одном списке
n_list = [2, 3, 10] # 10 максимальное число
srt_list = ["Max", "Jane", "max", 'Sfsdfsdfsd']
print(max(srt_list)) # max - почему, не знаю... возможно регистр учитывается
print(min(srt_list)) # Jane - тоже хз, как оно считает минимальное значение в строках
print(sum(n_list)) # 15 сумма всех чисел
# print(sum(srt_list)) # строки не суммируются

# reverce - разворачиваем список
srt_list.reverse() # ['Sfsdfsdfsd', 'max', 'Jane', 'Max']
print(srt_list)

# генерируем список с помощью range
gen_list = [i for i in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# итерация списка с помощью цикла
for item in gen_list:
    print(item, end=" ") # 0 1 2 3 4 5 6 7 8 9

# преобразовать список в строку
list_to_str = ['spam', 'ham', 'eggs']
print(', '.join(list_to_str)) # spam, ham, eggs - строка, не массив
