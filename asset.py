class Asset:
    def __init__(self, transaction):
        self.ticker = transaction.ticker
        self.category = transaction.category
        self.quantity = transaction.quantity
        self.total_price = transaction.total_price

    def update(self, transaction):
        self.quantity += transaction.quantity
        self.total_price = round(self.total_price + transaction.total_price, 2)

    def get_average_price(self):
        return round(self.total_price / self.quantity, 2)

    def __str__(self):
        return f'{self.category}\t{self.ticker}\t{self.quantity}\t{self.total_price}\t{self.get_average_price()}'
