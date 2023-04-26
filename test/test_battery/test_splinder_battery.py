import unittest
from datetime import date
from battery.battery_type.splinder_battery import SplinderBattery

class TestSplinderBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = date(2019, 4, 26)  # 2 years ago from current date
        battery = SplinderBattery(last_service_date=last_service_date, current_date=date.today())
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = date.today()  # current date, battery should not need service
        battery = SplinderBattery(last_service_date=last_service_date, current_date=date.today())
        self.assertFalse(battery.needs_service())