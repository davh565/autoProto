from openpyxl import load_workbook
from openpyxl import utils

file = "IO_INSTRUMENT_LIST.xlsx"
sheet = "DEFAULTS"


def main(fileName, sheetName):
    data = loadData(fileName, sheetName)
    createDBF(data)


def loadData(fileName, sheetName):

    wb = load_workbook(filename=file, read_only=False,
                       keep_vba=False, data_only=True, keep_links=False)
    ws = wb[sheetName]

    data = {
        "file": fileName,
        "sheet": sheetName,
        "prototypes": [],
        "fields": [],
    }
    for index in range(ws.max_row):
        cell = ws["A"+str(index+1)]
        if cell.value != None:
            data["fields"].append(cell.value)
            # print()
    for index in range(ws.max_column):
        cell = ws[utils.get_column_letter(index+1)+"2"]
        if cell.value != None:
            data["prototypes"].append(cell.value)

        # print()
        # print(index)

    return data


def createDBF(data):
    print(data)
    # print(data["prototypes"])


main(file, sheet)

# def get_all_tables(filename):
#     """ Get all tables from a given workbook. Returns a dictionary of tables.
#         Requires a filename, which includes the file path and filename. """

#     # Load the workbook, from the filename
#     wb = load_workbook(filename=file, read_only=False,
#                        keep_vba=False, data_only=True, keep_links=False)

#     # Initialize the dictionary of tables
#     tables_dict = {}

#     # Go through each worksheet in the workbook
#     for ws_name in wb.sheetnames:
#         print("")
#         print(f"worksheet name: {ws_name}")
#         ws = wb[ws_name]
#         # print(f"tables in worksheet: {len(ws._tables)}")

#         # Get each table in the worksheet
#         for tbl in ws._tables:
#             print(f"table name: {tbl.name}")
#             # First, add some info about the table to the dictionary
#             tables_dict[tbl.name] = {
#                 'table_name': tbl.name,
#                 'worksheet': ws_name,
#                 'num_cols': len(tbl.tableColumns),
#                 'table_range': tbl.ref}

#             # Grab the 'data' from the table
#             data = ws[tbl.ref]

#             # Now convert the table 'data' to a Pandas DataFrame
#             # First get a list of all rows, including the first header row
#             rows_list = []

#             for row in data:
#                 # Get a list of all columns in each row
#                 cols = []
#                 for col in row:
#                     cols.append(col.value)
#                 rows_list.append(cols)

#             # Create a pandas dataframe from the rows_list.
#             # The first row is the column names
#             df = data

#             # Add the dataframe to the dictionary of tables
#             tables_dict[tbl.name]['dataframe'] = df

#     return tables_dict


# File location:
# Run the function to return a dictionary of all tables in the Excel workbook
