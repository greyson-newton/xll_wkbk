# https://www.pythonguis.com/tutorials/qscrollarea/
# from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
#                              QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize, QEvent , QObject, pyqtSignal
from PyQt5.QtWidgets import * 
import sys
from df_btn_group import *
from qs_btn_group import *
from df_wiz import *
# creating a class

# that inherits the QDialog class
class Window(QDialog):
    # constructor

        # # creating a dialog button for ok and cancel
        # self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # self.add_container(self.buttonBox)

        # self.buttonBox.rejected.connect(self.reject)

    def __init__(self):
        super(Window, self).__init__()
        self.num=1
        self.num_wkbk_qs=0
        self.q_open=False

        self.qs=list()
        self.qs_dict=dict()
        self.setWindowTitle("Python")
        
        # setting geometry to the window
        self.setGeometry(100, 100, 500, 1000)
        self.mainLayout = QVBoxLayout()

        self.wkbk_container = QGroupBox("workbook")
        self.wkbk_name_lne = QLineEdit()
        self.num_qs_sb = QSpinBox()
        self.mk_wkbk_btn=QPushButton('fill xllwkbk')
        self.mk_wkbk_btn.clicked.connect(self.populate_xllwkbk)
        self.create_wkbk_form()

    def add_container(self,ctnr):  
        self.mainLayout.addWidget(ctnr)
        self.setLayout(self.mainLayout)

    def q_dict(self):
        op = { i : ele for i,ele in enumerate(self.qs) }
        self.qs_dict=op
    # https://stackoverflow.com/questions/5899826/pyqt-how-to-remove-a-widget
    # def rm_widget(self,layout_name,widget_name):
    #     layout_name.removeWidget(widget_name)
    #     widget_name.deleteLater()
    #     widget_name = None
    def update_qs(self):
        q_n = len(self.qs)+1
        print(q_n,self.num_wkbk_qs)
        if q_n != self.num_wkbk_qs:
            self.qs.append(self.qs_name_lne.text())
            self.qs_label.setText(f"({q_n}/{self.num_wkbk_qs})")
            self.qs_name_lne.setText("")
        elif q_n ==self.num_wkbk_qs and len(self.qs)>0: 
            self.qs.append(self.qs_name_lne.text())   
            # self.rm_widget(self.qs_container,self.qs_name_lne)           
            self.qs_name_lne.setText(":)")
            self.qs_label.setText("COMPLETE")
            self.create_qs_viewer()
        else:
            print('err')

    def populate_xllwkbk(self):
        self.num_wkbk_qs=int(self.num_qs_sb.text())
        self.qs_container = QGroupBox("Fill Questions")
        self.qs_name_lne = QLineEdit()
        self.qs_label = QLabel()
        self.next_btn = QPushButton('next')

        self.create_qs_form()
        self.next_btn.clicked.connect(self.update_qs)
        
    def create_qs_form(self):
        
        layout = QFormLayout()
        layout.addRow(self.qs_label,self.qs_name_lne)
        layout.addRow(self.next_btn)
        self.qs_container.setLayout(layout)   
        self.add_container(self.qs_container)
    # creat form method
    def create_qs_viewer(self):
        self.qs_selector_container = QGroupBox("Question Manager")
        layout = QFormLayout()
        self.q_dict()
        self.q_btns = MyQButtonGroup()
        self.q_btns.init()
        for q_num,q in self.qs_dict.items():
            q_btn=QPushButton(q)
            q_btn.setCheckable(True)
            q_btn.setChecked(False)
            self.q_btns.addButton(q_btn,q_num)
            layout.addWidget(q_btn)      
        self.q_btns.trigger.connect(self.view_q)
        self.qs_selector_container.setLayout(layout)
        self.add_container(self.qs_selector_container)

        self.dfs_selector_container = QGroupBox("Question DF's")
        self.create_dfs_form()

        self.add_container(self.dfs_selector_container)

        
    def view_q(self):
        df_grid=QGridLayout()
        self.q_btns.add_checked()
        open_qid=self.q_btns.qid_open
        print('viewing dfs of q_id:',open_qid)
        dfs=self.dfs.get(open_qid)
        df_btn_group=self.dfs_btns.get(open_qid)
        print(df_btn_group.dfbuttons)
        df_btn_group.trigger.connect(self.df_wizard)
        positions = [(0, y) for y in range(len(df_btn_group.dfbuttons))]
        for position, btn in zip(positions, df_btn_group.dfbuttons.values()):
            print(btn)
            df_grid.addWidget(btn, *position)
        self.dfs_selector_container.setLayout(df_grid)
        self.add_container(self.dfs_selector_container)

    def df_wizard(self):

        wizard=df_wiz()
        wizard.exec()

    def create_dfs_form(self):
        # Making DF viewer for every problem
        self.dfs=dict()
        self.dfs_btns=dict()
        for qid in self.qs_dict.keys():
            dfs_btn=QPushButton('Enter DFS')
            qdf_group=MyDFButtonGroup()
            qdf_group.init(qid)
            qdf_group.addButton(dfs_btn)
            self.dfs_btns[qid]=qdf_group
            self.dfs[qid]=list()


    # # creat form method
    def create_wkbk_form(self):
  
        # creating a form layout
        layout = QFormLayout()
  
        # adding rows
        # for name and adding input text

        layout.addRow(QLabel("enter wkbk name"), self.wkbk_name_lne)
  
        # for age and adding spin box
        layout.addRow(QLabel("enter # problems: "), self.num_qs_sb)
        # layout.addRow(QLabel("mk xl-wkbk"),self.mk_wkbk_btn)
        layout.addRow(self.mk_wkbk_btn)
        self.wkbk_container.setLayout(layout)        
        self.add_container(self.wkbk_container)

if __name__ == '__main__':
  
    # create pyqt5 app
    app = QApplication(sys.argv)
  
    # create the instance of our Window
    window = Window()
  
    # showing the window
    window.show()
  
    # start the app
    sys.exit(app.exec())