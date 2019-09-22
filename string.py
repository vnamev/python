tripleString = """В такой "строке" мы можем 'использовать' все.""" # В такой "строке" мы можем 'использовать' все.

# 1 конкатенация
s1 = 'qwe'
s2 = 'rty'
print(s1 + s2)  # qwerty

# 2 дублирование строк
print(s1 * 3)  # qweqweqwe

# 3 длина строки
print(len(s2))  # 3

# 4 достпуп по индексу
str_span = 'spam'
print(str_span[0])  # s
print(str_span[-1])  # m

# 5 поиск в строке с начала
S = 'Hello'
print(S.find('l'))  # вернёт 2

# 5.1 поиск в строке с конца
print(S.rfind('l'))  # вернёт 3

# 6 метод replace
print('Hello'.replace('l', 'L'))  # вернёт 'HeLLo'
print('Abrakadabra'.replace('a', 'A', 2)) # цифра 2 указывает на первые 2 совпадения и ее замены, вернёт 'AbrAkAdabra

# 7 метод .split() Разбиение строки по разделителю (пустой или по запятой или еще какому)
print('Maxon4eg from Mogilev Minsk'.split(" "))  # ['Maxon4eg', 'from', 'Mogilev']
print("apple#banana#cherry#orange".split("#"))  # ['apple', 'banana', 'cherry', 'orange']

# Форматирование строк %
apple = 'Яблоко'
another_string = "Я люблю %s и %s" % ("Python", apple)
print(another_string)  # Я люблю Python и Яблоко

my_string = "%i + %i = %i" % (1, 2, 3)
print(my_string)  # '1 + 2 = 3'

float_string = "%f" % (1.23)
print(float_string)  # '1.230000'

float_string2 = "%.2f" % (1.23)
print(float_string2)  # '1.23'

# Принимает неправильные типы и выдаёт ошибку
# int_float_err = "%i + %f" % ("1", "2.00") # WARNING!!! ожидает i + f (число целое и дробное), а принимает строку

# Форматирование строк method .format
'Hello, {} !'.format('Vasya')
'Hello, Vasya!'

'{0} , {1} , {2} '.format('a', 'b', 'c')
'a, b, c'

'{0} {1} {0} '.format('abra', 'cad')
'abracadabra'

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
'Coordinates: {latitude} , {longitude} '.format(**coord)
'Coordinates: 37.24N, -115.81W'

coord = (3, 5)
'X: {0[0]} ; Y: {0[1]} '.format(coord)
'X: 3; Y: 5'

# Форматирование строк method f'' - работают быстрее % и .format()
name = "MAX"
age = 30
print(f"Hello, {name}. You are {age}.")  # Hello, MAX. You are 30.

print(f"{2 * 30}")  # Вывод: 60
print(f"{2 + 30}")  # Вывод: 32
print(f"{'2' + '60'}")  # Вывод: 260

# Многострочный формат строк f''
name = "Max ON"
profession = "Fullstack  Dev"
affiliation = "Monty Python"

message = (
    f"Hi {name}. "
    f"You are a {profession}. "
    f"You were in {affiliation}."
)

print(message) # Hi Max ON. You are a Fullstack  Dev. You were in Monty Python.
