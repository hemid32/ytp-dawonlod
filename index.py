
from __future__ import unicode_literals
import sys
from PyQt4 import QtCore, QtGui, uic
from urllib2 import Request
import youtube_dl
import urllib
import shutil

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
        #self.pushButton.connect(self.pushButton, self.SIGNAL('clicked()'), self.dowonlod)
        #self.puchButton.clicked.connect(partial(self.dowonlod))
        #self.pushButton.clicked.connect(partial(self.dowonlod, pushButton.text()))
        #self.pushButton.clicked.connect(lambda:self.dowonlod)
        #QtCore.pushButton.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.dowonlod)

    def lint_save(self):
        pass
    def loding(self, blocknum , blocksize,totalsize):
        pass
    def dowonlod(self):
        url_text = self.lineEdit.text()
        open_save = self.lineEdit_2.text()
        f = [open_save]
        ydl_opts = {
            'verbose': True,  # like this
            'format': '{}'.format(int(comboget)),  # format,vebrose,ottmpl
            'outtmpl': f[0],  # how can i find
            'noplaylist': mt,  # all dictionary
            'logger': MyLogger(),  # options
            'progress_hooks': [durum],  # how can i find
        }
        #ydl_opts = {'outtmpl': str(f[0])}

        #ydl_opts = {'file_name.mp4'}
        #ydl_opts = {'outtmpl': 'file_name.mp4'}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([str(url_text)])

        self.progressBar.setValue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        #print'ok'
        self.QMessageBox.question(self,'dnvkjfvn','dknvkljdv')


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())