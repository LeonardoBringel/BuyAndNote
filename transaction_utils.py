from transaction import *


def list_transactions(worksheet):
    transactions = []
    for row in range(1, worksheet.max_row):
        row_data = []
        for col in range(0, worksheet.max_column):
            data = worksheet.cell(row+1, col+1).value
            row_data.append(data)
        date, category, order, ticker, quantity, price = row_data
        transaction = Transaction(date, category, order, ticker, quantity, price)
        transactions.append(transaction)
    return transactions
