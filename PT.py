# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PT.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
from PySide6.QtWidgets import QDialog, QDialogButtonBox, QLabel, QLineEdit, QMessageBox
from AddPal import Ui_AddPal
from Modify import Ui_ModifyPal
from Delete import Ui_DeletePal
from Database import Database
import webbrowser
from bs4 import BeautifulSoup

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 600)
        MainWindow.setMinimumSize(QSize(1000, 600))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        icon = QIcon(QIcon.fromTheme(u"face-raspberry"))
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.236422 rgba(28, 33, 44, 255), stop:0.760383 rgba(41, 48, 60, 255));")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.root = QFrame(self.centralwidget)
        self.root.setObjectName(u"root")
        self.root.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: none;")
        self.root.setFrameShape(QFrame.NoFrame)
        self.root.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.root)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QFrame(self.root)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMinimumSize(QSize(1000, 60))
        self.titleBar.setMaximumSize(QSize(1000, 60))
        self.titleBar.setFrameShape(QFrame.NoFrame)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titleBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.frame = QFrame(self.titleBar)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(250, 0))
        self.frame.setMaximumSize(QSize(250, 16777215))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.appName = QLabel(self.frame)
        self.appName.setObjectName(u"appName")

        self.horizontalLayout_3.addWidget(self.appName)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.titleBar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(300, 0))
        self.frame_2.setStyleSheet(u"border: none;\n"
"")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, 0)

        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.titleBar)

        self.container = QFrame(self.root)
        self.container.setObjectName(u"container")
        self.container.setMinimumSize(QSize(1000, 0))
        self.container.setMaximumSize(QSize(1000, 16777215))
        self.container.setFrameShape(QFrame.NoFrame)
        self.container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headers = QFrame(self.container)
        self.headers.setObjectName(u"headers")
        self.headers.setMaximumSize(QSize(16777215, 120))
        self.headers.setStyleSheet(u"")
        self.headers.setFrameShape(QFrame.NoFrame)
        self.headers.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.headers)
        self.horizontalLayout_5.setSpacing(30)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_4 = QSpacerItem(213, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.pushButton_6 = QPushButton(self.headers)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(50, 50))
        self.pushButton_6.setMaximumSize(QSize(50, 50))
        self.pushButton_6.setStyleSheet(u"border: 2px solid rgb(68, 204, 136);\n"
"border-radius: 25;\n"
"text-align: center;")
        icon1 = QIcon()
        icon1.addFile("assets/pal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setIconSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.pushButton_6)

        self.headerPal = QLabel(self.headers)
        self.headerPal.setObjectName(u"headerPal")
        self.headerPal.setMinimumSize(QSize(0, 0))
        self.headerPal.setMaximumSize(QSize(16666666, 16777215))

        self.horizontalLayout_5.addWidget(self.headerPal)

        self.horizontalSpacer_5 = QSpacerItem(213, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addWidget(self.headers)

        self.cards = QFrame(self.container)
        self.cards.setObjectName(u"cards")
        self.cards.setStyleSheet(u"")
        self.cards.setFrameShape(QFrame.NoFrame)
        self.cards.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.cards)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.card1 = QFrame(self.cards)
        self.card1.setObjectName(u"card1")
        self.card1.setMinimumSize(QSize(160, 210))
        self.card1.setMaximumSize(QSize(160, 210))
        self.card1.setStyleSheet(u"background-color: rgb(58, 65, 82);\n"
"border-radius: 15;")
        self.card1.setFrameShape(QFrame.NoFrame)
        self.card1.setFrameShadow(QFrame.Raised)
        self.card1.setLineWidth(5)
        self.verticalLayout_4 = QVBoxLayout(self.card1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.card1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 120))
        self.frame_4.setMaximumSize(QSize(150, 120))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButtonInstagram = QPushButton(self.frame_4)
        self.pushButtonInstagram.setObjectName(u"pushButtonInstagram")
        self.pushButtonInstagram.setMinimumSize(QSize(80, 80))
        self.pushButtonInstagram.setMaximumSize(QSize(80, 80))
        icon2 = QIcon()
        icon2.addFile("assets/instagram.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonInstagram.setIcon(icon2)
        self.pushButtonInstagram.setIconSize(QSize(70, 70))

        self.verticalLayout_3.addWidget(self.pushButtonInstagram, 0, Qt.AlignHCenter)

        self.labelInstagram = QLabel(self.frame_4)
        self.labelInstagram.setObjectName(u"labelInstagram")
        font = QFont()
        font.setBold(True)
        self.labelInstagram.setFont(font)

        self.verticalLayout_3.addWidget(self.labelInstagram, 0, Qt.AlignHCenter)

        self.labelInfo1 = QLabel(self.frame_4)
        self.labelInfo1.setObjectName(u"labelInfo1")
        font1 = QFont()
        font1.setPointSize(8)
        self.labelInfo1.setFont(font1)
        self.labelInfo1.setStyleSheet(u"text-align: center;")

        self.verticalLayout_3.addWidget(self.labelInfo1, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_7.addWidget(self.card1)

        self.card2 = QFrame(self.cards)
        self.card2.setObjectName(u"card2")
        self.card2.setMinimumSize(QSize(160, 210))
        self.card2.setMaximumSize(QSize(160, 210))
        self.card2.setStyleSheet(u"background-color: rgb(58, 65, 82);\n"
"border-radius: 15;")
        self.card2.setFrameShape(QFrame.NoFrame)
        self.card2.setFrameShadow(QFrame.Raised)
        self.card2.setLineWidth(5)
        self.verticalLayout_5 = QVBoxLayout(self.card2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.card2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(150, 120))
        self.frame_6.setMaximumSize(QSize(150, 120))
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButtonTwitter = QPushButton(self.frame_6)
        self.pushButtonTwitter.setObjectName(u"pushButtonTwitter")
        self.pushButtonTwitter.setMinimumSize(QSize(80, 80))
        self.pushButtonTwitter.setMaximumSize(QSize(80, 80))
        icon3 = QIcon()
        icon3.addFile("assets/twitter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonTwitter.setIcon(icon3)
        self.pushButtonTwitter.setIconSize(QSize(70, 70))

        self.verticalLayout_6.addWidget(self.pushButtonTwitter, 0, Qt.AlignHCenter)

        self.labelTwitter = QLabel(self.frame_6)
        self.labelTwitter.setObjectName(u"labelTwitter")
        self.labelTwitter.setFont(font)

        self.verticalLayout_6.addWidget(self.labelTwitter, 0, Qt.AlignHCenter)

        self.labelInfo2 = QLabel(self.frame_6)
        self.labelInfo2.setObjectName(u"labelInfo2")
        self.labelInfo2.setFont(font1)
        self.labelInfo2.setStyleSheet(u"text-align: center;")

        self.verticalLayout_6.addWidget(self.labelInfo2, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_7.addWidget(self.card2)

        self.card3 = QFrame(self.cards)
        self.card3.setObjectName(u"card3")
        self.card3.setMinimumSize(QSize(160, 210))
        self.card3.setMaximumSize(QSize(160, 210))
        self.card3.setStyleSheet(u"background-color: rgb(58, 65, 82);\n"
"border-radius: 15;")
        self.card3.setFrameShape(QFrame.NoFrame)
        self.card3.setFrameShadow(QFrame.Raised)
        self.card3.setLineWidth(5)
        self.verticalLayout_9 = QVBoxLayout(self.card3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.card3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(150, 120))
        self.frame_10.setMaximumSize(QSize(150, 120))
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButtonDiscord = QPushButton(self.frame_10)
        self.pushButtonDiscord.setObjectName(u"pushButtonDiscord")
        self.pushButtonDiscord.setMinimumSize(QSize(80, 80))
        self.pushButtonDiscord.setMaximumSize(QSize(80, 80))
        icon4 = QIcon()
        icon4.addFile("assets/discord.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonDiscord.setIcon(icon4)
        self.pushButtonDiscord.setIconSize(QSize(60, 60))

        self.verticalLayout_10.addWidget(self.pushButtonDiscord, 0, Qt.AlignHCenter)

        self.labelDiscord = QLabel(self.frame_10)
        self.labelDiscord.setObjectName(u"labelDiscord")
        self.labelDiscord.setFont(font)

        self.verticalLayout_10.addWidget(self.labelDiscord, 0, Qt.AlignHCenter)

        self.labelInfo3 = QLabel(self.frame_10)
        self.labelInfo3.setObjectName(u"labelInfo3")
        self.labelInfo3.setFont(font1)
        self.labelInfo3.setStyleSheet(u"text-align: center;")

        self.verticalLayout_10.addWidget(self.labelInfo3, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.frame_10, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_7.addWidget(self.card3)

        self.card4 = QFrame(self.cards)
        self.card4.setObjectName(u"card4")
        self.card4.setMinimumSize(QSize(160, 210))
        self.card4.setMaximumSize(QSize(160, 210))
        self.card4.setStyleSheet(u"background-color: rgb(58, 65, 82);\n"
"border-radius: 15;")
        self.card4.setFrameShape(QFrame.NoFrame)
        self.card4.setFrameShadow(QFrame.Raised)
        self.card4.setLineWidth(5)
        self.verticalLayout_11 = QVBoxLayout(self.card4)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.card4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(150, 120))
        self.frame_12.setMaximumSize(QSize(150, 120))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButtonSteam = QPushButton(self.frame_12)
        self.pushButtonSteam.setObjectName(u"pushButtonSteam")
        self.pushButtonSteam.setMinimumSize(QSize(80, 80))
        self.pushButtonSteam.setMaximumSize(QSize(80, 80))
        icon5 = QIcon()
        icon5.addFile("assets/steam.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSteam.setIcon(icon5)
        self.pushButtonSteam.setIconSize(QSize(60, 60))

        self.verticalLayout_12.addWidget(self.pushButtonSteam, 0, Qt.AlignHCenter)

        self.labelSteam = QLabel(self.frame_12)
        self.labelSteam.setObjectName(u"labelSteam")
        self.labelSteam.setFont(font)

        self.verticalLayout_12.addWidget(self.labelSteam, 0, Qt.AlignHCenter)

        self.labelInfo4 = QLabel(self.frame_12)
        self.labelInfo4.setObjectName(u"labelInfo4")
        self.labelInfo4.setFont(font1)
        self.labelInfo4.setStyleSheet(u"text-align: center;")

        self.verticalLayout_12.addWidget(self.labelInfo4, 0, Qt.AlignHCenter)


        self.verticalLayout_11.addWidget(self.frame_12, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_7.addWidget(self.card4)

        self.card5 = QFrame(self.cards)
        self.card5.setObjectName(u"card5")
        self.card5.setMinimumSize(QSize(160, 210))
        self.card5.setMaximumSize(QSize(160, 210))
        self.card5.setStyleSheet(u"background-color: rgb(58, 65, 82);\n"
"border-radius: 15;")
        self.card5.setFrameShape(QFrame.NoFrame)
        self.card5.setFrameShadow(QFrame.Raised)
        self.card5.setLineWidth(5)
        self.verticalLayout_7 = QVBoxLayout(self.card5)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.card5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(150, 120))
        self.frame_8.setMaximumSize(QSize(150, 120))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButtonTelegram = QPushButton(self.frame_8)
        self.pushButtonTelegram.setObjectName(u"pushButtonTelegram")
        self.pushButtonTelegram.setMinimumSize(QSize(80, 80))
        self.pushButtonTelegram.setMaximumSize(QSize(80, 80))
        icon6 = QIcon()
        icon6.addFile("assets/telegram.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonTelegram.setIcon(icon6)
        self.pushButtonTelegram.setIconSize(QSize(70, 70))

        self.verticalLayout_8.addWidget(self.pushButtonTelegram, 0, Qt.AlignHCenter)

        self.labelInfoTelegram = QLabel(self.frame_8)
        self.labelInfoTelegram.setObjectName(u"labelInfoTelegram")
        self.labelInfoTelegram.setFont(font)

        self.verticalLayout_8.addWidget(self.labelInfoTelegram, 0, Qt.AlignHCenter)

        self.labelInfo5 = QLabel(self.frame_8)
        self.labelInfo5.setObjectName(u"labelInfo5")
        self.labelInfo5.setFont(font1)
        self.labelInfo5.setStyleSheet(u"text-align: center;")

        self.verticalLayout_8.addWidget(self.labelInfo5, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_8, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_7.addWidget(self.card5)


        self.verticalLayout_2.addWidget(self.cards)

        self.buttons = QFrame(self.container)
        self.buttons.setObjectName(u"buttons")
        self.buttons.setMaximumSize(QSize(16777215, 150))
        self.buttons.setStyleSheet(u"")
        self.buttons.setFrameShape(QFrame.NoFrame)
        self.buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.buttons)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(20, -1, 20, -1)
        self.numberPals = QLabel(self.buttons)
        self.numberPals.setObjectName(u"numberPals")

        self.horizontalLayout_8.addWidget(self.numberPals)

        self.horizontalSpacer_10 = QSpacerItem(170, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)

        self.pushButtonFirst = QPushButton(self.buttons)
        self.pushButtonFirst.setObjectName(u"pushButtonFirst")
        self.pushButtonFirst.setMinimumSize(QSize(46, 46))
        self.pushButtonFirst.setMaximumSize(QSize(150, 46))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButtonFirst.setFont(font2)
        self.pushButtonFirst.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(68, 204, 136);\n"
"	border: none;\n"
"	border-radius: 23;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(59, 173, 116);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(51, 150, 101);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButtonFirst)

        self.pushButtonPrevious = QPushButton(self.buttons)
        self.pushButtonPrevious.setObjectName(u"pushButtonPrevious")
        self.pushButtonPrevious.setMinimumSize(QSize(46, 46))
        self.pushButtonPrevious.setMaximumSize(QSize(150, 46))
        self.pushButtonPrevious.setFont(font2)
        self.pushButtonPrevious.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(68, 204, 136);\n"
"	border: none;\n"
"	border-radius: 23;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(59, 173, 116);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(51, 150, 101);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButtonPrevious)

        self.pushButtonAdd = QPushButton(self.buttons)
        self.pushButtonAdd.setObjectName(u"pushButtonAdd")
        self.pushButtonAdd.setMinimumSize(QSize(150, 46))
        self.pushButtonAdd.setMaximumSize(QSize(150, 46))
        self.pushButtonAdd.setFont(font2)
        self.pushButtonAdd.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(68, 204, 136);\n"
"	border: none;\n"
"	border-radius: 23;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(59, 173, 116);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(51, 150, 101);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButtonAdd)

        self.pushButtonNext = QPushButton(self.buttons)
        self.pushButtonNext.setObjectName(u"pushButtonNext")
        self.pushButtonNext.setMinimumSize(QSize(46, 46))
        self.pushButtonNext.setMaximumSize(QSize(150, 46))
        self.pushButtonNext.setFont(font2)
        self.pushButtonNext.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(68, 204, 136);\n"
"	border: none;\n"
"	border-radius: 23;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(59, 173, 116);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(51, 150, 101);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButtonNext)

        self.pushButtonLast = QPushButton(self.buttons)
        self.pushButtonLast.setObjectName(u"pushButtonLast")
        self.pushButtonLast.setMinimumSize(QSize(46, 46))
        self.pushButtonLast.setMaximumSize(QSize(150, 46))
        self.pushButtonLast.setFont(font2)
        self.pushButtonLast.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(68, 204, 136);\n"
"	border: none;\n"
"	border-radius: 23;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(59, 173, 116);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(51, 150, 101);\n"
"}")

        self.horizontalLayout_8.addWidget(self.pushButtonLast)

        self.horizontalSpacer_9 = QSpacerItem(170, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.pushButtonModify = QPushButton(self.buttons)
        self.pushButtonModify.setObjectName(u"pushButtonModify")
        self.pushButtonModify.setMinimumSize(QSize(30, 30))
        self.pushButtonModify.setMaximumSize(QSize(200, 30))
        self.pushButtonModify.setFont(font)
        self.pushButtonModify.setStyleSheet(u"QPushButton {\n"
"	border-radius: 15;\n"
"	background-color: rgb(230, 230, 0);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(79, 93, 116);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile("assets/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonModify.setIcon(icon7)
        self.pushButtonModify.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.pushButtonModify)

        self.pushButtonDelete = QPushButton(self.buttons)
        self.pushButtonDelete.setObjectName(u"pushButtonDelete")
        self.pushButtonDelete.setMinimumSize(QSize(30, 30))
        self.pushButtonDelete.setMaximumSize(QSize(200, 30))
        self.pushButtonDelete.setFont(font)
        self.pushButtonDelete.setAutoFillBackground(False)
        self.pushButtonDelete.setStyleSheet(u"QPushButton {\n"
"	border-radius: 15;\n"
"	background-color: rgb(230, 0, 0);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(79, 93, 116);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        icon8 = QIcon()
        icon8.addFile("assets/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonDelete.setIcon(icon8)
        self.pushButtonDelete.setIconSize(QSize(20, 20))

        self.horizontalLayout_8.addWidget(self.pushButtonDelete)


        self.verticalLayout_2.addWidget(self.buttons)


        self.verticalLayout.addWidget(self.container)


        self.horizontalLayout.addWidget(self.root)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        #############################
        #############################
        #############################
        ########## MY CODE ##########
        #############################
        #############################
        #############################

        # Database initialization
        self.db = Database("pals.db")
        self.db.create_table()

        self.currentIndex = 0
        self.load_pal_data(self.currentIndex)

        self.pushButtonFirst.clicked.connect(self.navigate_first)
        self.pushButtonPrevious.clicked.connect(self.navigate_previous)
        self.pushButtonNext.clicked.connect(self.navigate_next)
        self.pushButtonLast.clicked.connect(self.navigate_last)

        self.pushButtonAdd.clicked.connect(self.add_button_clicked)
        self.pushButtonModify.clicked.connect(self.modify_button_clicked)
        self.pushButtonDelete.clicked.connect(self.delete_button_clicked)

        # Connect each button to the card_button_clicked method
        self.pushButtonInstagram.clicked.connect(lambda: self.card_button_clicked(self.labelInfo1.text(), "Instagram"))
        self.pushButtonTwitter.clicked.connect(lambda: self.card_button_clicked(self.labelInfo2.text(), "Twitter"))
        self.pushButtonDiscord.clicked.connect(lambda: self.card_button_clicked(self.labelInfo3.text(), "Discord"))
        self.pushButtonSteam.clicked.connect(lambda: self.card_button_clicked(self.labelInfo4.text(), "Steam"))
        self.pushButtonTelegram.clicked.connect(lambda: self.card_button_clicked(self.labelInfo5.text(), "Telegram"))

        # Create an instance of AddPal dialog
        self.add_pal_dialog = QDialog()
        self.ui_add_pal = Ui_AddPal()
        self.ui_add_pal.setupUi(self.add_pal_dialog)

    def load_pal_data(self, index):
            users = self.db.fetch_all_users()
            if users:
                    user = users[index]
                    palname = user[1]
                    instagram = user[2]
                    twitter = user[3]
                    discord = user[4]
                    steam = user[5]
                    telegram = user[6]

                    self.headerPal.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">This is </span>"
                                                                      f"<span style=\" font-size:24pt; font-weight:700; color:#44cc88;\">{palname}</span></p></body></html>",
                                                                      None))

                    self.set_header_text(self.headerPal, palname)
                    self.set_label_text(self.labelInfo1, instagram)
                    self.set_label_text(self.labelInfo2, twitter)
                    self.set_label_text(self.labelInfo3, discord)
                    self.set_label_text(self.labelInfo4, steam)
                    self.set_label_text(self.labelInfo5, telegram)
            else:
                    self.headerPal.setText(QCoreApplication.translate("MainWindow",
                                                                      f"<html><head/><body><p><span style=\"font-size:24pt; color:#ffffff;\">There are </span>"
                                                                      f"<span style=\"font-size:24pt; font-weight:700; color:#909090;\">no pals</span></p></body></html>",
                                                                      None))
                    self.labelInfo1.setText("");
                    self.labelInfo2.setText("");
                    self.labelInfo3.setText("");
                    self.labelInfo4.setText("");
                    self.labelInfo5.setText("");
            self.update_button_states()
            self.update_number_pals_label()

    def set_header_text(self, header, text):
            if text:
                    header.setText(QCoreApplication.translate("MainWindow",
                                                                      f"<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">This is </span>"
                                                                      f"<span style=\" font-size:24pt; font-weight:700; color:#44cc88;\">{text}</span></p></body></html>",
                                                                      None))
            else:
                    header.setText(QCoreApplication.translate("MainWindow",
                                                                      f"<html><head/><body><p><span style=\"font-size:24pt; color:#ffffff;\">This is </span>"
                                                                      f"<span style=\"font-size:24pt; font-weight:700; color:#909090;\">an unnamed pal</span></p></body></html>",
                                                                      None))

    def set_label_text(self, label, text):
            if text:
                    label.setText(QCoreApplication.translate("MainWindow",
                                                             f"<html><head/><body><p><span style=\" font-size:9pt; font-weight:700; color:#43c485;\">{text}</span></p></body></html>",
                                                             None))
            else:
                    label.setText(QCoreApplication.translate("MainWindow",
                                                             f"<html><head/><body><p><span style=\" font-size:9pt; font-weight:700; color:#909090;\">Not provided</span></p></body></html>",
                                                             None))

    def set_label_not_provided(self, label):
            label.setText(QCoreApplication.translate("MainWindow",
                                                     f"<html><head/><body><p><span style=\" font-size:9pt; font-weight:700; color:#909090;\">Not provided</span></p></body></html>",
                                                     None))

    def navigate_first(self):
            users = self.db.fetch_all_users()
            if users and self.currentIndex != 0:
                    self.currentIndex = 0
                    self.load_pal_data(self.currentIndex)
                    self.update_number_pals_label()

    def navigate_previous(self):
            users = self.db.fetch_all_users()
            if users and self.currentIndex > 0:
                    self.currentIndex -= 1
                    self.load_pal_data(self.currentIndex)
                    self.update_number_pals_label()

    def navigate_next(self):
            users = self.db.fetch_all_users()
            if users and self.currentIndex < len(users) - 1:
                    self.currentIndex += 1
                    self.load_pal_data(self.currentIndex)
                    self.update_number_pals_label()

    def navigate_last(self):
            users = self.db.fetch_all_users()
            if users:
                    self.currentIndex = len(users) - 1
                    self.load_pal_data(self.currentIndex)
                    self.update_number_pals_label()

    def add_button_clicked(self, s):
            print("click", s)
            self.add_pal_dialog = QDialog()
            self.ui_add_pal = Ui_AddPal()
            self.ui_add_pal.setupUi(self.add_pal_dialog)

            # Connect button box signals
            self.ui_add_pal.buttonBox.accepted.connect(self.accept_add_pal)
            self.ui_add_pal.buttonBox.rejected.connect(self.add_pal_dialog.reject)

            self.add_pal_dialog.exec()

    def accept_add_pal(self):
            # Retrieve data from AddPal dialog
            palname = self.ui_add_pal.lineEditPalName.text()
            instagram = self.ui_add_pal.lineEditInstagram.text()
            twitter = self.ui_add_pal.lineEditTwitter.text()
            discord = self.ui_add_pal.lineEditDiscord.text()
            steam = self.ui_add_pal.lineEditSteam.text()
            telegram = self.ui_add_pal.lineEditTelegram.text()

            # Insert data into the database
            self.db.insert_user(palname, instagram, twitter, discord, steam, telegram)

            # Update currentIndex and load data for the newly added pal
            self.currentIndex = len(self.db.fetch_all_users()) - 1
            self.load_pal_data(self.currentIndex)
            self.update_number_pals_label()

            self.navigate_last()

            # Close the dialog
            self.add_pal_dialog.accept()

    def modify_button_clicked(self):
            users = self.db.fetch_all_users()
            if users:
                    current_user = users[self.currentIndex]
                    palname = current_user[1]
                    instagram = current_user[2]
                    twitter = current_user[3]
                    discord = current_user[4]
                    steam = current_user[5]
                    telegram = current_user[6]

                    self.modify_pal_dialog = QDialog()
                    self.ui_modify_pal = Ui_ModifyPal()
                    self.ui_modify_pal.setupUi(self.modify_pal_dialog)

                    # Initialize line edits with current pal's attributes
                    self.ui_modify_pal.lineEditPalName.setText(palname)
                    self.ui_modify_pal.lineEditInstagram.setText(instagram)
                    self.ui_modify_pal.lineEditTwitter.setText(twitter)
                    self.ui_modify_pal.lineEditDiscord.setText(discord)
                    self.ui_modify_pal.lineEditSteam.setText(steam)
                    self.ui_modify_pal.lineEditTelegram.setText(telegram)

                    # Connect button box signals
                    self.ui_modify_pal.buttonBox.accepted.connect(self.accept_modify_pal)
                    self.ui_modify_pal.buttonBox.rejected.connect(self.modify_pal_dialog.reject)

                    self.modify_pal_dialog.exec()
            else:
                    print("No users found in the database.")

    def accept_modify_pal(self):
            # Retrieve data from ModifyPal dialog
            new_palname = self.ui_modify_pal.lineEditPalName.text()
            new_instagram = self.ui_modify_pal.lineEditInstagram.text()
            new_twitter = self.ui_modify_pal.lineEditTwitter.text()
            new_discord = self.ui_modify_pal.lineEditDiscord.text()
            new_steam = self.ui_modify_pal.lineEditSteam.text()
            new_telegram = self.ui_modify_pal.lineEditTelegram.text()

            # Update data in the database
            users = self.db.fetch_all_users()
            if users:
                    current_user = users[self.currentIndex]
                    user_id = current_user[0]

                    # Call update_user method from Database class
                    self.db.update_user(user_id, new_palname, new_instagram, new_twitter, new_discord, new_steam,
                                        new_telegram)

                    # Reload updated data for the current pal
                    self.load_pal_data(self.currentIndex)
                    self.update_number_pals_label()
                    self.load_pal_data(self.currentIndex)
            else:
                    print("No users found in the database.")

            # Close the dialog
            self.modify_pal_dialog.accept()

    def delete_button_clicked(self):
            # Create a QDialog instance for delete confirmation
            self.delete_pal_dialog = QDialog()
            self.ui_delete_pal = Ui_DeletePal()
            self.ui_delete_pal.setupUi(self.delete_pal_dialog)

            # Connect button box signals
            self.ui_delete_pal.buttonBox.accepted.connect(self.accept_delete_pal)
            self.ui_delete_pal.buttonBox.rejected.connect(self.delete_pal_dialog.reject)

            # Execute the dialog
            self.delete_pal_dialog.exec()

    def accept_delete_pal(self):
            pal_id = self.get_current_pal_id()
            if pal_id is not None:
                    self.db.delete_user(pal_id)
                    print(f"Deleting current pal with ID {pal_id}...")

                    # Update the current index to the previous pal if possible
                    if self.currentIndex > 0:
                            self.currentIndex -= 1

                    # Reload the data to reflect the deletion
                    self.load_pal_data(self.currentIndex)
                    self.update_number_pals_label()

                    # Show a message box indicating deletion success
                    QMessageBox.information(self, "Delete Pal", "Pal deleted successfully.")

            else:
                    QMessageBox.warning(self, "Delete Pal", "No pal could be found for deletion.")

            # Close the delete dialog after deletion is confirmed
            self.delete_pal_dialog.accept()

    def get_current_pal_id(self):
            users = self.db.fetch_all_users()
            if users and 0 <= self.currentIndex < len(users):
                    current_user = users[self.currentIndex]
                    return current_user[0]
            return None

    def update_number_pals_label(self):
            users = self.db.fetch_all_users()
            if users:
                    total_pals = len(users) if users else 0
                    self.numberPals.setText(QCoreApplication.translate("MainWindow",
                                                                       f"<html><head/><body><p><span style=\"font-size:10pt; font-weight:700; color:#ffffff;\">"
                                                                       f"Pals: {self.currentIndex + 1}/{total_pals}</span></p></body></html>",
                                                                       None))
            else:
                    self.numberPals.setText(QCoreApplication.translate("MainWindow",
                                                                       f"<html><head/><body><p><span style=\"font-size:10pt; font-weight:700; color:#ffffff;\">"
                                                                       f"Pals: 0</span></p></body></html>",
                                                                       None))

    def update_button_states(self):
            users = self.db.fetch_all_users()

            # Enable/disable First and Previous buttons
            self.pushButtonFirst.setEnabled(self.currentIndex != 0)
            self.pushButtonPrevious.setEnabled(self.currentIndex != 0)

            # Enable/disable Next and Last buttons
            self.pushButtonNext.setEnabled(self.currentIndex < len(users) - 1)
            self.pushButtonLast.setEnabled(self.currentIndex < len(users) - 1)

            # Enable/disable Modify and Delete buttons based on data availability
            if users:
                    current_user = users[self.currentIndex]

                    # Check if each platform has data for the current user
                    has_instagram = bool(current_user[2])
                    has_twitter = bool(current_user[3])
                    has_discord = bool(current_user[4])
                    has_steam = bool(current_user[5])
                    has_telegram = bool(current_user[6])

                    # Enable or disable buttons based on data availability
                    self.pushButtonModify.setEnabled(True)
                    self.pushButtonDelete.setEnabled(True)

                    self.pushButtonInstagram.setEnabled(has_instagram)
                    self.pushButtonTwitter.setEnabled(has_twitter)
                    self.pushButtonDiscord.setEnabled(has_discord)
                    self.pushButtonSteam.setEnabled(has_steam)
                    self.pushButtonTelegram.setEnabled(has_telegram)

            else:
                    # Disable all buttons if there are no users
                    self.pushButtonModify.setEnabled(False)
                    self.pushButtonDelete.setEnabled(False)
                    self.pushButtonInstagram.setEnabled(False)
                    self.pushButtonTwitter.setEnabled(False)
                    self.pushButtonDiscord.setEnabled(False)
                    self.pushButtonSteam.setEnabled(False)
                    self.pushButtonTelegram.setEnabled(False)

    def card_button_clicked(self, text, platform):
            soup = BeautifulSoup(text, 'html.parser')
            plain_text = soup.get_text().strip()
            print("Button clicked with text:", plain_text)

            # Define the base URLs for each platform
            base_urls = {
                    "Instagram": "https://www.instagram.com/{}/",
                    "Twitter": "https://twitter.com/{}/",
                    "Discord": "https://discord.com/users/{}/",
                    "Steam": "https://steamcommunity.com/id/{}/",
                    "Telegram": "https://t.me/{}"
            }

            # Check if platform exists in base_urls
            if platform in base_urls:
                    url = base_urls[platform].format(plain_text)
                    print("Opening URL:", url)
                    # Open the URL in the default web browser
                    webbrowser.open(url)
            else:
                    print(f"Platform '{platform}' not found in base_urls.")

    def closeEvent(self, event):
            # Ensure database connection is closed on exit
            self.db.close_connection()
            event.accept()

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pal Trove", None))
        self.appName.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700; color:#ffffff;\">PT </span><span style=\" font-size:18pt; color:#ffffff;\">Pal Trove</span></p></body></html>", None))
        self.pushButton_6.setText("")
        self.headerPal.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">This is </span><span style=\" font-size:24pt; font-weight:700; color:#44cc88;\">pal</span></p></body></html>", None))
        self.pushButtonInstagram.setText("")
        self.labelInstagram.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#e3e3e3;\">Instagram</span></p></body></html>", None))
        self.labelInfo1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:700; color:#43c485;\">Amongu</span></p></body></html>", None))
        self.pushButtonTwitter.setText("")
        self.labelTwitter.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#e3e3e3;\">Twitter/X</span></p></body></html>", None))
        self.labelInfo2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:700; color:#909090;\">Not amongu</span></p></body></html>", None))
        self.pushButtonDiscord.setText("")
        self.labelDiscord.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#e3e3e3;\">Discord</span></p></body></html>", None))
        self.labelInfo3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:700; color:#43c485;\">Amongu</span></p></body></html>", None))
        self.pushButtonSteam.setText("")
        self.labelSteam.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#e3e3e3;\">Steam</span></p></body></html>", None))
        self.labelInfo4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:700; color:#43c485;\">Amongu</span></p></body></html>", None))
        self.pushButtonTelegram.setText("")
        self.labelInfoTelegram.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#e3e3e3;\">Telegram</span></p></body></html>", None))
        self.labelInfo5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt; font-weight:700; color:#43c485;\">Amongu</span></p></body></html>", None))
        self.numberPals.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700; color:#ffffff;\">Pals: ?</span></p></body></html>", None))
        self.pushButtonFirst.setText(QCoreApplication.translate("MainWindow", u"\u25c0\u25c0", None))
        self.pushButtonPrevious.setText(QCoreApplication.translate("MainWindow", u"\u25c0", None))
#if QT_CONFIG(tooltip)
        self.pushButtonAdd.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Add a new pal</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonAdd.setText(QCoreApplication.translate("MainWindow", u"Add Pal", None))
        self.pushButtonNext.setText(QCoreApplication.translate("MainWindow", u"\u25b6", None))
        self.pushButtonLast.setText(QCoreApplication.translate("MainWindow", u"\u25b6\u25b6", None))
#if QT_CONFIG(tooltip)
        self.pushButtonModify.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#fafafa;\">Modify this pal</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonModify.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonModify.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.pushButtonDelete.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Delete this pal</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonDelete.setText("")
#if QT_CONFIG(shortcut)
        self.pushButtonDelete.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

