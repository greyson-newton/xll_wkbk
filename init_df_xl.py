from xltable import *
import pandas as pa
# create a dataframe with three columns where the last is the sum of the first two
dataframe = pa.DataFrame({
"col_1": [1, 2, 3],
"col_2": [4, 5, 6],
"col_3": Cell("col_1") + Cell("col_2"),
}, columns=["col_1", "col_2", "col_3"])
# create the named xltable Table instance
table = Table("table", dataframe)
# create the Workbook and Worksheet objects and add table to the sheet
sheet = Worksheet("Sheet1")
sheet.add_table(table)
workbook = Workbook("example.xlsx")
workbook.add_sheet(sheet)
# write the workbook to the file (requires xlsxwriter)
workbook.to_xlsx()