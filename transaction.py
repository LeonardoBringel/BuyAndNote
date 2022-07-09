class Transaction:
    def __init__(self, date, category, order, ticker, quantity, price, total_price):
        self.date = date
        self.category = category
        self.order = order
        self.ticker = ticker
        self.quantity = quantity
        self.price = round(float(price), 2)
        self.total_price = round(float(total_price), 2)

    def get_array(self):
        return [self.date, self.category, self.order, self.ticker, self.quantity, self.price, self.total_price]

    def __str__(self):
        return f'{self.date}\t{self.category}\t{self.order}\t' + \
            f'{self.ticker}\t{self.quantity}\t{self.price}\t{self.total_price}'
