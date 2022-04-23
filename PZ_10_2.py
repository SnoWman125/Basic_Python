# Реализовать проект расчёта суммарного расхода ткани на производство одежды.

from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return self.result + other.result

    @abstractmethod
    def result(self):
        pass


class Coat(Clothes):
    @property
    def result(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):
    @property
    def result(self):
        return round(2 * self.param) + 0.3


coat = Coat(65)
print(coat.result)
print('===' * 10)
costume = Costume(20)
print(costume.result)
print('===' * 10)
print(coat + costume)
