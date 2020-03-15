import datetime as dt


class Calculator:

    def __init__(self, limit=int):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        stats = 0
        for day in self.records:
            if day.date == dt.date.today():
                stats = stats + day.amount
        return stats

    def get_week_stats(self):
        week_stat = 0
        time_range = dt.timedelta(days=7)
        str_week = dt.date.today() - time_range
        for day in self.records:
            if day.date >= str_week:
                week_stat = week_stat + day.amount
        return week_stat


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment

        if date == None:
            self.date = dt.datetime.now().date()

        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()



class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        if self.get_today_stats() <= self.limit:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit - self.get_today_stats()} кКал"
        else:
            return 'Хватит есть!'


class CashCalculator(Calculator):
    USD_RATE = 80.1
    EURO_RATE = 70.1
    money = {'rub': "руб", 'usd': 'USD', 'eur': 'Euro'}

    def get_today_cash_remained(self, currency):
        rate = ''
        if currency == 'eur':
            rate = self.EURO_RATE
        elif currency == 'usd':
            rate = self.USD_RATE
        else:
            rate = 1

        if (self.get_today_stats() - self.limit) == 0:
            return 'Денег нет, держись'
        elif self.get_today_stats() <= self.limit:
            return f'На сегодня осталось {round((self.limit - self.get_today_stats()) / rate, 2)} {self.money[currency]}'
        else:
            return f'Денег нет, держись: твой долг - {(round((self.limit - self.get_today_stats()) / rate, 2)) * -1} {self.money[currency]}'
