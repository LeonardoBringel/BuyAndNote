from transaction import *
from datetime import datetime


def list_worksheet_rows(worksheet):
    rows = []
    for row in list(worksheet.rows)[1:]:
        rows.append([cell.value for cell in row])
    return rows


def list_transactions(worksheet):
    transactions = []

    for row in list_worksheet_rows(worksheet):
        date, category, order, ticker, quantity, price, total_price = row

        temp_date = datetime.strptime(str(date), '%Y-%m-%d %H:%M:%S')
        date = temp_date.strftime('%d/%m/%y')

        transaction = Transaction(date, category, order, ticker, quantity, price, total_price)
        transactions.append(transaction)
    return transactions


def add_transaction(worksheet, data):
    temp_date = datetime.strptime(str(data[0]), '%d/%m/%Y')
    data[0] = temp_date.strftime('%Y-%m-%d %H:%M:%S')

    worksheet.append(data)
