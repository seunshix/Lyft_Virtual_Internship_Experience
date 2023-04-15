from battery import Battery
from datetime import datetime

class NubbinBattery(Battery):

    def __init__(self, last_service_date,current_date):
        self.last_service_date = last_service_date
        self.current_date = datetime.date.today()
    
    def needs_service(self):
        service_date = self.last_service_date.replace(year=self.last_service_date + 4)

        if service_date < self.current_date:
            return True
        else:
            return False