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


def add_transaction(worksheet):
    date = input('Data: ')
    category = input('Categoria: ').lower()
    order = input('Ordem: ').lower()
    ticker = input('Ticker: ').upper()
    quantity = int(input('Quantidade: '))
    price = float(input('Preço R$: '))

    total_price = round(quantity * price, 2)

    temp_date = datetime.strptime(str(date), '%d/%m/%Y')
    date = temp_date.strftime('%Y-%m-%d %H:%M:%S')

    worksheet.append([date, category, order, ticker, quantity, price, total_price])
