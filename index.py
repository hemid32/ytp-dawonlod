import urllib
import sys
from PyQt4 import QtCore, QtGui, uic ,Qt

qtCreatorFile = "maino.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.handel_ui()
        self.button_sav()
        self.reporthook(0,0,0)





    def handel_ui(self):
        self.setFixedSize(614,250)
        self.setWindowTitle('hemidi benameur')
    def button_sav(self):
        self.pushButton.clicked.connect(self.dowonlod)
        self.pushButton_2.clicked.connect(self.lint_save)
    def lint_save(self):
        save = Qt.QFileDialog.getSaveFileName(self,caption='sav as',directory=".",filter="All files(*.*)")

        self.lineEdit_2.setText(str(save))
    def reporthook( self , blocknum, blocksize, totalsize ):


        red = blocksize * blocknum
        if totalsize > 0 :

            res = red * 100 / totalsize
            self.progressBar.setValue(res)
            Qt.QApplication.processEvents()

    def dowonlod(self):
        url_text = self.lineEdit.text()
        open_save = self.lineEdit_2.text()


        try:
            urllib.urlretrieve(str(url_text),str(open_save), self.reporthook)
        except Exception :

            Qt.QMessageBox.critical(self,'Erurr','dawonlod erurr')

            return
        #E:\programation\progect\pyqt\dawnlodyoutub\hmd.zip
        #https://codeload.github.com/ColinDuquesnoy/QDarkStyleSheet/zip/master

        self.progressBar.setValue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        Qt.QMessageBox.information(self,'finishd','finishd dawnlod')
        print 'yas'


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())