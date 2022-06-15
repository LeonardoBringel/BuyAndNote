from openpyxl import load_workbook


def open_workbook():
    workbook = load_workbook('carteira.xlsx')
    return workbook.active


try:
    worksheet = open_workbook()
except FileNotFoundError:
    print('Workbook not found')
