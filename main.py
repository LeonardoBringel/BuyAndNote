from transaction_utils import *
from workbook_utils import *

try:
    workbook, worksheet = open_workbook()
except FileNotFoundError:
    create_workbook()
    workbook, worksheet = open_workbook()

if input('Add transaction? <y/n> ').upper() == 'Y':
    add_transaction(worksheet)

for transaction in list_transactions(worksheet):
    print(transaction)

save_workbook(workbook)
