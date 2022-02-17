import ctypes  # An included library with Python install.
from pyxll import xl_func, xl_return, Formatter, DataFrameFormatter
from xltable import *
from win32com.client import constants

from DFFormatter import *
df_formatter = ret_DFFormatter()

# Pops-Up a Dialogue Box
def Mbox(title, text, style):
	##  Styles:
	##  0 : OK
	##  1 : OK | Cancel
	##  2 : Abort | Retry | Ignore
	##  3 : Yes | No | Cancel
	##  4 : Yes | No
	##  5 : Retry | Cancel 
	##  6 : Cancel | Try Again | Continue

    return ctypes.windll.user32.MessageBoxW(0, text, title, style)



print(' > helpers \n    Module Success')