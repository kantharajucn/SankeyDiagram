#################################################################
#Name: main_windows.py
#Version: 1.0
#Description: GUI for showing various operations
#################################################################
from PyQt4 import QtGui,QtCore
from uploadingFile import Ui_uploadingFile
from upload import Ui_upload
from mainVisualization import Ui_mainSankeyWindow
import sys
import os
import ntpath
import webbrowser

'''GLobal variables used'''
global filename
shipments = 0

'''GUI for displaying all the process involved'''
class MainSankeyWindow(QtGui.QMainWindow,Ui_mainSankeyWindow):
        def __init__(self, parent=None):
            QtGui.QMainWindow.__init__(self, parent)
            self.setupUi(self)
            self.preProcessing.clicked.connect(self.pre_process)
            self.sankeyDiagram.clicked.connect(self.view_sankey)
            self.attributes.clicked.connect(self.show_attributes)
            self.translation.clicked.connect(self.show_transition)
            self.evaluation.clicked.connect(self.show_evaluation)
            self.plainTextEdit

        def pre_process(self):
            self.plainTextEdit.appendPlainText("Pre Processing the Input file")
            os.system('preProcessingFiles.py')
            self.plainTextEdit.appendPlainText("Processing randomColour.py")
            os.system('randomColor.py')
            self.plainTextEdit.appendPlainText("Processing sankey.py")
            os.system('sankey.py')
            self.plainTextEdit.appendPlainText("Processing generateHTML.py")
            os.system('generateHTML.py')
            self.plainTextEdit.appendPlainText("Processing attributesUsed.py")
            os.system('attributesUsed.py')
            self.plainTextEdit.appendPlainText("Processing transitionTable.py")
            os.system('transitionTable.py')
            self.plainTextEdit.appendPlainText("Cleaning up the temporary files")
            os.system('cleanUp.py')
         
        def view_sankey(self):
            self.plainTextEdit.appendPlainText("Displaying sankey.html")
            webbrowser.open(os.getcwd()+"/../sankey/html/sankey.html")
        def show_attributes(self):
            self.plainTextEdit.appendPlainText("Displaying attribute.html")
            webbrowser.open(os.getcwd()+"/../sankey/html/attribute.html")
        def show_transition(self):
            self.plainTextEdit.appendPlainText("Displaying transition.html")
            webbrowser.open(os.getcwd()+"/../sankey/html/transition.html")
        def show_evaluation(self):
            w = QtGui.QWidget()
            self.plainTextEdit.appendPlainText("Evaluation results re in report")
            QtGui.QMessageBox.information(w, "Message", "Refer the Report for evaluation results")
            w.show()

'''Class for uploading the Data sets'''
class Upload(QtGui.QWidget, Ui_upload):
    ships = 0
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.upload_file)
        self.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.reject)
        self.toolButton.clicked.connect(self.browse_file)
        self.shipmentSubmit.button(QtGui.QDialogButtonBox.Reset).clicked.connect(self.reset)
        self.shipmentSubmit.button(QtGui.QDialogButtonBox.Save).clicked.connect(self.save)
        self.window2 = None
        
    def reset(self):
        self.shipmentEdit.clear()
    
    def save(self):
        w = QtGui.QWidget()
        if self.shipmentEdit.text() == '':
            QtGui.QMessageBox.information(w, "Message", "Please enter the number of shipments")
            w.show()
        else:
            ships = int(self.shipmentEdit.text())
            shipments = ships
        
    def reject(self):
        self.editFile.clear()   
    
    def browse_file(self):
        global filename
        w = QtGui.QWidget()
        shipments = int(self.shipmentEdit.text())
        if shipments > 0: 
            filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
            self.editFile.setText(filename)
            self.shipmentEdit.setText(str(shipments - 1))
        else:
            QtGui.QMessageBox.information(w, "Message", "Uploading is not possible for more than %d files.\n Opening the Main Window" %(shipments))
            w.show()
            if window is not None:
                window.deleteLater()
                self.window2 = MainSankeyWindow()
                self.window2.show()
          
    def upload_file(self):
        w = QtGui.QWidget()
        file_read = open(filename, "rb")
        head,tail = ntpath.split(str(filename))
        local_file = tail
        with open(os.path.join(os.pardir+"/data", local_file), 'wb') as f:
            f.write(file_read.read())
            if os.path.exists(os.path.join(os.pardir+"/data", local_file)):
                QtGui.QMessageBox.information(w, "Message", "Uploading is Success")
                w.show()
                self.editFile.clear()
            else:
                QtGui.QMessageBox.information(w, "Message", "Uploading is Failed. Please Try Again")
                w.show()
                self.editFile.clear()
            f.close()
            file_read.close()


'''Main function'''
if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    window = Upload()
    window.show()
    sys.exit(app.exec_())