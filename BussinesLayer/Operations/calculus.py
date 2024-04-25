from ...DataLayer.Models.models import Work
import datetime
from datetime import datetime as time


class TimeOperation:
    def __init__(self):
        pass

    def calculate_total_hours(self, time1="10:00:00", time2="22:00:00"):
        format = "%H:%M:%S"
        t1 = time.strptime(time1, format)
        t2 = time.strptime(time2, format)
        delta = t2 - t1
        seconds = 0

        if delta.total_seconds() < 0:
            seconds = delta.seconds
        else:
            seconds = delta.total_seconds()

        return float(seconds / (60 * 60))



class WorkOperation:
    def __init__(self, workList):
        self._workList = workList

    def calculate_payment_per_day(self):
        payments = []
        time = TimeOperation()
        total_hours_temp = 0.0

        for work in self._workList:
            total_hours_temp = time.calculate_total_hours(f"{work.get_checkIn()}:00", f"{work.get_checkOut()}:00")
            day = datetime.date(int(work.get_date().split('-')[2]), int(work.get_date().split('-')[1]), int(work.get_date().split('-')[0])).strftime("%A").lower()
            payments.append({
                "date": f"{day}, {work.get_date()}",
                "place": work.get_place(),
                "total_hours": total_hours_temp,
                "total_payment": float(work.get_paymentPerHours() * total_hours_temp)
            })

        return payments

    def calculate_total_hours(self):
        timeOp = TimeOperation()
        total_hours = 0

        for work in self._workList:
            total_hours += timeOp.calculate_total_hours(f"{work.get_checkIn()}:00", f"{work.get_checkOut()}:00")

        return total_hours

    def calculate_total_payment(self):
        timeOp = TimeOperation()
        total_payment = 0

        for work in self._workList:
            total_payment += work.get_paymentPerHours() * (timeOp.calculate_total_hours(f"{work.get_checkIn()}:00", f"{work.get_checkOut()}:00"))

        return total_payment