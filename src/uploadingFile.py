#################################################################
#Name: uploadingFile.py
#Version: 1.0
#Description: Displaying options for Generating sankey,
# Attributes used and Transitions for each Record
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

class Ui_uploadingFile(object):
    def setupUi(self, uploadingFile):
        uploadingFile.setObjectName(_fromUtf8("uploadingFile"))
        uploadingFile.resize(404, 277)
        uploadingFile.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout_4 = QtGui.QVBoxLayout(uploadingFile)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.heading = QtGui.QLabel(uploadingFile)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("MS PGothic"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.heading.setFont(font)
        self.heading.setTextFormat(QtCore.Qt.RichText)
        self.heading.setScaledContents(True)
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName(_fromUtf8("heading"))
        self.verticalLayout_4.addWidget(self.heading)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.label = QtGui.QLabel(uploadingFile)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_8.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.lineEdit = QtGui.QLineEdit(uploadingFile)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_8.addWidget(self.lineEdit)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem2 = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.buttonBox = QtGui.QDialogButtonBox(uploadingFile)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_9.addWidget(self.buttonBox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.label_4 = QtGui.QLabel(uploadingFile)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_10.addWidget(self.label_4)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.retranslateUi(uploadingFile)
        QtCore.QMetaObject.connectSlotsByName(uploadingFile)

    def retranslateUi(self, uploadingFile):
        uploadingFile.setWindowTitle(_translate("uploadingFile", "UploadingFile", None))
        self.heading.setText(_translate("uploadingFile", "Sankey Diagram", None))
        self.label.setText(_translate("uploadingFile", "Shipments", None))
        self.label_4.setText(_translate("uploadingFile", "Copyright @kantharaju", None))

