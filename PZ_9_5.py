class Stationary:
    def drow(self):
        print("Запуск отрисовки")

class Pen(Stationary):
    def drow(self):
        print("Рисуем ручкой!")

class Pencil(Stationary):
    def drow(self):
        print("Рисуем карандашом!!")

class Handle(Stationary):
    def drow(self):
        print("Рисуем маркером!!!")

start = Stationary()
start.drow()

pen = Pen()
pen.drow()

pencil = Pencil()
pencil.drow()

handle = Handle()
handle.drow()