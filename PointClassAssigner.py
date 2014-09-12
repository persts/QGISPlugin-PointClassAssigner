# -*- coding: utf-8 -*-
#
# Point Class Assigner Plugin
# Copyright (C) 2014 Peter Ersts
# ersts@amnh.org
#
# --------------------------------------------------------------------------
#
# This file is part of Point Class Assigner.
#
# Point Class Assigner is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Point Class Assigner is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Point Class Assigner.  If not, see <http://www.gnu.org/licenses/>.
#
# This work was supported by Conservation International under grant  #66236,
# entitled Partnership on research on methods and strategies for monitoring
# selected non-forest habitats, awarded to the American Museum of Natural History,
# Center for Biodiversity and Conservation.
# --------------------------------------------------------------------------
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from ConfigWidget import Ui_ConfigWidget
from AttributeWidget import Ui_AttributeWidget

import re
import resources

class PointClassAssigner:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.plugin = AttributeWidget(iface)

    def initGui(self):
        # Create action that will start plugin
        self.action = QAction(QIcon(":/PointClassAssigner/icon.png"), "&PointClassAssigner", self.iface.mainWindow())
        self.iface.addToolBarIcon(self.action)
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("activated()"), self.run)

        # Add toolbar button and menu item
        self.iface.addPluginToMenu("PointClassAssigner", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        #TODO Update this
        self.iface.removePluginMenu("PointClassAssigner", self.action)

    def run(self):
        self.plugin.launch()

class AttributeWidget(QWidget, Ui_AttributeWidget):
    def __init__(self, iface):
        QWidget.__init__(self)
        self.setupUi(self)
        self.iface = iface
        self.layer = None
        self.allFeatureIds = None
        self.currentFeature = 0
        self.classCodeAttribute = ''
        self.classDescriptionAttribute = ''

        self.twidgetClassMap.horizontalHeader().setStretchLastSection(True)
        self.twidgetClassMap.setSelectionMode(QAbstractItemView.SingleSelection)
        self.twidgetClassMap.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.configWidget = ConfigWidget(iface)

        QObject.connect(self.configWidget, SIGNAL("configured()"), self.update)
        QObject.connect(self.iface.mapCanvas(), SIGNAL("renderComplete(QPainter *)"), self.renderBuffer)
        QObject.connect(self.leditRadius, SIGNAL("editingFinished()"), self.loadPan)
        QObject.connect(self.twidgetClassMap, SIGNAL("cellClicked(int, int)"), self.tableCellClicked)
        QObject.connect(self.iface.mapCanvas(), SIGNAL("selectionChanged(QgsMapLayer *)"), self.userSelectedPoint)

    def on_pbuttonLoad_pressed(self):
        lvFileName = QFileDialog.getOpenFileName(self, "Open Class Map", ".", "Text Files (*.txt)")
        if lvFileName != '':
            self.loadClassMap(lvFileName)

    def on_pbuttonNext_pressed(self):
        if self.currentFeature + 1 != len(self.allFeatureIds):
            self.currentFeature += 1
            self.loadPan()

    def on_pbuttonNextEmpty_pressed(self):
        lvFeatures = self.layer.getFeatures()
        for lvFeature in lvFeatures:
            lvAttribute = lvFeature.attribute(self.classCodeAttribute)
            if type(lvAttribute) is QPyNullVariant:
                self.currentFeature = self.allFeatureIds.index(lvFeature.id());
                self.loadPan()
                return
        QMessageBox.warning(self.iface.mainWindow(), 'Done!', 'All points have attributes')

    def on_pbuttonPrevious_pressed(self):
        if self.currentFeature != 0:
            self.currentFeature -= 1
            self.loadPan()

    def launch(self):
        self.hide()
        self.configWidget.loadLayers()
        if self.configWidget.numberOfLayers() == 0:
            QMessageBox.warning(self.iface.mainWindow(), 'No Point Layers!', 'You must have at least one point layer loaded.')
        else:
            self.configWidget.show()
            self.configWidget.move(self.iface.mainWindow().pos())


    def loadClassMap(self, theFileName):
        #Load text file containing class codes and descriptions
        lvFile = QFile(theFileName)
        if lvFile.open(QIODevice.ReadOnly):
            while self.twidgetClassMap.rowCount() > 0:
                self.twidgetClassMap.removeRow(0)
            while not lvFile.atEnd():
                lvLine = lvFile.readLine().split(',')
                if len(lvLine) == 2:
                    lvRow = self.twidgetClassMap.rowCount() + 1
                    self.twidgetClassMap.setRowCount(lvRow)
                    self.twidgetClassMap.setItem(lvRow - 1, 0, QTableWidgetItem(str(lvLine[0])))
                    self.twidgetClassMap.setItem(lvRow - 1, 1, QTableWidgetItem(re.sub('[\n\r]', '', str(lvLine[1]))))
        else:
            QMessageBox.warning(self, "File Error", "Could not open %1", theFileName)

    def loadPan(self):
        if self.layer is None:
            return
        self.twidgetClassMap.clearSelection()
        self.layer.removeSelection()
        self.layer.select(self.allFeatureIds[self.currentFeature])
        lvCanvas = self.iface.mapCanvas()
        lvFeature = self.layer.selectedFeatures()[0]
        lvPoint = lvFeature.geometry().asPoint()
        lvPoint = lvCanvas.mapSettings().layerToMapCoordinates(self.layer, lvPoint)
        lvRect = QgsRectangle(lvPoint[0] - (lvCanvas.extent().width() / 2),
                              lvPoint[1] - (lvCanvas.extent().height() / 2),
                              lvPoint[0] + (lvCanvas.extent().width() / 2),
                              lvPoint[1] + (lvCanvas.extent().height() / 2))
        lvCanvas.setExtent(lvRect)
        lvCanvas.refresh()

        lvAttribute = lvFeature.attribute(self.classCodeAttribute)
        if type(lvAttribute) is QPyNullVariant:
            self.lCode.setText("")
        else:
            self.lCode.setText(str(lvAttribute))

        lvAttribute = lvFeature.attribute(self.classDescriptionAttribute)
        if type(lvAttribute) is QPyNullVariant:
            self.lDescription.setText("")
        else:
            self.lDescription.setText(lvAttribute)

    def renderBuffer(self, thePainter):
        if self.layer is not None and self.layer.selectedFeatureCount() == 1:
            lvCanvas = self.iface.mapCanvas()
            lvFeature = self.layer.selectedFeatures()[0]
            lvPoint = lvFeature.geometry().asPoint()
            lvPoint = lvCanvas.mapSettings().layerToMapCoordinates(self.layer, lvPoint)
            lvPoint = lvCanvas.mapSettings().mapToPixel().transform(lvPoint)
            lvRef1 = lvCanvas.mapSettings().mapToPixel().transform(0.0, 0.0)
            lvRef2 = lvCanvas.mapSettings().mapToPixel().transform(0.0, float(self.leditRadius.text()))
            lvRadius = abs(lvRef1.y() - lvRef2.y())
            thePainter.setPen(Qt.yellow)
            thePainter.drawEllipse(lvPoint[0] - lvRadius, lvPoint[1] - lvRadius, lvRadius*2, lvRadius*2)

    def tableCellClicked(self, theRow, theColumn):
        self.twidgetClassMap.selectRow(theRow)
        if self.layer.selectedFeatureCount() != 0:
            lvFeature = self.layer.selectedFeatures()[0]
            lvAttributes = {lvFeature.fieldNameIndex(self.classCodeAttribute): int(self.twidgetClassMap.item(theRow, 0).text()),
                            lvFeature.fieldNameIndex(self.classDescriptionAttribute): self.twidgetClassMap.item(theRow, 1).text()}
            self.layer.dataProvider().changeAttributeValues({lvFeature.id(): lvAttributes})
            self.lCode.setText(self.twidgetClassMap.item(theRow, 0).text())
            self.lDescription.setText(self.twidgetClassMap.item(theRow, 1).text())


    def update(self):
        self.layer = self.configWidget.getLayer()
        self.move(self.iface.mainWindow().pos())
        self.show()
        self.allFeatureIds = self.layer.allFeatureIds()
        self.currentFeature = 0
        self.classCodeAttribute, self.classDescriptionAttribute = self.configWidget.getClassAttributes()
        self.loadPan()

    def userSelectedPoint(self, theLayer):
        if self.layer.selectedFeatureCount() > 0:
            lvFeature = self.layer.selectedFeatures()[0]
            if lvFeature.id() != self.allFeatureIds[self.currentFeature]:
                #user selected feature
                self.currentFeature = self.allFeatureIds.index(lvFeature.id());
                self.loadPan()


class ConfigWidget(QWidget, Ui_ConfigWidget):
    def __init__(self, iface):
        QWidget.__init__(self)
        self.setupUi(self)
        self.iface = iface
        self.layers = dict()

    @pyqtSlot(str)
    def on_cboxLayers_currentIndexChanged(self, theValue):
        if theValue != '':
            self.loadAttributes()

    def on_pbuttonAddAttribute_pressed(self):
        #Add a new attribute the the selected layer
        lvProvider = self.layers[self.cboxLayers.currentText()].dataProvider()
        if lvProvider.capabilities() &  QgsVectorDataProvider.AddAttributes:
            if self.leditAttributeName.text() != '':
                if self.cboxAttributeType.currentText() == 'Integer':
                    lvProvider.addAttributes([QgsField(self.leditAttributeName.text(), QVariant.Int, "Integer", self.sboxAttributeLength.value())])
                else:
                    lvProvider.addAttributes([QgsField(self.leditAttributeName.text(), QVariant.String, "String", self.sboxAttributeLength.value())])
                self.layers[self.cboxLayers.currentText()].updateFields()
                if self.cboxAttributeType.currentText() == 'Integer':
                    self.loadIntegerAttributes()
                else:
                    self.loadStringAttributes()
                self.leditAttributeName.clear()
        else:
            QMessageBox.warning(self.iface.mainWindow(), "Add Attribute", "Additional attributes can not be added to this layer")

    def on_pbuttonDone_pressed(self):
        if self.cboxClassCode.currentText() == "":
            QMessageBox.warning(self.iface.mainWindow(), "Select Attribute", "You must select a Class Code attribute")
            return
        if self.cboxClassDescription.currentText() == "":
            QMessageBox.warning(self.iface.mainWindow(), "Select Attribute", "You must select a Class Description attribute")
            return

        self.close();
        self.emit(SIGNAL("configured()"));

    def getClassAttributes(self):
        return self.cboxClassCode.currentText(), self.cboxClassDescription.currentText()

    def getLayer(self):
        return self.layers[self.cboxLayers.currentText()]

    def loadAttributes(self):
        #Populate the combo boxes with appropriately type fields
        self.loadIntegerAttributes()
        self.loadStringAttributes()


    def loadIntegerAttributes(self):
        #Populate the combo boxes with appropriately type fields
        self.cboxClassCode.clear()
        lvFields = self.layers[self.cboxLayers.currentText()].dataProvider().fields()
        for lvField in lvFields:
            if lvField.typeName() == 'Integer':
                self.cboxClassCode.addItem(lvField.name())

    def loadLayers(self):
        #Populate the combo box will only point layers
        self.layers = dict()
        self.cboxLayers.clear()
        for lvLayer in self.iface.mapCanvas().layers():
            if lvLayer.type() == QgsMapLayer.VectorLayer:
                if QGis.vectorGeometryType(lvLayer.geometryType()) == 'Point':
                    self.layers[lvLayer.name()] = lvLayer
                    self.cboxLayers.addItem(lvLayer.name())

    def loadStringAttributes(self):
        #Populate the combo boxes with appropriately type fields
        self.cboxClassDescription.clear()
        lvFields = self.layers[self.cboxLayers.currentText()].dataProvider().fields()
        for lvField in lvFields:
            if lvField.typeName() == 'String':
                self.cboxClassDescription.addItem(lvField.name())

    def numberOfLayers(self):
        return len(self.layers)
