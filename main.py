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
    answer = input('[1] - Inserir\t\t[2] - Visualizar\n[3] - Importar\t\t[0] - Sair\nOpção: ')
    match answer:
        case '1':
            date = input('Data: ')
            category = input('Categoria: ').lower()
            order = input('Ordem: ').lower()
            ticker = input('Ticker: ').upper()
            quantity = int(input('Quantidade: '))
            price = float(input('Preço R$: '))
            total_price = round(quantity * price, 2)

            transaction = Transaction(date, category, order, ticker, quantity, price, total_price)

            add_transaction(worksheet, transaction.get_array())
            save_workbook(workbook)

        case '2':
            assets = {}
            print('\n\n-- Transações --')
            for transaction in list_transactions(worksheet):
                print(transaction)
                if transaction.ticker not in assets:
                    assets[transaction.ticker] = Asset(transaction)
                else:
                    assets.get(transaction.ticker).update(transaction)

            assets = list(assets.values())
            assets.sort(key=lambda value: (value.category, value.ticker))

            print('\n\n-- Posição --')
            for asset in assets:
                print(asset)

        case '3':
            _, temp_worksheet = open_workbook('negociacao.xlsx')

            for transaction in extract_transactions(temp_worksheet):
                add_transaction(worksheet, transaction.get_array())
            save_workbook(workbook)

        case '0':
            exit()
    print('\n\n\n')
