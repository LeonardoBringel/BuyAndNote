from transaction_utils import *
from workbook_utils import *

try:
    workbook, worksheet = open_workbook()
except FileNotFoundError:
    create_workbook()
    workbook, worksheet = open_workbook()

while True:
    print('------------- MENU -------------')
    answer = input('[1] - Inserir\t\t[2] - Visualizar\n[0] - Sair\tOpção: ')
    match answer:
        case '1':
            add_transaction(worksheet)
            save_workbook(workbook)
        case '2':
            print('\n\n-- Transações --')
            for transaction in list_transactions(worksheet):
                print(transaction)
        case '0':
            exit()
    print('\n\n\n')
