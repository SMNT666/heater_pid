# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(587, 435)
        self.verticalLayout_2 = QVBoxLayout(Widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.param_C_edit = QLineEdit(self.groupBox)
        self.param_C_edit.setObjectName(u"param_C_edit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.param_C_edit)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.param_L_edit = QLineEdit(self.groupBox)
        self.param_L_edit.setObjectName(u"param_L_edit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.param_L_edit)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.param_Ro_edit = QLineEdit(self.groupBox)
        self.param_Ro_edit.setObjectName(u"param_Ro_edit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.param_Ro_edit)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.param_T_edit = QLineEdit(self.groupBox)
        self.param_T_edit.setObjectName(u"param_T_edit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.param_T_edit)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCheckable(True)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.pushButton_4)

        self.param_Heater1_power = QLineEdit(self.groupBox_2)
        self.param_Heater1_power.setObjectName(u"param_Heater1_power")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.param_Heater1_power)

        self.pushButton_5 = QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCheckable(True)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.pushButton_5)

        self.lineEdit_6 = QLineEdit(self.groupBox_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lineEdit_6)

        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCheckable(True)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.pushButton_6)

        self.lineEdit_7 = QLineEdit(self.groupBox_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lineEdit_7)

        self.pushButton_7 = QPushButton(self.groupBox_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setCheckable(True)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.pushButton_7)

        self.lineEdit_8 = QLineEdit(self.groupBox_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lineEdit_8)

        self.pushButton_8 = QPushButton(self.groupBox_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setCheckable(True)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.pushButton_8)

        self.lineEdit_9 = QLineEdit(self.groupBox_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lineEdit_9)

        self.pushButton_9 = QPushButton(self.groupBox_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setCheckable(True)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.pushButton_9)

        self.lineEdit_10 = QLineEdit(self.groupBox_2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.lineEdit_10)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_3 = QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.pid_P_edit = QLineEdit(self.groupBox_3)
        self.pid_P_edit.setObjectName(u"pid_P_edit")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.pid_P_edit)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_7)

        self.pid_I_edit = QLineEdit(self.groupBox_3)
        self.pid_I_edit.setObjectName(u"pid_I_edit")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.pid_I_edit)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_8)

        self.pid_D_edit = QLineEdit(self.groupBox_3)
        self.pid_D_edit.setObjectName(u"pid_D_edit")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.pid_D_edit)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_9)

        self.pid_setPoint_edit = QLineEdit(self.groupBox_3)
        self.pid_setPoint_edit.setObjectName(u"pid_setPoint_edit")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.pid_setPoint_edit)


        self.horizontalLayout.addWidget(self.groupBox_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.groupBox.setTitle(QCoreApplication.translate("Widget", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0432\u043e\u0437\u0434\u0443\u0445\u0430", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u0421", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"L", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u03c1", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u0422", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"\u041d\u0430\u0433\u0440\u0435\u0432\u0430\u0442\u0435\u043b\u0438", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"1", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"2", None))
        self.pushButton_6.setText(QCoreApplication.translate("Widget", u"3", None))
        self.pushButton_7.setText(QCoreApplication.translate("Widget", u"4", None))
        self.pushButton_8.setText(QCoreApplication.translate("Widget", u"5", None))
        self.pushButton_9.setText(QCoreApplication.translate("Widget", u"6", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"\u041f\u0438\u0434", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"P", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"I", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"D", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"SETPOINT", None))
    # retranslateUi

