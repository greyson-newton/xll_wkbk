from PyQt5.QtCore import Qt, QSize, QEvent , QObject, pyqtSignal
from PyQt5.QtWidgets import * 
import sys
import pandas as pd

# creating a class
# that inherits the QDialog class
class df_wiz(QDialog):
    # constructor

        # # creating a dialog button for ok and cancel
        # self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # self.add_container(self.buttonBox)

        # self.buttonBox.rejected.connect(self.reject)

    def __init__(self):
        super(QDialog, self).__init__()

        self.setWindowTitle("DF Wizard")
        
        # setting geometry to the window
        self.setGeometry(500, 100, 1000, 1000)
        self.mainLayout = QVBoxLayout()

        self.df_metadata_container = QGroupBox("Shape")
        
        self.df_finish_container = QGroupBox("Finish")

        self.create_metadata()
    def add_container(self,ctnr):  
        self.mainLayout.addWidget(ctnr)
        self.setLayout(self.mainLayout)
    def create_metadata(self):
        self.df_name_lne=QLineEdit()
        self.qt_rows,self.qt_cols=QSpinBox(),QSpinBox()
        self.df_metadata_btn=QPushButton('load in')
        self.df_metadata_btn.clicked.connect(self.get_metadata)
        layout = QGridLayout()
        layout.addWidget(QLabel("rows"),0,0)
        layout.addWidget( self.qt_rows,0,1)
        layout.addWidget(QLabel("cols"),0,2)
        layout.addWidget( self.qt_cols,0,3)
        layout.addWidget(QLabel("DF Name:"),1,0)
        layout.addWidget(self.df_name_lne,1,1)
        layout.addWidget(self.df_metadata_btn,1,2)
        self.df_metadata_container.setLayout(layout)
        self.add_container(self.df_metadata_container)
    def get_metadata(self):
        self.df_name=self.df_name_lne.text()
        self.rows,self.cols= int(self.qt_cols.text()),int(self.qt_rows.text())
        self.create_data()
    def create_data(self):
        self.df_data_container = QGroupBox(self.df_name+" Data")
        self.data_grid=QGridLayout()
        for r in range(self.rows):
            for c in range(self.cols):
                self.data_grid.addWidget(QLineEdit(),r,c)

        
        
        self.df_data_container.setLayout(self.data_grid)
        self.add_container(self.df_data_container)
        self.finalize_data()
        self.add_container(self.df_finish_container)

    def finalize_data(self):
        self.ok,self.cancel = QPushButton('Ok'),QPushButton('Cancel')
        self.ok.clicked.connect(self.save_exit)
        self.cancel.clicked.connect(QApplication.instance().quit)

        layout=QFormLayout()
        layout.addWidget(self.ok)
        layout.addWidget(self.cancel)
        self.df_finish_container.setLayout(layout)
        

    def save_exit(self):
        print(self.cols)
        df_data=list()
        row_data=list()
        self.widgets = [self.data_grid.itemAt(i).widget() for i in range(self.data_grid.count())]
        l=0
        for i,w in enumerate(self.widgets):
            if l<=self.cols:
                row_data.append(float(w.text()))
                l+=1
            else:
                df_data.append(row_data)
                row_data=list()
                row_data.append(float(w.text()))
                l=0
        print(df_data)        
        self.df=pd.DataFrame(df_data)
        print(self.df.to_string())
    def exit(self):
        quit()

