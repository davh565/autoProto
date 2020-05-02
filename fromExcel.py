from openpyxl import load_workbook
from openpyxl import utils
import dbf

file = 'IO_INSTRUMENT_LIST.xlsx'
sheet = 'DEFAULTS'
divider = '____________________________________________________________________'


def main(fileName, sheetName):
    data = getData(fileName, sheetName)
    createDBF(data)


def getData(fileName, sheetName):
    print(divider)
    print('Getting data from sheet')

    wb = load_workbook(filename=file, read_only=False,
                       keep_vba=False, data_only=True, keep_links=False)
    ws = wb[sheetName]

    data = {
        'file': fileName,
        'sheet': sheetName,
        'protoNames': [],
        'fieldNames': [],
        'entries': [],
        'variables': []

    }

    def getFieldNames():
        for rowIndex in range(3, 12):
            cell = ws['A'+str(rowIndex)]
            if cell.value != None:
                data['fieldNames'].append(cell.value)
        print('Got FieldNames')

    def getProtoNames():
        for colIndex in range(2, 12):
            cell = ws[utils.get_column_letter(colIndex)+'2']
            if cell.value != None:
                data['protoNames'].append(cell.value)
        print('Got ProtoNames')

    def getEntries():
        for colIndex in range(2, 12):
            rows = []
            for rowIndex in range(3, 12):
                cell = ws[utils.get_column_letter(colIndex)+str(rowIndex)]
                rows.append(cell.value)
            data['entries'].append(tuple(rows))
        data['entries'] = tuple(data['entries'])
        print('Got Entries')

    def getVariables():
        for colIndex in range(2, 12):
            rows = []
            for rowIndex in range(3, 12):
                cell = ws[utils.get_column_letter(colIndex)+str(rowIndex)]
                if iterable(cell.value):
                    if '##' in cell.value:
                        rows.append(str(cell.value))
                    else:
                        rows.append(None)
                else:
                    rows.append(None)
            data['variables'].append(rows)
        print('Got Variables')

    getFieldNames()
    getProtoNames()
    getEntries()
    getVariables()
    print('')
    print('Got All Data')
    print(divider)
    return data


def createDBF(data):
    print(divider)
    print('Generating * .dbfs')
    print('')

    for protoName in data['protoNames']:
        protoIndex = data['protoNames'].index(protoName)
        fieldsStr = ''
        for fieldName in data['fieldNames']:
            fieldIndex = data['fieldNames'].index(fieldName)
            if data['entries'][protoIndex][fieldIndex] != None:
                fieldsStr += fieldName + ' C(16); '

        if fieldsStr != '':
            print(protoName+'.dbf')
            dbfTable = dbf.Table(filename=protoName +
                                 '.dbf', field_specs=fieldsStr,)
            dbfTable.open(mode=dbf.READ_WRITE)
            entries = tuple([str(e) for e in data['entries']
                             [protoIndex] if e != None])
            # print(entries)
            dbfTable.append(entries)
            # print(test)
            # for datum in (
            #     ('John Doe', 31, dbf.Date(1979, 9, 13)),
            #     ('Ethan Furman', 102, dbf.Date(1909, 4, 1)),
            #     ('Jane Smith', 57, dbf.Date(1954, 7, 2)),
            #     ('John Adams', 44, dbf.Date(1967, 1, 9)),
            # ):
            #     dbfTable.append(datum)

            # for datum in data['entries']:
    print('')
    print('DBFs generated')
    print(divider)


def iterable(obj):
    try:
        iter(obj)
    except Exception:
        return False
    else:
        return True


main(file, sheet)
