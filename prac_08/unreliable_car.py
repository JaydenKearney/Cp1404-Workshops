from prac_08.car import Car
from random import random

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        reliable_measure = random.randfloat(1, 100)
        if self.reliability > reliable_measure:
            super().drive(distance)
        else:
            return 0