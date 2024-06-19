# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Modify.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_ModifyPal(object):
    def setupUi(self, ModifyPal):
        if not ModifyPal.objectName():
            ModifyPal.setObjectName(u"ModifyPal")
        ModifyPal.resize(390, 303)
        ModifyPal.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.236422 rgba(28, 33, 44, 255), stop:0.760383 rgba(41, 48, 60, 255));")
        self.iconPalName = QLabel(ModifyPal)
        self.iconPalName.setObjectName(u"iconPalName")
        self.iconPalName.setGeometry(QRect(20, 20, 16, 16))
        self.iconPalName.setPixmap(QPixmap("assets/pal.svg"))
        self.iconPalName.setScaledContents(True)
        self.labelPalName = QLabel(ModifyPal)
        self.labelPalName.setObjectName(u"labelPalName")
        self.labelPalName.setGeometry(QRect(40, 20, 81, 16))
        self.labelPalName.setStyleSheet(u"color: white;\n"
"    font-family: Arial, sans-serif; \n"
"    font-size: 12px;")
        self.lineEditPalName = QLineEdit(ModifyPal)
        self.lineEditPalName.setObjectName(u"lineEditPalName")
        self.lineEditPalName.setGeometry(QRect(130, 20, 230, 22))
        self.lineEditPalName.setStyleSheet(u"color: rgb(0, 188, 119);\n"
"    font-family: Arial, sans-serif; \n"
"    font-size: 12px;")
        self.lineEditPalName.setMaxLength(18)
        self.iconInstagram = QLabel(ModifyPal)
        self.iconInstagram.setObjectName(u"iconInstagram")
        self.iconInstagram.setGeometry(QRect(20, 60, 16, 16))
        self.iconInstagram.setPixmap(QPixmap("assets/instagram.svg"))
        self.iconInstagram.setScaledContents(True)
        self.labelInstagram = QLabel(ModifyPal)
        self.labelInstagram.setObjectName(u"labelInstagram")
        self.labelInstagram.setGeometry(QRect(40, 60, 81, 16))
        self.labelInstagram.setStyleSheet(u"color: white;\n"
"    font-family: Arial, sans-serif; \n"
"    font-size: 12px;")
        self.lineEditInstagram = QLineEdit(ModifyPal)
        self.lineEditInstagram.setObjectName(u"lineEditInstagram")
        self.lineEditInstagram.setGeometry(QRect(130, 60, 230, 22))
        self.lineEditInstagram.setStyleSheet(u"color: rgb(0, 188, 119);\n"
"    font-family: Arial, sans-serif; \n"
"    font-size: 12px;")
        self.lineEditInstagram.setMaxLength(18)
        self.iconTwitter = QLabel(ModifyPal)
        self.iconTwitter.setObjectName(u"iconTwitter")
        self.iconTwitter.setGeometry(QRect(20, 100, 16, 16))
        self.iconTwitter.setPixmap(QPixmap("assets/twitter.svg"))
        self.iconTwitter.setScaledContents(True)
        self.labelTwitter = QLabel(ModifyPal)
        self.labelTwitter.setObjectName(u"labelTwitter")
        self.labelTwitter.setGeometry(QRect(40, 100, 81, 16))
        self.labelTwitter.setStyleSheet(u"color: white;\n"
"    font-family: Arial, sans-serif; \n"
"    font-size: 12px;")
        self.lineEditTwitter = QLineEdit(ModifyPal)
        self.lineEditTwitter.setObjectName(u"lineEditTwitter")
        self.lineEditTwitter.setGeometry(QRect(130, 100, 230, 22))
        self.lineEditTwitter.setStyleSheet(u"color: rgb(0, 188, 119);\n"
"    font-family: Arial, sans-serif; \n"
"    font-size: 12px;")
        self.lineEditTwitter.setMaxLength(18)
        self.iconDiscord = QLabel(ModifyPal)
        self.iconDiscord.setObjectName(u"iconDiscord")
        self.iconDiscord.setGeometry(QRect(20, 140, 16, 16))
        self.iconDiscord.setPixmap(QPixmap("assets/discord.svg"))
        self.iconDiscord.setScaledContents(True)
        self.labelDiscord = QLabel(ModifyPal)
        self.labelDiscord.setObjectName(u"labelDiscord")
        self.labelDiscord.setGeometry(QRect(40, 140, 81, 16))
        self.labelDiscord.setStyleSheet(u"color: white;\n"
"    font-family: Arial, sans-serif; \n"
"    font-size: 12px;")
        self.lineEditDiscord = QLineEdit(ModifyPal)
        self.lineEditDiscord.setObjectName(u"lineEditDiscord")
        self.lineEditDiscord.setGeometry(QRect(130, 140, 230, 22))
        self.lineEditDiscord.setStyleSheet(u"color: rgb(0, 188, 119);\n"
"    font-family: Arial, sans-serif; \n"
"    font-size: 12px;")
        self.lineEditDiscord.setMaxLength(18)
        self.iconSteam = QLabel(ModifyPal)
        self.iconSteam.setObjectName(u"iconSteam")
        self.iconSteam.setGeometry(QRect(20, 180, 16, 16))
        self.iconSteam.setPixmap(QPixmap("assets/steam.svg"))
        self.iconSteam.setScaledContents(True)
        self.iconSteam.setWordWrap(True)
        self.labelSteam = QLabel(ModifyPal)
        self.labelSteam.setObjectName(u"labelSteam")
        self.labelSteam.setGeometry(QRect(40, 180, 81, 16))
        self.labelSteam.setStyleSheet(u"color: white;\n"
"    font-family: Arial, sans-serif; \n"
"    font-size: 12px;")
        self.lineEditSteam = QLineEdit(ModifyPal)
        self.lineEditSteam.setObjectName(u"lineEditSteam")
        self.lineEditSteam.setGeometry(QRect(130, 180, 230, 22))
        self.lineEditSteam.setStyleSheet(u"color: rgb(0, 188, 119);\n"
"    font-family: Arial, sans-serif; \n"
"    font-size: 12px;")
        self.lineEditSteam.setMaxLength(18)
        self.iconTelegram = QLabel(ModifyPal)
        self.iconTelegram.setObjectName(u"iconTelegram")
        self.iconTelegram.setGeometry(QRect(20, 220, 16, 16))
        self.iconTelegram.setPixmap(QPixmap("assets/telegram.svg"))
        self.iconTelegram.setScaledContents(True)
        self.iconTelegram.setWordWrap(True)
        self.labelTelegram = QLabel(ModifyPal)
        self.labelTelegram.setObjectName(u"labelTelegram")
        self.labelTelegram.setGeometry(QRect(40, 220, 81, 16))
        self.labelTelegram.setStyleSheet(u"color: white;\n"
"    font-family: Arial, sans-serif; \n"
"    font-size: 12px;")
        self.lineEditTelegram = QLineEdit(ModifyPal)
        self.lineEditTelegram.setObjectName(u"lineEditTelegram")
        self.lineEditTelegram.setGeometry(QRect(130, 220, 230, 22))
        self.lineEditTelegram.setStyleSheet(u"color: rgb(0, 188, 119);\n"
"    font-family: Arial, sans-serif; \n"
"    font-size: 12px;")
        self.lineEditTelegram.setMaxLength(18)
        self.buttonBox = QDialogButtonBox(ModifyPal)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(20, 260, 341, 32))
        self.buttonBox.setStyleSheet(u"QDialogButtonBox QPushButton {\n"
"    min-width: 80px;\n"
"    min-height: 30px;\n"
"	background-color: dark-yellow;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.retranslateUi(ModifyPal)

        QMetaObject.connectSlotsByName(ModifyPal)
    # setupUi

    def retranslateUi(self, ModifyPal):
        ModifyPal.setWindowTitle(QCoreApplication.translate("ModifyPal", u"Modify Pal", None))
        self.iconPalName.setText("")
        self.labelPalName.setText(QCoreApplication.translate("ModifyPal", u"Pal Name", None))
        self.lineEditPalName.setText("")
        self.labelInstagram.setText(QCoreApplication.translate("ModifyPal", u"Instagram", None))
        self.lineEditInstagram.setText("")
        self.labelTwitter.setText(QCoreApplication.translate("ModifyPal", u"Twitter/X", None))
        self.labelDiscord.setText(QCoreApplication.translate("ModifyPal", u"Discord", None))
        self.labelSteam.setText(QCoreApplication.translate("ModifyPal", u"Steam", None))
        self.labelTelegram.setText(QCoreApplication.translate("ModifyPal", u"Telegram", None))
    # retranslateUi

