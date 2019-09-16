class B:
    arg = 'Python'

    def g(self):
        return self.arg

b = B() # <- экземпляр объекта
b.g()  # 'Python'

b.arg = 'span4Bob'
b.g()  # 'span4Bob' - изменили аргумент вместо 'Python'


# Создание объектов от класса
class figura:
    '''Класс, описывающий любую фигуру'''

    type_figura = None
    color_figura = None
    strong_figura = None
    coordinates_figura = None

    # Магический метод возвращает строку
    def __str__(self):
        return str((self.type_figura, self.color_figura, self.strong_figura, self.coordinates_figura))

# Создаём объект "пешка"
figura_peshka = figura()
figura_peshka.type_figura = 'peshka'
figura_peshka.color_figura = 'white'
figura_peshka.strong_figura = 'пушечное мясо'
figura_peshka.coordinates_figura = (2, 2)

about_figura = "О фигуре: " + str(figura_peshka)  # О фигуре: (None, None, None, None)

print(about_figura)
