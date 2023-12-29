from datetime import datetime
from battery.spindler_battery import SpindlerBattery
from car import Car

from battery.battery import Battery
from engine.engine import Engine


class Palindrome(Car):
    def __init__(self, engine: Engine, battery: Battery):
        super().__init__(engine, battery)
