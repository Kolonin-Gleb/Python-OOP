# Классы и объекты. Атрибуты классов и объектов
'''
class Point:
    # Аттрибуты / свойства класса:
    color = 'red'
    circle = 2

# Просмотр всех аттрибутов класса (мои + встроенные)
print(Point.__dict__)
a = Point()
b = Point()

print(a.circle)

Point.circle = 1 # Меняя значение аттрибута класса оно изменится во всех объектах.
# Т.к. я создал объекты a и b без аттрибутов, но через них можно обращаться к аттрибутам класса
print(a.circle)

print(a.__dict__) # У самого объекта нет аттрибутов

a.color = 'green' # Добавление собственного аттрибута объекту

print(a.__dict__)

# В класс также можно добавить новый аттрибут (2 способа)
Point.type_pt = 'disc'
setattr(Point, 'prop', 1) # Если аттрибут prop уже существует, то его значение будет изменено

print(Point.__dict__)

# Получение значений аттрибутов

# Point.a - т.к. аттрибута a нет, вернёт ошибку
print(getattr(Point, 'a', False)) # Если аттрибута нет, то вернёт False

# Проверка на наличие аттрибута
print(hasattr(Point, 'prop'))

# Удаление аттрибута класса
del Point.prop
# delattr(Point, 'prop')

# Удаление аттрибута объекта
print(a.color)
del a.color
# После удаления аттрибута в объекте он будет ссылаться на значение, что лежит в классе
print(a.color)

# У объектов могут быть аттрибуты, которых нет у их класса!
a.x = 1
a.y = 2
b.x = 10
b.y = 20
'''
# Решение задач из курса step 6:
'''
class Car:
    pass

setattr(Car, "model", "Тойота")
setattr(Car, "color", "Розовый")
setattr(Car, "number","П111УУ77")

print(Car.__dict__["color"])
'''

# step 7
'''
class Notes:
    uid = 1005435
    title = "Шутка"
    author = "И.С. Бах"
    pages = 2

print(getattr(Notes, 'author'))
'''

# step 9
'''
class Figure:
    type_fig = 'ellipse'
    color = 'red'

fig1 = Figure()
fig1.start_pt = (10, 5)
fig1.end_pt = (100, 20)
fig1.color = 'blue'
del fig1.color

print(*fig1.__dict__)
'''

# step 10
'''
class Person:
    name = 'Сергей Балакирев'
    job = 'Программист'
    city = 'Москва'

p1 = Person()
print('job' in p1.__dict__)
'''

'''
class Point:
    tp = 1

print(Point.__dict__)
'''

