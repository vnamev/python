"""
Декораторы — это, по сути, “обёртки”,
которые дают нам возможность изменить поведение функции, не изменяя её код.
"""

# Пример с 1 декоратором
def decorator_func(func):
    def wrapper():
        print("Код, который отработает до вызова ф-ции")
        func() #  print("Код, который сработает внутри ф-ции c decor_func()")
        print("Код, который отработает после func()")
        return decorator_func
    return wrapper

@decorator_func
def decor_func():
    print("Код, который сработает внутри ф-ции")

decor_func()
# Код, который отработает до вызова ф-ции
# Код, который сработает внутри ф-ции
# Код, который отработает после func()



# пример с двумя декораторами: сначала от последней к первому декоратору
def decor1(fn):
    def wrapper():
        return "Start 1 decor wrapper " + fn() + " 1 END" # а сюда в первую обертку передаём (2 decor wrapper {MAX HELLO} 2 )
    return wrapper

def decor2(fn):
    def wrapper():
        return "(2 decor wrapper " + fn() + " 2 )" # сюда передаём {MAX HELLO}
    return wrapper

@decor1
@decor2
def hello():
    return "{MAX HELLO}"

print(hello())  # Start 1 decor wrapper (2 decor wrapper {MAX HELLO} 2 ) 1 END
