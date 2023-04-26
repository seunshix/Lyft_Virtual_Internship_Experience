import unittest
from tires.carrigan_tire import CarriganTires

class TestCarriganTires(unittest.TestCase):

    def test_needs_service_true(self):
        tire_wear = [0.8, 0.5, 0.6, 0.9]
        tires = CarriganTires(tire_wear=tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.8, 0.5, 0.6, 0.8]
        tires = CarriganTires(tire_wear=tire_wear)