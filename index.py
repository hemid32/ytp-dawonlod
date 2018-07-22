import urllib
from urllib2 import urlopen
import sys
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "maino.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.handel_ui()
        self.button_sav()


    def handel_ui(self):
        self.setFixedSize(614,250)
        self.setWindowTitle('hemidi benameur')
    def button_sav(self):
        self.pushButton.clicked.connect(self.dowonlod)
        #https://www.youtube.com/watch?v=MQoQcPHAJN0
        #self.pushButton.connect(self.pushButton, self.SIGNAL('clicked()'), self.dowonlod)
        #self.puchButton.clicked.connect(partial(self.dowonlod))
        #self.pushButton.clicked.connect(partial(self.dowonlod, pushButton.text()))
        #self.pushButton.clicked.connect(lambda:self.dowonlod)
        #QtCore.pushButton.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.dowonlod)

    def lint_save(self):
        pass
    def loding(self, blocknum,blocksize,totalsize):
        pass

    def dowonlod(self):
        url_text = self.lineEdit.text()
        open_save = self.lineEdit_2.text()
        #f = [open_save]
        #ydl_opts = {
        #   'verbose': True,  # like this
        #  'outtmpl':'E:\programation\hemidi.mp4',  # how can i find
        #   'progress_hooks': [100],  # how can i find
        #}
        #ydl_opts = {'outtmpl': str(f[0])}

        #ydl_opts = {'file_name.mp4'}
        #ydl_opts = {'outtmpl': 'file_name.mp4'}
        #with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        #    ydl.download([str(url_text)])
        try:
            urllib.urlretrieve(str(url_text),str(open_save),self.loding)
        except Exception :
            print 'ERORR'
            return


        self.progressBar.setValue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        #print'ok'
        #QMessageBox.information(self,'dnvkjfvn','dvufdu')
        print 'yas'


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())