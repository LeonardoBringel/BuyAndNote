from datetime import datetime


class Transaction:
    def __init__(self, date, category, order, ticker, quantity, price):
        temp_date = datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S')

        self.date = temp_date.strftime('%d/%m/%y')
        self.category = category
        self.order = order
        self.ticker = ticker
        self.quantity = quantity
        self.price = round(float(price), 2)

    def __str__(self):
        return f'{self.date}\t{self.category}\t{self.order}\t' + \
            f'{self.ticker}\t{self.quantity}\t{self.price}'
