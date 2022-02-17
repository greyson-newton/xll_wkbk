import sys
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, uic

ui_file = uic.loadUiType("example.ui")[0]

class UI(QtGui.QMainWindow, ui_file):
    def __init__(self):
        ## Inherit the QMainWindow and ui_file classes
        QtGui.QMainWindow.__init__(self)
        ui_file.__init__(self)
        self.setupUi(self)

    #     ## Create aditional widgets
    #     self.plot_item = self.plotWidget.plot()
    #     self.vLine = pg.InfiniteLine(angle=90, movable=False)
    #     self.hLine = pg.InfiniteLine(angle=0, movable=False)
    #     self.cursorlabel = pg.TextItem(anchor=(-1,10))
    #     ## Build the rest of the GUI
    #     self.format_plot()
    #     ## data
    #     self.plotx = range(100)
    #     self.ploty = [number**2 for number in self.plotx]        
    #     ## Connect signals to actions
    #     self.startbutton.clicked.connect(self.clickedstartButton)
    #     self.exitbutton.clicked.connect(self.clickedexitButton)
    #     self.plotWidget.scene().sigMouseMoved.connect(self.mouseMoved)
    
    # ## OVERWRITE the mouseMoved action:
    def mouseMoved(self, evt):
        pos = evt
        print(pos)
        # if self.plotWidget.sceneBoundingRect().contains(pos):
        #     mousePoint = self.plotWidget.plotItem.vb.mapSceneToView(pos)
        #     index = int(mousePoint.x())
        #     if index > 0 and index < len(self.plotx):
        #     # if index > 0 and index < self.MFmax:
        #         self.cursorlabel.setHtml(
        #             "<span style='font-size: 12pt'>x={:0.1f}, \
        #              <span style='color: red'>y={:0.1f}</span>".format(
        #         mousePoint.x(), mousePoint.y()))
        #     self.vLine.setPos(mousePoint.x())
        #     self.hLine.setPos(mousePoint.y())
  
    def clickedstartButton(self):  #action if start button clicked
        self.plot_item.setData(self.plotx, self.ploty, pen='r')
        self.plotWidget.addItem(self.cursorlabel)

    def clickedexitButton(self):
        self.close()
    
        
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())