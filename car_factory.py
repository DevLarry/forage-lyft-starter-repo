from datetime import date
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from model.calliope import Calliope


class CarFactory:
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        return Calliope(engine, battery)
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        return Calliope(engine, battery)
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool):
        battery = SpindlerBattery(last_service_date, current_date)
        engine = SternmanEngine(last_service_date, warning_light_on)
        return Calliope(engine, battery)
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        battery = NubbinBattery(last_service_date, current_date)
        engine = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        return Calliope(engine, battery)
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        battery = NubbinBattery(last_service_date, current_date)
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        return Calliope(engine, battery)