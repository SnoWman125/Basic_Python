class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def full_name(self):
        return f'{self.name} {self.surname}'

    def salary(self):
        return f'{self.position} salary is {sum(self._income.values())}'

result = Position('Ivan', 'Moroz', 'Chief', 1000, 50)
print(result.full_name())
print(result.salary())

