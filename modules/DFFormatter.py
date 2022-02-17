from pyxll import xl_func, xl_return, Formatter, DataFrameFormatter
from xltable import *
from win32com.client import constants

def ret_DFFormatter():
    df_formatter = DataFrameFormatter(
        index=Formatter(bold=True, interior_color=Formatter.rgb(0xA9, 0xD0, 0x8E)),
        header=Formatter(bold=True, interior_color=Formatter.rgb(0xA9,0xD0,0x8E)),
        rows=[
            Formatter(interior_color=Formatter.rgb(0xE4, 0xF1, 0xDB)),
            Formatter(interior_color=Formatter.rgb(0xF4, 0xF9, 0xF1)),
        ],	
        )
    return df_formatter

class BorderFormatter(Formatter):

    def apply(self, cell, *args, **kwargs):
        # get the Excel.Range COM object from the XLCell
        xl_range = cell.to_range()

        # add a border to each edge
        for edge in (constants.xlEdgeLeft,
                     constants.xlEdgeRight,
                     constants.xlEdgeTop,
                     constants.xlEdgeBottom):
            border = xl_range.Borders[edge]
            border.LineStyle = constants.xlContinuous
            border.ColorIndex = 0
            border.TintAndShade = 0
            border.Weight = constants.xlThin

        # call the super class to apply any other styles
        super().apply(cell, *args, **kwargs)




print(' > DFFormatter \n    Module Success')