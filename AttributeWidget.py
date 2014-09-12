# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/AttributeWidget.ui'
#
# Created: Fri Sep 12 13:50:06 2014
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

class Ui_AttributeWidget(object):
    def setupUi(self, AttributeWidget):
        AttributeWidget.setObjectName(_fromUtf8("AttributeWidget"))
        AttributeWidget.resize(583, 432)
        self.gridLayout_2 = QtGui.QGridLayout(AttributeWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.frame = QtGui.QFrame(AttributeWidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pbuttonLoad = QtGui.QPushButton(self.frame)
        self.pbuttonLoad.setObjectName(_fromUtf8("pbuttonLoad"))
        self.gridLayout.addWidget(self.pbuttonLoad, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(451, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.twidgetClassMap = QtGui.QTableWidget(self.frame)
        self.twidgetClassMap.setObjectName(_fromUtf8("twidgetClassMap"))
        self.twidgetClassMap.setColumnCount(2)
        self.twidgetClassMap.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.twidgetClassMap.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.twidgetClassMap.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.twidgetClassMap, 1, 0, 1, 2)
        self.label_6 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 7)
        self.label = QtGui.QLabel(AttributeWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.leditRadius = QtGui.QLineEdit(AttributeWidget)
        self.leditRadius.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leditRadius.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leditRadius.setObjectName(_fromUtf8("leditRadius"))
        self.gridLayout_2.addWidget(self.leditRadius, 3, 1, 1, 5)
        self.label_2 = QtGui.QLabel(AttributeWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 3, 6, 1, 1)
        self.line = QtGui.QFrame(AttributeWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 7)
        self.pbuttonNext = QtGui.QPushButton(AttributeWidget)
        self.pbuttonNext.setObjectName(_fromUtf8("pbuttonNext"))
        self.gridLayout_2.addWidget(self.pbuttonNext, 5, 6, 1, 1)
        self.pbuttonPrevious = QtGui.QPushButton(AttributeWidget)
        self.pbuttonPrevious.setObjectName(_fromUtf8("pbuttonPrevious"))
        self.gridLayout_2.addWidget(self.pbuttonPrevious, 5, 5, 1, 1)
        self.pbuttonNextEmpty = QtGui.QPushButton(AttributeWidget)
        self.pbuttonNextEmpty.setObjectName(_fromUtf8("pbuttonNextEmpty"))
        self.gridLayout_2.addWidget(self.pbuttonNextEmpty, 5, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(151, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 5, 1, 1, 4)
        self.label_3 = QtGui.QLabel(AttributeWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.lCode = QtGui.QLabel(AttributeWidget)
        self.lCode.setText(_fromUtf8(""))
        self.lCode.setObjectName(_fromUtf8("lCode"))
        self.gridLayout_2.addWidget(self.lCode, 0, 1, 1, 6)
        self.lDescription = QtGui.QLabel(AttributeWidget)
        self.lDescription.setText(_fromUtf8(""))
        self.lDescription.setObjectName(_fromUtf8("lDescription"))
        self.gridLayout_2.addWidget(self.lDescription, 1, 1, 1, 6)
        self.label_4 = QtGui.QLabel(AttributeWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.retranslateUi(AttributeWidget)
        QtCore.QMetaObject.connectSlotsByName(AttributeWidget)

    def retranslateUi(self, AttributeWidget):
        AttributeWidget.setWindowTitle(_translate("AttributeWidget", "Attribute Editor", None))
        self.pbuttonLoad.setText(_translate("AttributeWidget", "Load", None))
        item = self.twidgetClassMap.horizontalHeaderItem(0)
        item.setText(_translate("AttributeWidget", "Class Code", None))
        item = self.twidgetClassMap.horizontalHeaderItem(1)
        item.setText(_translate("AttributeWidget", "Class Description", None))
        self.label_6.setText(_translate("AttributeWidget", "Class Map", None))
        self.label.setText(_translate("AttributeWidget", "Buffer point", None))
        self.leditRadius.setText(_translate("AttributeWidget", "0.0", None))
        self.label_2.setText(_translate("AttributeWidget", "map units ", None))
        self.pbuttonNext.setText(_translate("AttributeWidget", "Next", None))
        self.pbuttonPrevious.setText(_translate("AttributeWidget", "Previous", None))
        self.pbuttonNextEmpty.setText(_translate("AttributeWidget", "Next Empty", None))
        self.label_3.setText(_translate("AttributeWidget", "Current Class Code:", None))
        self.label_4.setText(_translate("AttributeWidget", "Description:", None))

