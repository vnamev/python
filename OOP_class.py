class B: # <- имя класса должно быть словом существимтельным или комбинацией типа WikiPage / AddressParser, не глаголом  и не одной буквой!!!!
    arg = 'Python'

    def g(self): # <- имена методов должны быть глаголами и глагольными словосочетаниями get set is update и т.д.
        return self.arg

b = B() # <- экземпляр объекта (класса)
b.g()  # 'Python'

b.arg = 'span4Bob'
b.g()  # 'span4Bob' - изменили аргумент вместо 'Python'


# Создание объектов от класса
class figura:
    ''' Класс, описывающий любую фигуру '''

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


###############
# Пример создания структуры школы на ООП
#
"""
персона
    ученик
        дежурный
        староста
        
    учитель
        директор
        завуч
        классный руководитель
        
    технический персонал
        сторож
        дворник
        вахтер
        повар
        
    медицинский персонал
        медсестра
        психолог
        
класс
    начальный
    средний
    старший
    
тип класса
    с уклоном
    без уклона
    
помещение
    учебный
    административный
    технический
    
документация
    журнал
    расписание
    программа обучения
    
предмет
    гуманитарный
    точный
"""

class Persona:
    def __init__(self, _first_name, _middle_name, _last_name, _gender, _birthday, _contact_info):
        self.gender = _gender
        self.birthday = _birthday
        self.first_name = _first_name
        self.last_name = _last_name
        self.middle_name = _middle_name
        self.contact_info = _contact_info


    def get_fio(self):
        return self.first_name + ' ' + self.middle_name + ' ' + self.last_name

    def get_dopinfo(self):
        return self.gender + ' ' + self.birthday

    def get_contacts(self):
        return self.contact_info

school_student_1 = Persona("Vlad", "Максимович", "Нырков", 'm', '21.07.2014', None)
school_student_2 = Persona("Miron", "Максимович", "Нырков", 'm', '20.08.2017', "Тут типа адресс и телефон домашний")

# print(school_student_1.get_fio(), school_student_1.get_dopinfo())
# print(school_student_2.get_fio(), school_student_2.get_dopinfo(), school_student_2.get_contacts())

# Создаём / наследуем класс и все его методы от Person
class Student(Persona):
    def __init__(self, _first_name, _middle_name, _last_name, _gender, _birthday, _contact_info, _university_name, _faculty, _price, _address):
        super().__init__(_first_name, _middle_name, _last_name, _gender, _birthday, _contact_info)
        self.bal = 0
        self.university = University(_university_name, _faculty, _price, _address)  # используем экземпляр класса

    def update_bal(self, balCT):
        self.bal = balCT

    # переопределение метода под наш класс
    def get_dopinfo(self):
        return self.gender + ' ' + self.birthday + ' ' + str(self.bal)

# Экземпляр класса
class University:
    def __init__(self, _university_name, _faculty, _price, _address):
        self.university_name = _university_name
        self.faculty = _faculty
        self.price = _price
        self.address = _address

    def update_university_name(self, university_name):
        self.university_name = university_name

    def get_university_name(self):
        return 'Поступил в ' + self.university_name

    def get_university_info(self):
        return 'Инфа об универе: ' + self.university_name + ' ' + self.faculty + ' ' + self.address


student_1 = Student('Max', 'M', 'N', 'm', '12.12.12', '+375445340362', 'MGUP', 'MAPP', '800', 'Mogilev ... Shmidta')
student_2 = Student('Vasis', 'S', 'T', 'women', '10.12.10', '+375445340362', 'MGU', 'SAPR', '1800', 'London Good Buy!')

print(student_1.get_fio(), student_1.get_dopinfo())
print(student_1.university.get_university_info())
print(student_2.university.get_university_info())
