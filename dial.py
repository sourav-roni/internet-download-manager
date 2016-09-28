#!/usr/bin/python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dial.ui'
#
# Created: Wed Dec  9 21:25:00 2015
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(355, 335)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.dial = QtGui.QDial(Form)
        self.dial.setObjectName(_fromUtf8("dial"))
        self.gridLayout.addWidget(self.dial, 4, 1, 1, 1)
        self.horizontalSlider = QtGui.QSlider(Form)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout.addWidget(self.horizontalSlider, 4, 0, 1, 1)
        self.verticalSlider = QtGui.QSlider(Form)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName(_fromUtf8("verticalSlider"))
        self.gridLayout.addWidget(self.verticalSlider, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.label.setNum)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.dial.setValue)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.verticalSlider.setValue)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.horizontalSlider.setValue)
        QtCore.QObject.connect(self.verticalSlider, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.dial.setValue)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "0", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

