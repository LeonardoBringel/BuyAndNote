from transaction_utils import *
from workbook_utils import *

try:
    worksheet = open_workbook()
except FileNotFoundError:
    create_workbook()
    worksheet = open_workbook()

for transaction in list_transactions(worksheet):
    print(transaction)
