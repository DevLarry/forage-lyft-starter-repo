from datetime import datetime
from car import Car

from battery.battery import Battery
from engine.engine import Engine

class Calliope(Car):
    def __init__(self, engine: Engine, battery: Battery):
        super().__init__(engine, battery)

