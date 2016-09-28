from PyQt4 import QtGui,QtCore, uic
import sys

class plm(QtCore.QAbstractTableModel):

    def __init__(self,colors=[],parent = None):
        QtCore.QAbstractTableModel.__init__(self,parent)
        self.__colors = colors

    def rowCount(self,parent):
        return len(self.__colors)

    def data(self,index,role):
        
        if role == QtCore.Qt.ToolTipRole:
            return "Hex code : "+ self.__colors[index.row()].name()

        
        if role == QtCore.Qt.DecorationRole:
            row = index.row()
            value = self.__colors[row]

            pixmap = QtGui.QPixmap(26,26)
            pixmap.fill(value)

            icon = QtGui.QIcon(pixmap)

            return icon

        
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            value = self.__colors[row]
            return value.name()
        

if __name__ =='__main__':

    app = QtGui.QApplication(sys.argv)
    app.setStyle("plastique")

    lv = QtGui.QListView()
    lv.show()

    tv = QtGui.QTreeView()
    tv.show()

    cb  =QtGui.QComboBox()
    cb.show()

    table = QtGui.QTableView()
    table.show()


    red = QtGui.QColor(255,0,0)
    blue = QtGui.QColor(0,255,0)
    green = QtGui.QColor(0,0,255)

    mod = plm([red,blue,green])

    lv.setModel(mod)
    tv.setModel(mod)
    cb.setModel(mod)
    table.setModel(mod)

    sys.exit(app.exec_())
    
    
