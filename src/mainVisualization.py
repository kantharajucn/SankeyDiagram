#################################################################
#Name: mainVisualization.py
#Version: 1.0
#Description: GUI for showing various operations
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

'''Creating widgets for GUI'''
class Ui_mainSankeyWindow(object):
    def setupUi(self, mainSankeyWindow):
        mainSankeyWindow.setObjectName(_fromUtf8("mainSankeyWindow"))
        mainSankeyWindow.resize(711, 354)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainSankeyWindow.sizePolicy().hasHeightForWidth())
        mainSankeyWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        mainSankeyWindow.setFont(font)
        mainSankeyWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtGui.QWidget(mainSankeyWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Engravers MT"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.evaluation = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.evaluation.setFont(font)
        self.evaluation.setObjectName(_fromUtf8("evaluation"))
        self.gridLayout.addWidget(self.evaluation, 8, 1, 1, 1)
        self.sankeyDiagram = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sankeyDiagram.setFont(font)
        self.sankeyDiagram.setObjectName(_fromUtf8("sankeyDiagram"))
        self.gridLayout.addWidget(self.sankeyDiagram, 5, 1, 1, 1)
        self.translation = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.translation.setFont(font)
        self.translation.setObjectName(_fromUtf8("translation"))
        self.gridLayout.addWidget(self.translation, 7, 1, 1, 1)
        self.attributes = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.attributes.setFont(font)
        self.attributes.setObjectName(_fromUtf8("attributes"))
        self.gridLayout.addWidget(self.attributes, 6, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        self.preProcessing = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.preProcessing.setFont(font)
        self.preProcessing.setObjectName(_fromUtf8("preProcessing"))
        self.gridLayout.addWidget(self.preProcessing, 4, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout.addLayout(self.verticalLayout, 9, 0, 1, 1)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout.addWidget(self.plainTextEdit, 10, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        mainSankeyWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(mainSankeyWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainSankeyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainSankeyWindow)
        QtCore.QMetaObject.connectSlotsByName(mainSankeyWindow)

    def retranslateUi(self, mainSankeyWindow):
        mainSankeyWindow.setWindowTitle(_translate("mainSankeyWindow", "Sankey Window", None))
        self.label.setText(_translate("mainSankeyWindow", "Visualization of Sub Space Clustering", None))
        self.evaluation.setText(_translate("mainSankeyWindow", "Evaluation", None))
        self.sankeyDiagram.setText(_translate("mainSankeyWindow", "Sankey Diagram", None))
        self.translation.setText(_translate("mainSankeyWindow", "View Transition", None))
        self.attributes.setText(_translate("mainSankeyWindow", "View Attributes", None))
        self.preProcessing.setText(_translate("mainSankeyWindow", "Pre Processing", None))

