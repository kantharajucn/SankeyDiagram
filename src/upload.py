#################################################################
#Name: upload.py
#Version: 1.0
#Description: Uploading data file

#################################################################

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

class Ui_upload(object):
    def setupUi(self, upload):
        upload.setObjectName(_fromUtf8("upload"))
        upload.resize(488, 294)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(upload.sizePolicy().hasHeightForWidth())
        upload.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(upload)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.shipments = QtGui.QLabel(upload)
        self.shipments.setObjectName(_fromUtf8("shipments"))
        self.gridLayout.addWidget(self.shipments, 0, 0, 1, 1)
        self.shipmentEdit = QtGui.QLineEdit(upload)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shipmentEdit.sizePolicy().hasHeightForWidth())
        self.shipmentEdit.setSizePolicy(sizePolicy)
        self.shipmentEdit.setObjectName(_fromUtf8("shipmentEdit"))
        self.gridLayout.addWidget(self.shipmentEdit, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.shipmentSubmit = QtGui.QDialogButtonBox(upload)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shipmentSubmit.sizePolicy().hasHeightForWidth())
        self.shipmentSubmit.setSizePolicy(sizePolicy)
        self.shipmentSubmit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.shipmentSubmit.setStandardButtons(QtGui.QDialogButtonBox.Reset|QtGui.QDialogButtonBox.Save)
        self.shipmentSubmit.setCenterButtons(True)
        self.shipmentSubmit.setObjectName(_fromUtf8("shipmentSubmit"))
        self.gridLayout.addWidget(self.shipmentSubmit, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lableFile = QtGui.QLabel(upload)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lableFile.sizePolicy().hasHeightForWidth())
        self.lableFile.setSizePolicy(sizePolicy)
        self.lableFile.setObjectName(_fromUtf8("lableFile"))
        self.horizontalLayout.addWidget(self.lableFile)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.editFile = QtGui.QLineEdit(upload)
        self.editFile.setObjectName(_fromUtf8("editFile"))
        self.horizontalLayout.addWidget(self.editFile)
        self.toolButton = QtGui.QToolButton(upload)
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.buttonBox = QtGui.QDialogButtonBox(upload)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_6.addWidget(self.buttonBox)
        self.verticalLayout_8.addLayout(self.verticalLayout_6)
        self.verticalLayout.addLayout(self.verticalLayout_8)

        self.retranslateUi(upload)
        QtCore.QMetaObject.connectSlotsByName(upload)

    def retranslateUi(self, upload):
        upload.setWindowTitle(_translate("upload", "FileUpload", None))
        self.shipments.setText(_translate("upload", "Shipments", None))
        self.lableFile.setText(_translate("upload", "File", None))
        self.toolButton.setText(_translate("upload", "...", None))

