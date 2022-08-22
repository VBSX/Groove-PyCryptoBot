# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_admin.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Admin(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(590, 597)
        MainWindow.setStyleSheet(u"background-color: rgb(129, 135, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.botao_deslogar = QPushButton(self.centralwidget)
        self.botao_deslogar.setObjectName(u"botao_deslogar")
        self.botao_deslogar.setGeometry(QRect(0, 0, 91, 21))
        font = QFont()
        font.setPointSize(13)
        self.botao_deslogar.setFont(font)
        self.botao_deslogar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"color: rgb(255, 0, 0);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 40, 201, 31))
        font1 = QFont()
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.botao_cadastrar = QPushButton(self.centralwidget)
        self.botao_cadastrar.setObjectName(u"botao_cadastrar")
        self.botao_cadastrar.setGeometry(QRect(10, 120, 161, 31))
        self.botao_cadastrar.setFont(font)
        self.botao_cadastrar.setStyleSheet(u"background-color: rgb(53, 218, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"color: rgb(0, 0, 0);")
        self.nome_user = QLabel(self.centralwidget)
        self.nome_user.setObjectName(u"nome_user")
        self.nome_user.setGeometry(QRect(210, 40, 231, 31))
        self.nome_user.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.botao_deslogar.setText(QCoreApplication.translate("MainWindow", u"Deslogar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Seja Bem Vindo!", None))
        self.botao_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar usu\u00e1rio", None))
        self.nome_user.setText("")
    # retranslateUi

