from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMenu,QLineEdit
from PyQt5.QtCore import QCoreApplication,QTimer,QThread,pyqtSignal
import sys

def proxy():
    proxyapp = QApplication(sys.argv)
    ex = Ui()
    sys.exit(proxyapp.exec_())
