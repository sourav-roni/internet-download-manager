# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sample.ui'
#
# Created: Thu Dec 17 20:58:16 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(695, 407)
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.frame = QtGui.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 90, 691, 281))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_2 = QtGui.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 691, 80))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.pushButton_2 = QtGui.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 10, 101, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 10, 61, 51))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton = QtGui.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 61, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.progressBar = QtGui.QProgressBar(self.frame_2)
        self.progressBar.setGeometry(QtCore.QRect(370, 30, 181, 41))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(580, 20, 91, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(374, 10, 171, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        TabWidget.addTab(self.tab1, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget", None))
        self.pushButton_2.setText(_translate("TabWidget", "Resume/Pause", None))
        self.pushButton_3.setText(_translate("TabWidget", "Stop all", None))
        self.pushButton.setText(_translate("TabWidget", "Add", None))
        self.label.setText(_translate("TabWidget", "Time Remaining", None))
        self.label_2.setText(_translate("TabWidget", "Download Completed", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Now Downloading", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Finished Downloads", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TabWidget = QtGui.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())

