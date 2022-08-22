# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'segunda_tela.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_Home(object):
    def setupUi(self, Operacoes):
        if not Operacoes.objectName():
            Operacoes.setObjectName(u"Operacoes")
        Operacoes.resize(677, 713)
        Operacoes.setMinimumSize(QSize(677, 713))
        Operacoes.setMaximumSize(QSize(677, 713))
        Operacoes.setStyleSheet(u"")
        self.centralwidget = QWidget(Operacoes)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(677, 693))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 47))
        self.frame_2.setStyleSheet(u"background-color: rgb(53, 218, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 12, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(49, 0))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.nome_user = QLabel(self.frame_2)
        self.nome_user.setObjectName(u"nome_user")
        self.nome_user.setMinimumSize(QSize(168, 23))
        self.nome_user.setMaximumSize(QSize(278, 16777215))
        self.nome_user.setFont(font)
        self.nome_user.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.nome_user, 0, 1, 1, 1, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(89, 0))
        font1 = QFont()
        font1.setPointSize(13)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(129, 135, 255);")

        self.gridLayout_3.addWidget(self.pushButton, 0, 2, 1, 1)

        self.botao_api = QPushButton(self.frame_2)
        self.botao_api.setObjectName(u"botao_api")
        self.botao_api.setMinimumSize(QSize(104, 0))
        self.botao_api.setFont(font1)
        self.botao_api.setStyleSheet(u"background-color: rgb(129, 135, 255);")

        self.gridLayout_3.addWidget(self.botao_api, 0, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(129, 135, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_icone = QLabel(self.frame_4)
        self.label_icone.setObjectName(u"label_icone")
        self.label_icone.setMaximumSize(QSize(32, 16777215))
        self.label_icone.setPixmap(QPixmap(u"../imagens/carteira.png"))

        self.horizontalLayout_2.addWidget(self.label_icone)

        self.label_texto_instrucao = QLabel(self.frame_4)
        self.label_texto_instrucao.setObjectName(u"label_texto_instrucao")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_texto_instrucao.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_texto_instrucao)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.label_resultado = QLabel(self.frame_4)
        self.label_resultado.setObjectName(u"label_resultado")
        self.label_resultado.setMinimumSize(QSize(303, 0))

        self.verticalLayout_9.addWidget(self.label_resultado)

        self.botao_ver_saldo = QPushButton(self.frame_4)
        self.botao_ver_saldo.setObjectName(u"botao_ver_saldo")
        self.botao_ver_saldo.setMinimumSize(QSize(20, 34))
        self.botao_ver_saldo.setMaximumSize(QSize(1024, 33))
        self.botao_ver_saldo.setFont(font1)
        self.botao_ver_saldo.setStyleSheet(u"background-color: rgb(53, 218, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_9.addWidget(self.botao_ver_saldo)


        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_texto_instrucao_2 = QLabel(self.frame_5)
        self.label_texto_instrucao_2.setObjectName(u"label_texto_instrucao_2")

        self.verticalLayout_4.addWidget(self.label_texto_instrucao_2)

        self.botao_2 = QPushButton(self.frame_5)
        self.botao_2.setObjectName(u"botao_2")
        self.botao_2.setMaximumSize(QSize(1024, 34))
        self.botao_2.setFont(font1)
        self.botao_2.setStyleSheet(u"background-color: rgb(53, 218, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_4.addWidget(self.botao_2)


        self.gridLayout.addWidget(self.frame_5, 0, 1, 1, 1)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_texto_instrucao_3 = QLabel(self.frame_6)
        self.label_texto_instrucao_3.setObjectName(u"label_texto_instrucao_3")

        self.verticalLayout_5.addWidget(self.label_texto_instrucao_3)

        self.label_resultado_3 = QLabel(self.frame_6)
        self.label_resultado_3.setObjectName(u"label_resultado_3")

        self.verticalLayout_5.addWidget(self.label_resultado_3)

        self.label_icone_3 = QLabel(self.frame_6)
        self.label_icone_3.setObjectName(u"label_icone_3")

        self.verticalLayout_5.addWidget(self.label_icone_3)

        self.botao_3 = QPushButton(self.frame_6)
        self.botao_3.setObjectName(u"botao_3")
        self.botao_3.setMaximumSize(QSize(1024, 34))
        self.botao_3.setFont(font1)
        self.botao_3.setStyleSheet(u"background-color: rgb(53, 218, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.botao_3)


        self.gridLayout.addWidget(self.frame_6, 1, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_texto_instrucao_4 = QLabel(self.frame_7)
        self.label_texto_instrucao_4.setObjectName(u"label_texto_instrucao_4")

        self.verticalLayout_6.addWidget(self.label_texto_instrucao_4)

        self.label_resultado_4 = QLabel(self.frame_7)
        self.label_resultado_4.setObjectName(u"label_resultado_4")

        self.verticalLayout_6.addWidget(self.label_resultado_4)

        self.label_icone_4 = QLabel(self.frame_7)
        self.label_icone_4.setObjectName(u"label_icone_4")

        self.verticalLayout_6.addWidget(self.label_icone_4)

        self.botao_4 = QPushButton(self.frame_7)
        self.botao_4.setObjectName(u"botao_4")
        self.botao_4.setMaximumSize(QSize(1024, 34))
        self.botao_4.setFont(font1)
        self.botao_4.setStyleSheet(u"background-color: rgb(53, 218, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_6.addWidget(self.botao_4)


        self.gridLayout.addWidget(self.frame_7, 1, 1, 1, 1)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_texto_instrucao_5 = QLabel(self.frame_8)
        self.label_texto_instrucao_5.setObjectName(u"label_texto_instrucao_5")

        self.verticalLayout_7.addWidget(self.label_texto_instrucao_5)

        self.label_resultado_5 = QLabel(self.frame_8)
        self.label_resultado_5.setObjectName(u"label_resultado_5")

        self.verticalLayout_7.addWidget(self.label_resultado_5)

        self.label_icone_5 = QLabel(self.frame_8)
        self.label_icone_5.setObjectName(u"label_icone_5")

        self.verticalLayout_7.addWidget(self.label_icone_5)

        self.botao_5 = QPushButton(self.frame_8)
        self.botao_5.setObjectName(u"botao_5")
        self.botao_5.setMaximumSize(QSize(1024, 34))
        self.botao_5.setFont(font1)
        self.botao_5.setStyleSheet(u"background-color: rgb(53, 218, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_7.addWidget(self.botao_5)


        self.gridLayout.addWidget(self.frame_8, 2, 0, 1, 1)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_texto_instrucao_6 = QLabel(self.frame_9)
        self.label_texto_instrucao_6.setObjectName(u"label_texto_instrucao_6")

        self.verticalLayout_8.addWidget(self.label_texto_instrucao_6)

        self.label_resultado_6 = QLabel(self.frame_9)
        self.label_resultado_6.setObjectName(u"label_resultado_6")

        self.verticalLayout_8.addWidget(self.label_resultado_6)

        self.label_icone_6 = QLabel(self.frame_9)
        self.label_icone_6.setObjectName(u"label_icone_6")

        self.verticalLayout_8.addWidget(self.label_icone_6)

        self.botao_6 = QPushButton(self.frame_9)
        self.botao_6.setObjectName(u"botao_6")
        self.botao_6.setMaximumSize(QSize(1024, 34))
        self.botao_6.setFont(font1)
        self.botao_6.setStyleSheet(u"background-color: rgb(53, 218, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_8.addWidget(self.botao_6)


        self.gridLayout.addWidget(self.frame_9, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        Operacoes.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Operacoes)
        self.statusbar.setObjectName(u"statusbar")
        Operacoes.setStatusBar(self.statusbar)

        self.retranslateUi(Operacoes)

        QMetaObject.connectSlotsByName(Operacoes)
    # setupUi

    def retranslateUi(self, Operacoes):
        Operacoes.setWindowTitle(QCoreApplication.translate("Operacoes", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Operacoes", u"Seja Bem Vindo!", None))
        self.nome_user.setText("")
        self.pushButton.setText(QCoreApplication.translate("Operacoes", u"LOGOUT", None))
        self.botao_api.setText(QCoreApplication.translate("Operacoes", u"ADICIONAR API KEY", None))
        self.label_icone.setText("")
        self.label_texto_instrucao.setText(QCoreApplication.translate("Operacoes", u"Veja as criptos que voc\u00ea tem saldo ativo", None))
        self.label_resultado.setText("")
        self.botao_ver_saldo.setText(QCoreApplication.translate("Operacoes", u"Ver Saldo", None))
        self.label_texto_instrucao_2.setText(QCoreApplication.translate("Operacoes", u"TextLabel", None))
        self.botao_2.setText("")
        self.label_texto_instrucao_3.setText(QCoreApplication.translate("Operacoes", u"TextLabel", None))
        self.label_resultado_3.setText(QCoreApplication.translate("Operacoes", u"TextLabel", None))
        self.label_icone_3.setText(QCoreApplication.translate("Operacoes", u"TextLabel", None))
        self.botao_3.setText("")
        self.label_texto_instrucao_4.setText(QCoreApplication.translate("Operacoes", u"TextLabel", None))
        self.label_resultado_4.setText(QCoreApplication.translate("Operacoes", u"TextLabel", None))
        self.label_icone_4.setText(QCoreApplication.translate("Operacoes", u"TextLabel", None))
        self.botao_4.setText("")
        self.label_texto_instrucao_5.setText(QCoreApplication.translate("Operacoes", u"TextLabel", None))
        self.label_resultado_5.setText(QCoreApplication.translate("Operacoes", u"TextLabel", None))
        self.label_icone_5.setText(QCoreApplication.translate("Operacoes", u"TextLabel", None))
        self.botao_5.setText("")
        self.label_texto_instrucao_6.setText(QCoreApplication.translate("Operacoes", u"TextLabel", None))
        self.label_resultado_6.setText(QCoreApplication.translate("Operacoes", u"TextLabel", None))
        self.label_icone_6.setText(QCoreApplication.translate("Operacoes", u"TextLabel", None))
        self.botao_6.setText("")
    # retranslateUi

