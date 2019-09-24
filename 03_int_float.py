# числа и работы с ними

# целые числа int
num_int_1 = 5
num_int_2 = 8

# операции над числами
print(num_int_1 + num_int_2)  # 13
print(num_int_1 - num_int_2)  # -3
print(num_int_1 * num_int_2)  # 40
print(num_int_1 / num_int_2)  # 0.625
print(num_int_1 // num_int_2)  # 0 Получение целой части от деления
print(num_int_1 % num_int_2)  # 5 Остаток от деления
print(num_int_1 ** num_int_2)  # 390625 Возведение в степень

# вещественные числа float
num_float_1 = 4
num_float_2 = 9

# операции над числами - аналогично как и в int
print(num_float_1 + num_float_2)  # 13
print(num_float_1 - num_float_2)  # -5
print(num_float_1 * num_float_2)  # 36
print(num_float_1 / num_float_2)  # 0.4444444444444444
print(num_float_1 // num_float_2)  # 0 Получение целой части от деления
print(num_float_1 % num_float_2)  # 4 Остаток от деления
print(num_float_1 ** num_float_2)  # 262144 Возведение в степень

# Можно складывать float + int
print(num_int_1 + num_float_1)  # 9

# складываем со строками - нельзя !!!!
str_1 = "What??? AAAA"
print(num_int_1 + num_float_2 + str_1)  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
