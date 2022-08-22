# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tela_Inicial.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.setWindowModality(Qt.WindowModal)
        Login.setEnabled(True)
        Login.resize(784, 603)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QSize(784, 603))
        Login.setMaximumSize(QSize(1167, 603))
        Login.setStyleSheet(u"background-color: rgb(129, 135, 255);")
        self.verticalLayout_3 = QVBoxLayout(Login)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Login)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(35, 32))
        self.label.setPixmap(QPixmap(u"../imagens/usuario.png"))

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(Login)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(72, 0))
        self.lineEdit.setMaximumSize(QSize(1000, 40))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.lineEdit.setInputMethodHints(Qt.ImhNone)
        self.lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(32, 40))
        self.label_2.setPixmap(QPixmap(u"../imagens/senha.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(Login)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setMinimumSize(QSize(92, 0))
        self.lineEdit_2.setMaximumSize(QSize(1000, 40))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"border-width: 2px;")
        self.lineEdit_2.setInputMethodHints(Qt.ImhNone)
        self.lineEdit_2.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, -1, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.pushButton = QPushButton(Login)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(374, 42))
        self.pushButton.setMaximumSize(QSize(439, 45))
        font = QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(129, 135, 255);\n"
"border-radius: 15px;\n"
"border-style: outset;\n"
"\n"
"")
        self.pushButton.setAutoDefault(True)
        self.pushButton.setFlat(False)

        self.verticalLayout_2.addWidget(self.pushButton, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(Login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(656, 40))
        self.label_3.setMaximumSize(QSize(532, 41))
        font1 = QFont()
        font1.setPointSize(13)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.verticalLayout_2.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 79, 0, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(Login)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(231, 0))
        self.label_5.setMaximumSize(QSize(249, 30))
        self.label_5.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.botao_git = QToolButton(Login)
        self.botao_git.setObjectName(u"botao_git")
        self.botao_git.setMinimumSize(QSize(43, 38))
        icon = QIcon()
        icon.addFile(u"../imagens/github.png", QSize(), QIcon.Normal, QIcon.On)
        self.botao_git.setIcon(icon)
        self.botao_git.setIconSize(QSize(48, 48))

        self.horizontalLayout_3.addWidget(self.botao_git)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Login)

        self.pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Dialog", None))
        self.label.setText("")
        self.lineEdit.setText("")
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("Login", u"LOGAR", None))
        self.label_3.setText("")
        self.label_5.setText(QCoreApplication.translate("Login", u"Visite Meu Github", None))
        self.botao_git.setText(QCoreApplication.translate("Login", u"...", None))
    # retranslateUi

