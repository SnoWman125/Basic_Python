# Реализуйте базовый класс Car:
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.


#return f'Speed auto = {self.speed}, color auto = {self.color}, name auto = {self.name} auto is police = {self.is_police}'
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина поехала!'
    def stop(self):
        return f'Машина остановилась!'
    def turn(self, direction):
        self.direction = direction
        return f'Машина повернула {direction}'
    def show_speed(self):
        return self.speed

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def show_speed(self):
        if self.speed > 60:
            return f'Скорость очень выская'
        else:
            return self.speed



class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def show_speed(self):
        if self.speed > 40:
            return f'Скорость очень выская'
        else:
            return self.speed

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

town = TownCar(70, 'green', 'Toyota', False)
sport = SportCar(120, 'red', 'Mazda', False)
work = WorkCar(50, 'black', 'Mersedes', False)
police = PoliceCar(100, 'Blue', 'Ford', True)


print(town.color)
print(sport.speed)
print(work.name)
print(police.is_police)
print(town.show_speed())
print(police.go())
print(police.turn('влево'))
print(sport.stop())
print(sport.turn('вправо'))

