# try:
#     pass
# except:
#     pass
# else:
#     pass
# finally:
#     pass

def calc(m):
    try:
        m = int(m)
    except Exception as e:
        print(e)  # invalid literal for int() with base 10: 'йцук'
    else:
        return 10 * m
    finally:
        print('Я буду выполняться в любом случе, с ошибкой или без')

# print(calc('йцук'))


# Вариант в зависимости от ошибки
def calm(m):
    try:
        m = int(m)
    except ValueError as e:
        print(e)  # invalid literal for int() with base 10: 'кук'
        m = 2
    except TypeError:
        pass
    except FileNotFoundError:
        pass
    return 10 * m

print(calm('кук'))
