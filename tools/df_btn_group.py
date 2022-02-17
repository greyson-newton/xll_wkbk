from PyQt5.QtCore import Qt, QSize, QEvent , QObject, pyqtSignal
# from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import * 
import sys


class MyDFButtonGroup(QObject):
    trigger = pyqtSignal((),(bool,))
    def init(self,qid):
        self.dfchecked = dict()
        self.dfbuttons=dict()
        self.dfid_open=-1
        self.qid=qid
        self.dfid=0
    def addButton(self, button):
        
        self.dfbuttons[self.dfid]=button
        button.clicked.connect(self.trigger.emit)
        self.dfid+=1

    def removeButton(self, button):
        button.clicked.disconnect(self.trigger.emit)

    def ret_checked(self):
        return [btn.isChecked() for btn in self.dfbuttons.values()]
    def ret_open_q(self):
        for dfid,btn in self.self.dfbuttons.items():
            if btn.isChecked():
                return dfid
            else:
                return -1
    def clr_checked(self):
        for dfid,btn in self.dfbuttons.items():
            btn.isChecked(False)
        self.dfchecked = dict()
    def set_checked(self,dfid):
        self.dfbuttons[dfid].setChecked(True)
    def add_checked(self):
        print('self.dfbuttons:',self.dfbuttons)
        if self.ret_checked().count(True)==1 :
            dfid=self.ret_checked().index(True)
            checked=dict()
            checked[dfid]=self.dfbuttons.get(dfid)
        elif checked_btns.values().count(True)==0 :
            self.dfchecked[dfid]=self.dfbuttons.get(dfid)

        print('checked:',self.dfchecked)