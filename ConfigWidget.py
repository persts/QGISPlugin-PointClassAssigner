# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ConfigWidget.ui'
#
# Created: Fri Sep 12 13:50:32 2014
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

class Ui_ConfigWidget(object):
    def setupUi(self, ConfigWidget):
        ConfigWidget.setObjectName(_fromUtf8("ConfigWidget"))
        ConfigWidget.resize(426, 358)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ConfigWidget.sizePolicy().hasHeightForWidth())
        ConfigWidget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtGui.QGridLayout(ConfigWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(ConfigWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.cboxLayers = QtGui.QComboBox(ConfigWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboxLayers.sizePolicy().hasHeightForWidth())
        self.cboxLayers.setSizePolicy(sizePolicy)
        self.cboxLayers.setObjectName(_fromUtf8("cboxLayers"))
        self.gridLayout_2.addWidget(self.cboxLayers, 1, 0, 1, 3)
        self.label_2 = QtGui.QLabel(ConfigWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.cboxClassCode = QtGui.QComboBox(ConfigWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboxClassCode.sizePolicy().hasHeightForWidth())
        self.cboxClassCode.setSizePolicy(sizePolicy)
        self.cboxClassCode.setObjectName(_fromUtf8("cboxClassCode"))
        self.gridLayout_2.addWidget(self.cboxClassCode, 2, 1, 1, 2)
        self.label_3 = QtGui.QLabel(ConfigWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.cboxClassDescription = QtGui.QComboBox(ConfigWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboxClassDescription.sizePolicy().hasHeightForWidth())
        self.cboxClassDescription.setSizePolicy(sizePolicy)
        self.cboxClassDescription.setObjectName(_fromUtf8("cboxClassDescription"))
        self.gridLayout_2.addWidget(self.cboxClassDescription, 3, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 1, 1, 1)
        self.frame = QtGui.QFrame(ConfigWidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.leditAttributeName = QtGui.QLineEdit(self.frame)
        self.leditAttributeName.setObjectName(_fromUtf8("leditAttributeName"))
        self.gridLayout.addWidget(self.leditAttributeName, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 3, 1, 1)
        self.cboxAttributeType = QtGui.QComboBox(self.frame)
        self.cboxAttributeType.setObjectName(_fromUtf8("cboxAttributeType"))
        self.cboxAttributeType.addItem(_fromUtf8(""))
        self.cboxAttributeType.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cboxAttributeType, 2, 1, 1, 2)
        self.sboxAttributeLength = QtGui.QSpinBox(self.frame)
        self.sboxAttributeLength.setMinimum(1)
        self.sboxAttributeLength.setMaximum(250)
        self.sboxAttributeLength.setObjectName(_fromUtf8("sboxAttributeLength"))
        self.gridLayout.addWidget(self.sboxAttributeLength, 2, 3, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(267, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 2)
        self.pbuttonAddAttribute = QtGui.QPushButton(self.frame)
        self.pbuttonAddAttribute.setObjectName(_fromUtf8("pbuttonAddAttribute"))
        self.gridLayout.addWidget(self.pbuttonAddAttribute, 3, 2, 1, 2)
        self.label_6 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 2)
        self.label_4 = QtGui.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 5, 0, 1, 3)
        spacerItem2 = QtGui.QSpacerItem(314, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 6, 0, 1, 2)
        self.pbuttonDone = QtGui.QPushButton(ConfigWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbuttonDone.sizePolicy().hasHeightForWidth())
        self.pbuttonDone.setSizePolicy(sizePolicy)
        self.pbuttonDone.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pbuttonDone.setObjectName(_fromUtf8("pbuttonDone"))
        self.gridLayout_2.addWidget(self.pbuttonDone, 6, 2, 1, 1)

        self.retranslateUi(ConfigWidget)
        QtCore.QMetaObject.connectSlotsByName(ConfigWidget)

    def retranslateUi(self, ConfigWidget):
        ConfigWidget.setWindowTitle(_translate("ConfigWidget", "SamplePoint Configuration", None))
        self.label.setText(_translate("ConfigWidget", "Layer", None))
        self.label_2.setText(_translate("ConfigWidget", "Class Code (Integer)", None))
        self.label_3.setText(_translate("ConfigWidget", "Class Description (String)", None))
        self.label_5.setText(_translate("ConfigWidget", "Length", None))
        self.cboxAttributeType.setItemText(0, _translate("ConfigWidget", "Integer", None))
        self.cboxAttributeType.setItemText(1, _translate("ConfigWidget", "String", None))
        self.pbuttonAddAttribute.setText(_translate("ConfigWidget", "Add Attribute", None))
        self.label_6.setText(_translate("ConfigWidget", "Name", None))
        self.label_7.setText(_translate("ConfigWidget", "Type", None))
        self.label_4.setText(_translate("ConfigWidget", "Add Attribute", None))
        self.pbuttonDone.setText(_translate("ConfigWidget", "Ok", None))

