import unittest
from datetime import date, datetime
from battery.battery_type.nubbin_battery import NubbinBattery

class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = date(2018, 4, 26) # 4 years ago from current date
        battery = NubbinBattery(last_service_date=last_service_date, current_date=date.today())
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = date.today()  # current date, battery should not need service
        battery = NubbinBattery(last_service_date=last_service_date, current_date=date.today())
        self.assertFalse(battery.needs_service())