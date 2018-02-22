# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'updatedgui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_StringFinder(object):
    def setupUi(self, StringFinder):
        StringFinder.setObjectName(_fromUtf8("StringFinder"))
        StringFinder.resize(779, 600)
        self.centralwidget = QtGui.QWidget(StringFinder)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(23, 12, 348, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 12, 348, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.instr = QtGui.QPushButton(self.centralwidget)
        self.instr.setGeometry(QtCore.QRect(20, 195, 350, 50))
        self.instr.setObjectName(_fromUtf8("instr"))
        self.startComp = QtGui.QPushButton(self.centralwidget)
        self.startComp.setEnabled(True)
        self.startComp.setGeometry(QtCore.QRect(410, 195, 350, 50))
        self.startComp.setObjectName(_fromUtf8("startComp"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 260, 741, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.statOut = QtGui.QLabel(self.centralwidget)
        self.statOut.setGeometry(QtCore.QRect(20, 275, 740, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.statOut.setFont(font)
        self.statOut.setAlignment(QtCore.Qt.AlignCenter)
        self.statOut.setObjectName(_fromUtf8("statOut"))
        self.strOut = QtGui.QPlainTextEdit(self.centralwidget)
        self.strOut.setGeometry(QtCore.QRect(20, 320, 740, 260))
        self.strOut.setObjectName(_fromUtf8("strOut"))
        self.CList = QtGui.QListWidget(self.centralwidget)
        self.CList.setGeometry(QtCore.QRect(22, 40, 348, 147))
        self.CList.setObjectName(_fromUtf8("CList"))
        self.DList = QtGui.QListWidget(self.centralwidget)
        self.DList.setGeometry(QtCore.QRect(411, 40, 348, 147))
        self.DList.setObjectName(_fromUtf8("DList"))
        StringFinder.setCentralWidget(self.centralwidget)

        self.retranslateUi(StringFinder)
        QtCore.QMetaObject.connectSlotsByName(StringFinder)

    def retranslateUi(self, StringFinder):
        StringFinder.setWindowTitle(_translate("StringFinder", "String Finder", None))
        self.label.setText(_translate("StringFinder", "Clean Instances", None))
        self.label_2.setText(_translate("StringFinder", "Client Instances", None))
        self.instr.setText(_translate("StringFinder", "Instructions because this thing is horribly made", None))
        self.startComp.setText(_translate("StringFinder", "Start the comparison", None))
        self.label_3.setText(_translate("StringFinder", "Status:", None))
        self.statOut.setText(_translate("StringFinder", "Nothing", None))

