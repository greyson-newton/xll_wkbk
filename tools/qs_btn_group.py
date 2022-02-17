from PyQt5.QtCore import Qt, QSize, QEvent , QObject, pyqtSignal
# from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import * 
import sys
  
class MyQButtonGroup(QObject):
    trigger = pyqtSignal((),(bool,))

    def init(self):
      
        self.checked = dict()
        self.buttons=dict()
        self.qid_open=-1
    def addButton(self, button,bid):
        self.buttons[bid]=button
        button.clicked.connect(self.trigger.emit)

    def removeButton(self, button):
        button.clicked.disconnect(self.trigger.emit)

    def ret_checked(self):
        return [btn.isChecked() for btn in self.buttons.values()]
        
    def ret_open_q(self):
        for qid,btn in self.buttons.items():
            if btn.isChecked():
                return qid
            else:
                return -1
    def clr_checked(self):
        for q,btn in self.buttons:
            btn.isChecked(False)
        self.checked = dict()
        self.qid_open=-1
    def set_checked(self,bid):
        self.buttons[bid].setChecked(True)
    def add_checked(self):
        print('self.buttons:',self.buttons)

        if self.ret_checked().count(True)==1 :
            bid=self.ret_checked().index(True)
            self.checked=dict()
            self.checked[bid]=self.buttons.get(bid)
            self.qid_open=bid
        elif self.checked_btns.values().count(True)==0 :
            self.checked[bid]=self.buttons.get(bid)
            self.qid_open=bid

        print('self.checked:',self.checked)
        print('pushed button:',self.qid_open)
