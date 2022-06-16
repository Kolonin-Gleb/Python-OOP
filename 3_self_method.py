# Методы классов. Параметр self
'''
class Point:
    color = 'red'
    circle = 2

    # Методы
    def set_coordinates(self, x, y):
        # Благодаря ссылке на вызывающий объект self - с ним можно взаимодействовать
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)

    def info(self):
        print(f"color = {self.color} circle = {self.circle}")

# Когда мы вызываем методы класса через его объекты, 
# то интерпретатор Python автоматически добавляет первым аргументом ссылку на объект,
# из которого этот метод вызывается. Поэтому необходимо указывать параметр self

a = Point()
a.info()

a.set_coordinates(0, 0)
print(a.__dict__)
'''

# step 5
'''
class MediaPlayer:
    def open(self, file):
        self.filename = file
    def play(self):
        print(f"Воспроизведение {self.filename}")


media1 = MediaPlayer()
media2 = MediaPlayer()
media1.open("filemedia1")
media2.open("filemedia2")

media1.play()
media2.play()
'''

# step 6
'''
class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data
    def draw(self):
        print(*[num for num in self.data if num >=Graph.LIMIT_Y[0] and num <= Graph.LIMIT_Y[1]])


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()
'''

'''
class Stepik:
    def next_task(self):
        return "Следующее задание"

my_st = Stepik()

print(Stepik.next_task(my_st))
'''

#  step 8
'''
import sys

class StreamData:
    def create(self, fields, lst_values):
        # Ключей столько же, сколько и значений
        if len(fields) == len(lst_values):
            self.__dict__ = dict(zip(fields, lst_values))
            return True
        else:
            return False

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res # Возращаю объект и результат работы

sr = StreamReader()
data, result = sr.readlines()
print(data.__dict__, result, sep='\n')
'''

# step 10
'''
import sys # Для работы с потоками ввода/вывода

class DataBase:
    lst_data = [] # Список словарей
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):
        for line in data:
            dict_line = dict(zip(self.FIELDS, line.split()))
            self.lst_data.append(dict_line)

    def select(self, a, b):
        if b >= len(self.lst_data):
            b = len(self.lst_data)
        return self.lst_data[a:b+1]

lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока

# print(lst_in)
db = DataBase()
db.insert(lst_in)

# for test only
'''

# Translator
'''
class Translator:
    # Данные следует хранить в формате словаря
    transl = {}

    # По хорошему не нужно добавлять перевод слова, если он уже присутствует-)
    def add(self, eng, rus):
        self.transl[eng] = self.transl.get(eng, []) + [rus]
        # self.transl.setdefault(eng, [])
        # self.transl[eng].append(rus)

    def remove(self, eng):
        del self.transl[eng]

    def translate(self, eng):
        return self.transl[eng] # Не защищён от обращения по несуществующему слову.



tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

tr.remove('car')

print(*tr.translate('go'), end=' ')
'''

# 
''''''
