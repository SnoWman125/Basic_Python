class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    def get_mass(self, mass=25, thickness=5):
        self.mass = mass
        self.thickness = thickness
        a= f'{self._width} * {self._length} * {mass} * {thickness}'
        result = (self._width * self._length * mass * thickness) / 1000
        print(f'{a} == {result}')


result = Road(5000, 20)
result.get_mass()