from pyxll import xl_func, xl_return, Formatter, DataFrameFormatter
from xltable import *
from win32com.client import constants

from helpers import *
from DFFormatter import *
df_formatter = ret_DFFormatter()

# For all methods:
# set debug=dbg for debugging

'''

Pandas Helpers

'''
@xl_func(volatile=True)
def pandas_is_installed():
    """returns True if pandas is installed"""
    try:
        import pandas
        return True
    except ImportError:
        return False


@xl_func("dataframe<index=True>, float[], str[], str[]: dataframe<index=True>",
auto_resize=True,
formatter=df_formatter)   
def describe_dataframe(df, percentiles=[], include=[], exclude=[]):
	"""
	Generates descriptive statistics that summarize the central tendency,
	˓→dispersion and shape of a dataset's
	distribution, excluding NaN values.
	:param df: DataFrame to describe.
	:param percentiles: The percentiles to include in the output. All should fall
	˓→between 0 and 1.
	:param include: dtypes to include.
	:param exclude: dtypes to exclude.
	:return:
	"""
	# filter out any blanks
	percentiles = list(filter(None, percentiles))
	include = list(filter(None, include))
	exclude = list(filter(None, exclude))
	return df.describe(percentiles=percentiles or None,
	include=include or None,
	exclude=exclude or None) 

def df_title(df,name):
	return df.set_axis([name, *df.columns[1:]], axis=1)	


'''

Pandas Operations

'''

'''
Creates a DataFrame with excell cells for input
Can also include index and col names
'''
@xl_func("dataframe<index=None,columns=None>,str,str,str,str[],str[]:dataframe<index=True,columns=True>",
	formatter=df_formatter,
	auto_resize=True)
def DF(df,title,proc_name='_DF',debug='dbg',index=[],cols=[],):
	title+=proc_name
	if debug=='dbg':
		Mbox('DF Creation: Input', df.to_string(index=False), 0)
		io_str='Input\n'+df.to_string(index = True)
		# Mbox('DF Creation Debug', io_str, 0)
		# Mbox('DF Creation',df.values.tolist(),0)
	if len(index)==0:
		indices=[x for x in range(len(df))]
		io_str=' '.join([str(x) for x in indices])
		df[title]=indices
		df.set_index(title,inplace=True)
	if title!='b_DF':
		columns = [chr(ord('A') + x) for x in range(len(df.columns.tolist()))]
		df.columns=columns
	else:
		if title=='b_DF':
			df.columns=['b']
	out_df=pd.DataFrame(df.values.tolist(),index=df.index,columns=columns)
	# out_df.style.set_properties(**{'text-align': 'center'})
	print(out_df.to_string())
	return df

"""
Creates a DataFrame of random numbers.
params :
	> rows: Number of rows to create the DataFrame with.
	> columns: Number of columns to create the DataFrame with.
"""
@xl_func("int, int: dataframe<index=True>",
auto_resize=True,
formatter=df_formatter)
def random_df(rows, columns):

	data = np.random.rand(rows, columns)
	column_names = [chr(ord('A') + x) for x in range(columns)]
	df = pa.DataFrame(data, columns=column_names)
	return df



print(' > Pandas \n    Module Success')