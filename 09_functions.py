# простая функция
def add(x, y):
    return x + y
print(add(4, 13))  # 17
print(add("qwe", "rty"))  # qwerty
# print(add(4, "asd"))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# пустая функция возвращает None
def whatpass():
    pass
print(whatpass()) # None

# Функция может быть любой сложности и возвращать любые объекты (списки, кортежи, и даже функции!):
def newfunc(n):
    def myfunc(x):
        return x + n
    return myfunc

new = newfunc(100)  # new - это функция
new(200)


####################################
###  Аргументы

def func(a, b, c=2):  # c - необязательный аргумент
    return a + b + c

func(1, 2)  # a = 1, b = 2, c = 2 (по умолчанию)
func(1, 2, 3)  # a = 1, b = 2, c = 3
func(a=1, b=3)  # a = 1, b = 3, c = 2
# func(a=3, c=6)  # a = 3, c = 6, b не определен

# Неопределенное количество аргументов *args - кортеж аргументов
def func(*args):
    return args

print(func(1, 2, 3, 'abc'))  # (1, 2, 3, 'abc')
print(func())  # ()
print(func(1))  # (1,)

# Аргументы **kwargs в общем собираются в словарь
def func(**kwargs):
    return kwargs

print(func(a=1, b=2, c=3))  # {'a': 1, 'b': 2, 'c': 3}
print(func())  # {}
print(func(a='python'))  # {'a': 'python'}

# Анонимные функции lambda - могут содержать лишь одно выражение
func = lambda x, y: x + y
print(func(1, 2))  # 3
print(func('a', 'b'))  # ab
print((lambda x, y: x + y)(1, 2))  # 3
print((lambda x, y: x + y)('a', 'b'))  # ab

# lambda функции, в отличие от обычной, не требуется инструкция return
func = lambda *args: args
print(func(1, 2, 3, 4))