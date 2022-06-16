from transaction_utils import *
from workbook_utils import *

try:
    workbook, worksheet = open_workbook()
except FileNotFoundError:
    create_workbook()
    workbook, worksheet = open_workbook()

for transaction in list_transactions(worksheet):
    print(transaction)
