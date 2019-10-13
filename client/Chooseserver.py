# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooseserver.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget
import sys

class Ui_chooseserver(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 512)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.ip = QtWidgets.QLineEdit(Form)
        self.ip.setMinimumSize(QtCore.QSize(0, 31))
        self.ip.setObjectName("ip")
        self.horizontalLayout_2.addWidget(self.ip)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(22, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.port = QtWidgets.QLineEdit(Form)
        self.port.setMinimumSize(QtCore.QSize(0, 31))
        self.port.setObjectName("port")
        self.horizontalLayout.addWidget(self.port)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.test = QtWidgets.QPushButton(Form)
        self.test.setObjectName("test")
        self.gridLayout.addWidget(self.test, 3, 1, 1, 1)
        self.save = QtWidgets.QPushButton(Form)
        self.save.setObjectName("save")
        self.gridLayout.addWidget(self.save, 4, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #self.show()
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.5)
        self.ip.setGraphicsEffect(op)
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.5)
        self.port.setGraphicsEffect(op)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "共享工作站"))
        self.comboBox.setItemText(1, _translate("Form", "私有工作站"))
        self.label.setText(_translate("Form", "服务器地址"))
        self.label_2.setText(_translate("Form", "  端口"))
        self.test.setText(_translate("Form", "测试"))
        self.save.setText(_translate("Form", "保存"))


if __name__ == '__main__':  # 调试用启动器
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    loginapp = QApplication(sys.argv)
    ex = Ui_chooseserver()
    sys.exit(loginapp.exec_())