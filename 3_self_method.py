# Методы классов. Параметр self

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

