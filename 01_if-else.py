# 1
num = 2000
if num > 100:
    if num == 150:
        print('Равно 150')
    else:
        print('Больше 150 явно!')
elif num < 100:
    print('меньше 100')
else:
    print('равно 100')


# 2 Результат от ввода
# a = int(input())
a = 5
if a < -5:
    print('Меньше')
elif -5 <= a <= 5:
    print('Между -5 и 5 или равно')
else:
    print('Больше')

# 3 if в цикле for... применение else в совокупности с break - прерывает цикл
for i in 'hello world':
    if i == 'a':
        break
else:
    print('Буквы в строке нет')

# 3.1
for i in 'hello world':
    if i == 'o':
        break
    print(i * 2, end='')
# hheellll
