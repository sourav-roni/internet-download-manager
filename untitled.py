from idm2 import Ui_MainWindow
from PyQt4 import QtCore, QtGui
import sys
from adddialog import Ui_Dialog
import urllib2
import requests

def downloader(url,filetype):
    #print url
    #print filetype
    proxyDict = { 'http' : "http://10.3.100.207:8080",
                  'https' : "https://10.3.100.207:8080",
                  'ftp' : "ftp://10.3.100.207:8080"
                  }
    hdr = [ 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'none',
        'en-US,en;q=0.8',
       'keep-alive' ]
    proxy = urllib2.ProxyHandler(proxyDict)
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    x = urllib2.urlopen(url).read()
    f = open(filetype,'w')
    f.write(x)


class newTableModel(QtCore.QAbstractTableModel):

    def __init__(self,datum=[[]],headers=[],parent = None):
        QtCore.QAbstractTableModel.__init__(self,parent)
        self.__datum = datum
        self.__headers = headers

    def rowCount(self,parent):
        return len(self.__datum)

    def columnCount(self,parent):
        return len(self.__datum[0])

    def data(self, index,role):

        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self.__datum[row][column]
            return value

        if role == QtCore.Qt.ToolTipRole:
            row = index.row()
            column = index.column()
            return self.__datum[row][column]
        

    def headerData(self, section, orientation, role):
        
        if role == QtCore.Qt.DisplayRole:
            
            if orientation == QtCore.Qt.Horizontal:
                
                if section < len(self.__headers):
                    return self.__headers[section]
                else:
                    return "not implemented"
            else:
                return QtCore.QString("Download %1").arg(section+1)


    def insertRows(self, position, rows, defaultValues, parent = QtCore.QModelIndex()):
        self.beginInsertRows(parent, position, position + rows - 1)
        
        for i in range(rows):
            
            self.__datum.insert(position, defaultValues)
        
        self.endInsertRows()
        
        return True

                
    

class Dialog(QtGui.QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        super(Dialog,self).__init__(parent)
        #self.d=Ui_Dialog()
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.okButton.clicked.connect(self.okButtonclicked)

    def okButtonclicked(self):
        url=str(self.lineEdit.text())
        filetype=str(self.lineEdit_2.text())
        filename = url.split('/')[-1].split('#')[0].split('?')[0]
        self.close()
        print url
        print filename
        data = [url,filename,filetype,"------"]
        model.insertRows(0,1,data)
        downloader(url,filename)
    

class Main(QtGui.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        #self.window=Ui_MainWindow()
        self.setupUi(self)
        data = [["---","---","---","---"]]
        headers = ["URL","File Name","File Type","Progress"]
        global model
        model = newTableModel(data,headers)
        self.tableView.setModel(model)
        self.tableView.show()
        self.actionHide.triggered.connect(self.hide)
        self.actionVisible.triggered.connect(self.visible)
        self.action_Add_URL.triggered.connect(self.downloadDialog)

    def downloadDialog(self):
        dia=Dialog(self)
        dia.show()
        

    def hide(self):
        self.toolBar.hide()

    def visible(self):
        self.toolBar.show()

def main():
    app=QtGui.QApplication(sys.argv)
    global win
    win=Main()
    win.show()
    sys.exit(app.exec_())

if __name__=='__main__':
    main()
        
    




