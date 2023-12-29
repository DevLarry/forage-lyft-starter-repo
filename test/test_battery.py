import unittest
from datetime import datetime, date
from battery.battery import Battery
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def setUp(self):
        pass
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = NubbinBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_is_battery(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(isinstance(battery, Battery))

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = NubbinBattery(today, last_service_date)
        self.assertTrue(battery.current_date == today)


class TestSpindler(unittest.TestCase):
    def setUp(self):
        pass
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        battery = SpindlerBattery(today, last_service_date)
        self.assertFalse(battery.needs_service())

    def test_is_battery(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(isinstance(battery, Battery))

    def test_engine_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        battery = SpindlerBattery(today, last_service_date)
        self.assertTrue(battery.current_date == today)


if __name__ == '__main__':
    unittest.main()
