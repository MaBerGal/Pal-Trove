# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Delete.ui'
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
    QLabel, QSizePolicy, QWidget)

class Ui_DeletePal(object):
    def setupUi(self, DeletePal):
        if not DeletePal.objectName():
            DeletePal.setObjectName(u"DeletePal")
        DeletePal.resize(297, 120)
        DeletePal.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.236422 rgba(28, 33, 44, 255), stop:0.760383 rgba(41, 48, 60, 255));")
        self.labelDeleteConfirmation = QLabel(DeletePal)
        self.labelDeleteConfirmation.setObjectName(u"labelDeleteConfirmation")
        self.labelDeleteConfirmation.setGeometry(QRect(20, 10, 261, 61))
        self.labelDeleteConfirmation.setStyleSheet(u"color: white;\n"
"    font-family: Arial, sans-serif; \n"
"    font-size: 14px;")
        self.labelDeleteConfirmation.setWordWrap(True)
        self.buttonBox = QDialogButtonBox(DeletePal)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(-20, 80, 341, 32))
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

        self.retranslateUi(DeletePal)

        QMetaObject.connectSlotsByName(DeletePal)
    # setupUi

    def retranslateUi(self, DeletePal):
        DeletePal.setWindowTitle(QCoreApplication.translate("DeletePal", u"Delete Pal", None))
        self.labelDeleteConfirmation.setText(QCoreApplication.translate("DeletePal", u"Are you sure you want to delete this pal?", None))
    # retranslateUi

