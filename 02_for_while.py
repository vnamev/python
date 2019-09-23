# while
i = 5
while i < 15:
    print(i)  # 5 7 9 11 13
    i = i + 2

# for
for i in 'hello world':
    print(i * 2, end=' ')  # hh ee ll ll oo   ww oo rr ll dd

# continue
for i in 'hello world':
    if i == 'o':
        continue
    print(i * 2, end=',')  # hh,ee,ll,ll,  ,ww,rr,ll,dd,

# break
for i in 'hello world':
    if i == 'o':
        break
    print(i * 2, end='')  # hheellll

# else in for with break
for i in 'hello world':
    if i == 'a':
        break
else:
    print('Буквы a в строке нет')  # Буквы a в строке нет