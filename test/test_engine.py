import unittest
from datetime import datetime, date
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.engine import Engine


class TestCapuletEngine(unittest.TestCase):
    def setUp(self):
        pass
    def test_engine_should_be_serviced(self):
        # today = datetime.today().date()
        # last_service_date = today.replace(year=today.year - 3)
        current_mileage = 400667
        last_service_mileage = 65
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        # today = datetime.today().date()
        # last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 200

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_engine_is_type_of_engine(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(isinstance(engine, Engine))

    def test_engine_parameter_set(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = CapuletEngine(current_mileage, last_service_mileage)
        
        self.assertTrue(engine.last_service_mileage == last_service_mileage)


class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        engine = SternmanEngine(True)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = SternmanEngine(False)
        self.assertFalse(engine.needs_service())

    def test_engine_is_type_of_engine(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = SternmanEngine(True)
        self.assertTrue(isinstance(engine, Engine))

    def test_engine_parameter_set(self):
        engine = SternmanEngine(True)  
        self.assertTrue(engine.warning_light_is_on is True)


class TestWilloughby(unittest.TestCase):
    def setUp(self):
        pass
    def test_engine_should_be_serviced(self):
        # today = datetime.today().date()
        # last_service_date = today.replace(year=today.year - 3)
        current_mileage = 75066
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        # today = datetime.today().date()
        # last_service_date = today.replace(year=today.year - 1)
        current_mileage = 0
        last_service_mileage = 200

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_engine_is_type_of_engine(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(isinstance(engine, Engine))

    def test_engine_parameter_set(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        
        self.assertTrue(engine.last_service_mileage == last_service_mileage)


if __name__ == '__main__':
    unittest.main()
