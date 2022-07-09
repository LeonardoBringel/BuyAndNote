from transaction import *
from datetime import datetime


def list_transactions(worksheet):
    transactions = []
    for row in range(1, worksheet.max_row):
        row_data = []
        for col in range(0, worksheet.max_column):
            data = worksheet.cell(row+1, col+1).value
            row_data.append(data)
        date, category, order, ticker, quantity, price, total_price = row_data

        temp_date = datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S')
        date = temp_date.strftime('%d/%m/%y')

        transaction = Transaction(date, category, order, ticker, quantity, price, total_price)
        transactions.append(transaction)
    return transactions


def add_transaction(worksheet, data):
    temp_date = datetime.strptime(str(data[0]), '%d/%m/%Y')
    data[0] = temp_date.strftime('%Y-%m-%d %H:%M:%S')

    worksheet.append(data)
