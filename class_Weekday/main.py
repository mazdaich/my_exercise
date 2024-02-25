from enum import IntEnum
from datetime import date, timedelta

Weekday = IntEnum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], start=0)


class NextDate:
    def __init__(self, today, weekday, after_today=False):
        self.today = today
        self.day = today.weekday()
        self.weekday = weekday
        self.after_today = after_today
        self.count = 0
        if self.after_today:
            self.w = self.today
            while self.w.weekday() != self.weekday.value:
                self.w += timedelta(days=1)
                self.count += 1
        else:
            self.count += 1
            self.w = self.today + timedelta(days=1)
            while self.w.weekday() != self.weekday.value:
                self.w += timedelta(days=1)
                self.count += 1

    def days_until(self):
        return self.count

    def date(self):
        return self.today + timedelta(days=self.count)


if __name__ == '__main__':

    from datetime import date

    today = date(2023, 4, 17)  # понедельник
    next_friday = NextDate(today, Weekday.FRIDAY)  # следующая пятница

    print(next_friday.date())
    print(next_friday.days_until())
