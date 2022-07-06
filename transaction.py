class Transaction:
    def __init__(self, date, category, order, ticker, quantity, price):
        self.date = date
        self.category = category
        self.order = order
        self.ticker = ticker
        self.quantity = quantity
        self.price = round(float(price), 2)

    def __str__(self):
        return f'{self.date}\t{self.category}\t{self.order}\t' + \
            f'{self.ticker}\t{self.quantity}\t{self.price}'
