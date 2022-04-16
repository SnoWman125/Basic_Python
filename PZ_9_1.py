from itertools import cycle
from time import sleep

class TrafficLight:
    __color = [['red', 7], ['yellow', 2], ['green', 4], ['yellow', 2]]

    def running(self):
        print(f'Traffic light is running...')
        for color, sec in cycle(self.__color):
            print(color, f' -  {sec} second')
            sleep(sec)

light = TrafficLight()
light.running()
