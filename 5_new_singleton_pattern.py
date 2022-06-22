# Магический метод __new__
# __new__ вызывается перед созданием объекта класса

# В Python все классы неявно наследуются от класса obj.
# В нём уже определены магические классы, благодаря чему мы можем перегружать лишь те, что нам нужны не описывая все остальные.
'''

class Point:
    # cls - это ссылка на тек. класс
    def __new__(cls, *agrs, **kwargs):
        print("вызов __new__ для " + str(cls))
        return super().__new__(cls) # возврат адреса создаваемого объекта. Если его не сделать, то вёрнёт None = отказ в создании объетка

    def __init__(self, x, y):
        print("вызов __init__ для " + str(self))
        self.x = x
        self.y = y

# pt = Point(1, 2)
# print(pt)

# Учебный пример паттерна Singleton
# Используется для гарантирования, что будет лишь 1 объекта класса для работы с БД


class DataBase:
    __instance = None # Ссылка на экземпляр класса при его наличии

    def __new__(cls, *args, **kwargs): # cls - ссылка на класс для которого создаётся объект
        # *args, **kwargs - нужно указывать, т.к. при создании объекта аргументы передаются не только в init, но и в new
        if cls.__instance is None:
            cls.__instance = super().__new__(cls) # Идет обращение к базовому классу, из которого вызывается конструктор
        
        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def __del__(self):
        # При удалении соединения его можно будет сделать снова
        DataBase.__instance = None

    def connect(self):
        print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")
    
    def close(self):
        print("закрытие соединения с БД")
    
    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")



db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(id(db), id(db2))

db.connect()
db2.connect()
# Мы здесь действительно видим первый объект. 
# Но при повторном вызове DataBase() также был вызван магический метод __init__
# с новым набором аргументов и локальные свойства изменили свое значение.

# Решить это поможет метод __call__, что будет изучен позже

'''
# tasks

'''
class AbstractClass():
    __instance = "Ошибка: нельзя создавать объекты абстрактного класса"

    def __new__(cls, *args, **kwargs):
        return cls.__instance

obj = AbstractClass()
'''

class SingletonFive:
    __total_bojects = 0 # число экмепляров класса
    __last_obj = None # Ссылка на последний объект

    def __new__(cls, *args, **kwargs):
        if cls.__total_bojects < 5:
            cls.__last_obj = super().__new__(cls) # Сохранение ссылки на последний созданный объект
            cls.__total_bojects += 1
        # выдать ссылку на последний объект
        return cls.__last_obj

    def __init__(self, name):
        self.name = name

# Создание объектов класса
objs = [SingletonFive(str(n)) for n in range(10)] # 5 объектов должно быть создано. Ещё 5 должны ссылаться на тот, что с индексом 4

# For test
print(*objs, sep="\n")
