from datetime import date, datetime
from battery.battery import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        current_year = self.current_date.year
        service_year = self.last_service_date.year
        current_month = self.current_date.month
        service_month = self.last_service_date.month
        if current_year - service_year > 4:
            return True
        if current_year - service_year == 4:
            if current_month >= service_month:
                if self.current_date.day >= self.last_service_date.day:
                    return True
        return False
