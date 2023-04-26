import unittest
from engine.engine_type.willoughby_engine import WilloughbyEngine

class TestWilloughbyEngine(unittest.TestCase):

    def test_needs_service_true(self):
        current_mileage = 70000
        last_service_mileage = 10000
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 35000
        last_service_mileage = 20000
        engine = WilloughbyEngine(current_mileage=current_mileage, last_service_mileage=last_service_mileage)
        self.assertFalse(engine.needs_service())