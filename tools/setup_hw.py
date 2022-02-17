from xltable import *
import pandas as pa

# workbook = Workbook("example.xlsx")
workbook = Workbook(args.nbk+'.xlsxm')

# sheet = Worksheet("Sheet1")
for question,dataframes in args.questions.items():
	# create the Workbook and Worksheet objects and add table to the sheet
	sheet = Worksheet(question)
	
	for name,table in dataframes:
	# create the named xlwriter Table instance
	table = Table(name, dataframe)
		sheet.add_table(table)


	workbook.add_sheet(sheet)

# write the workbook to the file (requires xlsxwriter)
workbook.to_xlsx()