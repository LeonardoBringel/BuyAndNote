from asset import *
from transaction_utils import *
from workbook_utils import *

try:
    workbook, worksheet = open_workbook('carteira.xlsx')
except FileNotFoundError:
    create_workbook()
    workbook, worksheet = open_workbook('carteira.xlsx')

while True:
    print('------------- MENU -------------')
    answer = input('[1] - Inserir\t\t[2] - Visualizar\n[0] - Sair\tOpção: ')
    match answer:
        case '1':
            add_transaction(worksheet)
            save_workbook(workbook)
        case '2':
            assets = {}
            print('\n\n-- Transações --')
            for transaction in list_transactions(worksheet):
                print(transaction)
                if transaction.ticker not in assets:
                    assets[transaction.ticker] = Asset(transaction)
                else:
                    assets.get(transaction.ticker).add_transaction(transaction)

            assets = list(assets.values())
            assets.sort(key=lambda value: (value.category, value.ticker))

            print('\n\n-- Posição --')
            for asset in assets:
                print(asset)
        case '0':
            exit()
    print('\n\n\n')
