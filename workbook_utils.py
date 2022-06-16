from openpyxl import load_workbook, Workbook


def open_workbook():
    workbook = load_workbook('carteira.xlsx')
    return workbook, workbook.active


def create_workbook():
    workbook = Workbook()
    workbook.active.title = 'Transações'
    workbook.active.append(['Data', 'Categoria', 'Ordem', 'Ticker', 'Quantidade', 'Preço (R$)'])
    workbook.save('carteira.xlsx')


def save_workbook(workbook):
    workbook.save('carteira.xlsx')
