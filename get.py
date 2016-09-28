from idm import Ui_MainWindow
from PyQt4 import QtCore, QtGui
import sys
from adddialog import Ui_Dialog
import urllib2

class Dialog(QtGui.QDialog):
    def __init__(self):
        super(Dialog,self).__init__()
        self.d=Ui_Dialog()
        self.d.setupUi(self)

class Main(QtGui.QMainWindow):
    def __init__(self):
        super(Main,self).__init__()
        self.window=Ui_MainWindow()
        self.window.setupUi(self)
        self.window.actionHide.triggered.connect(self.hide)
        self.window.actionVisible.triggered.connect(self.visible)
        self.window.action_Add_URL.triggered.connect(self.downloadDialog)

    def downloadDialog(self):
        self.dialog=Dialog()
        self.dialog.show()

    def hide(self):
        self.window.toolBar.hide()

    def visible(self):
        self.window.toolBar.show()

def main():
    app=QtGui.QApplication(sys.argv)
    win=Main()
    win.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
        
    




