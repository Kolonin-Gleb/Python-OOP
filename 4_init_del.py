# Инициализатор __init__ и Финализатор __del__
# Инициализатор = конструктор
# Финализатор = деструктор

# Предопределенные методы для классов называются Магическими и начинаются с __...__
'''
class Point:
    
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color

points = []

for i in range(1, 2000, 2):
    points.append(Point(i, i))

points[1].color = 'yellow'
'''

# step 5
'''
from random import randint, choice

class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = []
func = [Line, Rect, Ellipse]
# Формируем 217 объектов
for i in range(1, 218):
    coordinates = [randint(-100, 100) for _ in range(4)]
    obj = choice(func)
    if obj == Line:
        elements.append(obj(0, 0, 0, 0))
    else:
        elements.append(obj(*coordinates))

# print(elements[0].__dict__)
'''

# TriangleChecker
'''
def pos_num(num):
    if type(num) != int or num < 0:
        return False
    else:
        return True

class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(list(map(pos_num, self.__dict__.values()))):
            return 1
        # Ни 1 из сторон не может быть >= суммы оставшихся
        if self.a >= (self.b + self.c) or self.b >= (self.a + self.c) or self.c >= (self.a + self.b):
            return 2
        else:
            return 3

a, b, c = map(int, input().split())

tr = TriangleChecker(a, b, c)

print(tr.is_triangle())
'''

# Graph
'''
'''

class Graph:
    def __init__(self, data):
        self.data = data.copy() # Копируем данные, а не ссылаемся на них
        self.is_show = True
    
    def set_data(self, data):
        self.data = data

    def set_show(self, fl_show):
        self.is_show = fl_show

    def _get_str_data(self): # Служебный метод начинается с _
        return ' '.join(map(str, self.data))

    def show_table(self):
        if self.is_show == False: print("Отображение данных закрыто")
        else: 
            print(self._get_str_data()) # Вызов метода класса внутри метода

    def show_graph(self):
        if self.is_show == False: print("Отображение данных закрыто")
        else:
            print("Графическое отображение данных:")
            print(self._get_str_data())

    def show_bar(self):
        if self.is_show == False: print("Отображение данных закрыто")
        else:
            print("Столбчатая диаграмма:", end=' ')
            print(self._get_str_data())

data_graph = list(map(int, input().split())) # 8 11 10 -32 0 7 18

gr = Graph(data_graph)

gr.show_bar()
gr.set_show(fl_show=False)
gr.show_table()

# На экране должны отобразиться две соответствующие строки.

''''''

