# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Interfaces\Tela_key.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Key(object):
    def setupUi(self, TelaApi):
        TelaApi.setObjectName("TelaApi")
        TelaApi.resize(782, 200)
        TelaApi.setMinimumSize(QtCore.QSize(539, 200))
        TelaApi.setMaximumSize(QtCore.QSize(16777215, 263))
        TelaApi.setStyleSheet("background-color: rgb(129, 135, 255);")
        self.centralwidget = QtWidgets.QWidget(TelaApi)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.apy_key = QtWidgets.QLineEdit(self.centralwidget)
        self.apy_key.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.apy_key.setFont(font)
        self.apy_key.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.apy_key.setInputMask("")
        self.apy_key.setText("API KEY")
        self.apy_key.setPlaceholderText("")
        self.apy_key.setClearButtonEnabled(True)
        self.apy_key.setObjectName("apy_key")
        self.verticalLayout.addWidget(self.apy_key)
        self.secret_key = QtWidgets.QLineEdit(self.centralwidget)
        self.secret_key.setMinimumSize(QtCore.QSize(30, 35))
        self.secret_key.setMaximumSize(QtCore.QSize(2000, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.secret_key.setFont(font)
        self.secret_key.setAutoFillBackground(False)
        self.secret_key.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.secret_key.setInputMethodHints(QtCore.Qt.ImhSensitiveData)
        self.secret_key.setText("SECRET KEY")
        self.secret_key.setClearButtonEnabled(True)
        self.secret_key.setObjectName("secret_key")
        self.verticalLayout.addWidget(self.secret_key)
        self.botao_config = QtWidgets.QPushButton(self.centralwidget)
        self.botao_config.setMinimumSize(QtCore.QSize(203, 37))
        self.botao_config.setMaximumSize(QtCore.QSize(234, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.botao_config.setFont(font)
        self.botao_config.setStyleSheet("background-color: rgb(53, 218, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"")
        self.botao_config.setObjectName("botao_config")
        self.verticalLayout.addWidget(self.botao_config, 0, QtCore.Qt.AlignHCenter)
        self.msg_erro = QtWidgets.QLabel(self.centralwidget)
        self.msg_erro.setMinimumSize(QtCore.QSize(64, 44))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.msg_erro.setFont(font)
        self.msg_erro.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.msg_erro.setText("")
        self.msg_erro.setObjectName("msg_erro")
        self.verticalLayout.addWidget(self.msg_erro)
        TelaApi.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TelaApi)
        self.statusbar.setObjectName("statusbar")
        TelaApi.setStatusBar(self.statusbar)

        self.retranslateUi(TelaApi)
        QtCore.QMetaObject.connectSlotsByName(TelaApi)

    def retranslateUi(self, TelaApi):
        _translate = QtCore.QCoreApplication.translate
        TelaApi.setWindowTitle(_translate("TelaApi", "MainWindow"))
        self.botao_config.setText(_translate("TelaApi", "Configurar API_Key"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaApi = QtWidgets.QMainWindow()
    ui = Ui_TelaApi()
    ui.setupUi(TelaApi)
    TelaApi.show()
    sys.exit(app.exec_())
