# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Interfaces\Tela_cadastro.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, TelaCadastro):
        TelaCadastro.setObjectName("TelaCadastro")
        TelaCadastro.resize(653, 261)
        TelaCadastro.setStyleSheet("background-color: rgb(129, 135, 255);")
        self.centralwidget = QtWidgets.QWidget(TelaCadastro)
        self.centralwidget.setObjectName("centralwidget")
        self.nome = QtWidgets.QLineEdit(self.centralwidget)
        self.nome.setGeometry(QtCore.QRect(10, 10, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.nome.setFont(font)
        self.nome.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.nome.setObjectName("nome")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 290, 471, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.botao_cadastro = QtWidgets.QPushButton(self.centralwidget)
        self.botao_cadastro.setGeometry(QtCore.QRect(480, 90, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.botao_cadastro.setFont(font)
        self.botao_cadastro.setStyleSheet("background-color: rgb(53, 218, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"")
        self.botao_cadastro.setObjectName("botao_cadastro")
        self.login = QtWidgets.QLineEdit(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(10, 70, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.login.setFont(font)
        self.login.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.login.setObjectName("login")
        self.senha = QtWidgets.QLineEdit(self.centralwidget)
        self.senha.setGeometry(QtCore.QRect(10, 130, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.senha.setFont(font)
        self.senha.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.senha.setObjectName("senha")
        self.confirmar_senha = QtWidgets.QLineEdit(self.centralwidget)
        self.confirmar_senha.setGeometry(QtCore.QRect(10, 190, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.confirmar_senha.setFont(font)
        self.confirmar_senha.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.confirmar_senha.setObjectName("confirmar_senha")
        self.erro = QtWidgets.QLabel(self.centralwidget)
        self.erro.setGeometry(QtCore.QRect(370, 30, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.erro.setFont(font)
        self.erro.setStyleSheet("color: rgb(255, 0, 0);")
        self.erro.setText("")
        self.erro.setObjectName("erro")
        self.cadastrado = QtWidgets.QLabel(self.centralwidget)
        self.cadastrado.setGeometry(QtCore.QRect(370, 200, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cadastrado.setFont(font)
        self.cadastrado.setStyleSheet("color: rgb(0, 0, 0);\n"
"")
        self.cadastrado.setObjectName("cadastrado")
        TelaCadastro.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TelaCadastro)
        self.statusbar.setObjectName("statusbar")
        TelaCadastro.setStatusBar(self.statusbar)

        self.retranslateUi(TelaCadastro)
        QtCore.QMetaObject.connectSlotsByName(TelaCadastro)

    def retranslateUi(self, TelaCadastro):
        _translate = QtCore.QCoreApplication.translate
        TelaCadastro.setWindowTitle(_translate("TelaCadastro", "MainWindow"))
        self.nome.setText(_translate("TelaCadastro", "Nome"))
        self.botao_cadastro.setText(_translate("TelaCadastro", "Cadastrar usuário"))
        self.login.setText(_translate("TelaCadastro", "Login"))
        self.senha.setText(_translate("TelaCadastro", "Senha"))
        self.confirmar_senha.setText(_translate("TelaCadastro", "Confirmação da senha"))
        self.cadastrado.setText(_translate("TelaCadastro", "Usuario cadastrado com sucesso"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TelaCadastro = QtWidgets.QMainWindow()
    ui = Ui_TelaCadastro()
    ui.setupUi(TelaCadastro)
    TelaCadastro.show()
    sys.exit(app.exec_())
