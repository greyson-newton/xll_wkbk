from pyxll import xl_func, xl_return, Formatter, DataFrameFormatter
from xltable import *
from win32com.client import constants

from helpers import *
from DFFormatter import *
df_formatter = ret_DFFormatter()
# To implement:
'''
def solve(M, b):
def CROSS(DF_M,DF_M):
def TPOSE(DF_M):
'''

'''

LA Helpers

'''

def zeros( s , zero=0):
    """
    return a matrix of size `size`
    :param size: a tuple containing dimensions of the matrix
    :param zero: the value to use to fill the matrix (by default it's zero )
    """
    return [zeros(s[1:] ) for i in range(s[0] ) ] if not len(s) else zero  

'''

Elementary LA Operations:

'''
@xl_func("dataframe<index=True,columns=True>,dataframe<index=True,columns=True>,str,str:dataframe<index=True,columns=True>",
	formatter=df_formatter,
	auto_resize=True)	
def dot(m1,m2,title,proc_name='DOT'):

	dot_result=m1.dot(m2)

	indices = [str(x+1) for x in range(len(dot_result))]
	dot_result.index=indices
	dot_result.index.names=['SOE_sol']

	Mbox('DOT', 'Results:\n'+dot_result.to_string(index=True), 0)

	columns=[title]
	dot_result.columns=columns		
	
	return dot_result


'''

Advanced LA Operations:

'''


@xl_func("dataframe<index=True,columns=True>,float[],str,str:dataframe<index=True,columns=True>",
	formatter=df_formatter,
	auto_resize=True)	
def SOE(M,b,title,proc_name='SOE_'):

	indices = ['e_'+str(x+1) for x in range(len(M))]
	M.index=indices
	M.index.names=[proc_name+title]
	columns=['M_'+str(x) for x in range(len(M.columns.tolist()))]
	M.columns=columns
	M['b']=b
	# out_df=pd.DataFrame(df.values.tolist(),index=df.index,columns=columns)
	# out_df.style.set_properties(**{'text-align': 'center'})
	return M	

@xl_func("dataframe<index=True,columns=True> : dataframe<index=True,columns=True>",
auto_resize=True,
formatter=df_formatter)
def gauss_jordan(M, eps = 1.0/(10**10)):
	a=M.values.tolist()
	print(a)
	n = len(a[0]) #defining the range through which loops will run
	#constructing the n X 2n augmented matrix
	P = [[0.0 for i in range(len(a))] for j in range(len(a))]
	for i in range(3):
		for j in range(n):
			P[j][j] = 1.0
	for i in range(len(a)):
		a[i].extend(P[i])
	#main loop for gaussian elimination begins here
	for k in range(n):
		if abs(a[k][k]) < 1.0e-12:
			for i in range(k+1, n):
				if abs(a[i][k]) > abs(a[k][k]):
					for j in range(k, 2*n):
						a[k][j], a[i][j] = a[i][j], a[k][j] #swapping of rows
					break
		pivot = a[k][k] #defining the pivot
		if pivot == 0: #checking if matrix is invertible
			print("This matrix is not invertible.")
			return
		else:
			for j in range(k, 2*n): #index of columns of the pivot row
				a[k][j] /= pivot
			for i in range(n): #index the subtracted rows
				if i == k or a[i][k] == 0: continue
				factor = a[i][k]
				for j in range(k, 2*n): #index the columns for subtraction
					a[i][j] -= factor * a[k][j]

	print('GJ_INV Success: ')					
	m_inv=list()
	for i in range(len(a)): #displaying the matrix
		row=list()
		for j in range(n, len(a[0])):
			row.append(a[i][j])
			print(a[i][j], end = " ")
		print()
		m_inv.append(row)
	out_df=pd.DataFrame(m_inv,M.columns,M.index)   
	out_df.index.names=['GJ_INV_'+M.index.names[0]]

	return out_df	 

@xl_func("dataframe<index=True,columns=True>,str,str : dataframe<index=True,columns=True>",
auto_resize=True,
formatter=df_formatter)
def inv(M,proc_name='INV_',debug='ndbg'):
  print(M.index.names)
  old_title=M.index.names[0]
  M.index.names =[proc_name+old_title]
  df_inv = pd.DataFrame(np.linalg.inv(M.values),M.columns,M.index)

  if debug=='dbg' or debug=='debug':
  	io_str='Input\n'+M.to_string(index = True)+'\n\nOutput\n'+df_inv.to_string(index = True)
  	Mbox('Matrix Inversion Debug', io_str, 0)
  	return df_inv 
  else:
  	return df_inv

print(' > LinAlg \n    Module Success')