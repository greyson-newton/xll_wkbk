# https://pypi.org/project/xltable/
from xltable import *
# https://pypi.org/project/xltable/
import pandas as pa
# https://stackoverflow.com/questions/27957373/python-import-and-initialize-argparse-after-if-name-main
# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
import argparse
def start_ntbk(args):
	workbook = Workbook(args.name+'.xlsxm')

	# sheet = Worksheett("Sheet1")
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
def main(args):
	# workbook = Workbook("example.xlsx")
	if args.name.count('.')>1:
		print('del ext. in your notebook name')
	else:
		start_ntbk()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'setup pyxll notebook')
    parser.add_argument('-n', help='Enter name of the xl notebook, include specific filename prefix if want to specifiy output folder')
    parser.add_argument('-q', help='Enter name of the xl notebook')
    args = parser.parse_args()

    main(args.name)