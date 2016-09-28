from PyQt4 import QtGui, QtCore, uic
import sys

if __name__=='__main__':

    app=QtGui.QApplication(sys.argv)
    app.setStyle("cleanlooks")

    data = QtCore.QStringList()
    data <<"one"<<"two"<<"three"<<"four"<<"five"

    listWidget = QtGui.QListView()
    listWidget.show()

    mod = QtGui.QStringListModel(data)

    listview = QtGui.QListView()
    listview.show()

    combo = QtGui.QComboBox()
    combo.show()

    combo.setModel(mod)
    listWidget.setModel(mod)
    listview.setModel(mod)

    sys.exit(app.exec_())

    

    
