# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Interfaces\Tela_saldo.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Balance(object):
    def setupUi(self, tela_erro):
        tela_erro.setObjectName("tela_erro")
        tela_erro.resize(438, 821)
        tela_erro.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(tela_erro)
        self.centralwidget.setStyleSheet("background-color: rgb(192, 192, 192);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setStyleSheet("background-color: rgb(128, 128, 128);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridvalor = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridvalor.setContentsMargins(0, 0, 0, 0)
        self.gridvalor.setObjectName("gridvalor")
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setStyleSheet("background-color:rgb(248, 248, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridvalor.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.splitter)
        tela_erro.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(tela_erro)
        self.statusbar.setObjectName("statusbar")
        tela_erro.setStatusBar(self.statusbar)

        self.retranslateUi(tela_erro)
        QtCore.QMetaObject.connectSlotsByName(tela_erro)

    def retranslateUi(self, tela_erro):
        _translate = QtCore.QCoreApplication.translate
        tela_erro.setWindowTitle(_translate("tela_erro", "MainWindow"))
        self.label.setText(_translate("tela_erro", "Saldos Ativos em sua conta Binance"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    tela_erro = QtWidgets.QMainWindow()
    ui = Ui_tela_erro()
    ui.setupUi(tela_erro)
    tela_erro.show()
    sys.exit(app.exec_())
