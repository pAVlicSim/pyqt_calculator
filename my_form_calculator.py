# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_form_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(960, 388)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_result = QtWidgets.QTextEdit(Form)
        self.textEdit_result.setObjectName("textEdit_result")
        self.verticalLayout.addWidget(self.textEdit_result)
        self.lineEdit_1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_1.setMouseTracking(False)
        self.lineEdit_1.setTabletTracking(False)
        self.lineEdit_1.setText("")
        self.lineEdit_1.setMaxLength(10000)
        self.lineEdit_1.setFrame(False)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_1.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.verticalLayout.addWidget(self.lineEdit_1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_numbers = QtWidgets.QFrame(Form)
        self.frame_numbers.setObjectName("frame_numbers")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_numbers)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.pushButton_cursor_right = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_cursor_right.setAutoRepeat(True)
        self.pushButton_cursor_right.setObjectName("pushButton_cursor_right")
        self.gridLayout.addWidget(self.pushButton_cursor_right, 1, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)
        self.pushButton_plus_minus = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_plus_minus.setObjectName("pushButton_plus_minus")
        self.gridLayout.addWidget(self.pushButton_plus_minus, 2, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 3, 0, 1, 1)
        self.pushButton_clear_all = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_clear_all.setObjectName("pushButton_clear_all")
        self.gridLayout.addWidget(self.pushButton_clear_all, 1, 0, 1, 1)
        self.pushButton_cursor_left = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_cursor_left.setAutoRepeat(True)
        self.pushButton_cursor_left.setObjectName("pushButton_cursor_left")
        self.gridLayout.addWidget(self.pushButton_cursor_left, 1, 1, 1, 1)
        self.pushButton_clear_one = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_clear_one.setAutoRepeat(True)
        self.pushButton_clear_one.setObjectName("pushButton_clear_one")
        self.gridLayout.addWidget(self.pushButton_clear_one, 1, 3, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 4, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 2, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 4, 2, 1, 1)
        self.pushButton_comma = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_comma.setObjectName("pushButton_comma")
        self.gridLayout.addWidget(self.pushButton_comma, 3, 3, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 3, 2, 1, 1)
        self.pushButton_leftBracket = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_leftBracket.setObjectName("pushButton_leftBracket")
        self.gridLayout.addWidget(self.pushButton_leftBracket, 1, 4, 1, 1)
        self.pushButton_rightBracket = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_rightBracket.setObjectName("pushButton_rightBracket")
        self.gridLayout.addWidget(self.pushButton_rightBracket, 2, 4, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.frame_numbers)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.pushButtonTop0 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop0.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop0.setObjectName("pushButtonTop0")
        self.horizontalLayout_7.addWidget(self.pushButtonTop0)
        self.pushButtonTop1 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop1.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop1.setObjectName("pushButtonTop1")
        self.horizontalLayout_7.addWidget(self.pushButtonTop1)
        self.pushButtonTop2 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop2.setObjectName("pushButtonTop2")
        self.horizontalLayout_7.addWidget(self.pushButtonTop2)
        self.pushButtonTop3 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop3.setObjectName("pushButtonTop3")
        self.horizontalLayout_7.addWidget(self.pushButtonTop3)
        self.pushButtonTop4 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop4.setObjectName("pushButtonTop4")
        self.horizontalLayout_7.addWidget(self.pushButtonTop4)
        self.pushButtonTop5 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop5.setObjectName("pushButtonTop5")
        self.horizontalLayout_7.addWidget(self.pushButtonTop5)
        self.pushButtonTop6 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop6.setObjectName("pushButtonTop6")
        self.horizontalLayout_7.addWidget(self.pushButtonTop6)
        self.pushButtonTop7 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop7.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop7.setObjectName("pushButtonTop7")
        self.horizontalLayout_7.addWidget(self.pushButtonTop7)
        self.pushButtonTop8 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop8.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop8.setObjectName("pushButtonTop8")
        self.horizontalLayout_7.addWidget(self.pushButtonTop8)
        self.pushButtonTop9 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop9.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop9.setObjectName("pushButtonTop9")
        self.horizontalLayout_7.addWidget(self.pushButtonTop9)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.frame_numbers)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        self.pushButtonBottom0 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom0.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom0.setAutoRepeat(False)
        self.pushButtonBottom0.setObjectName("pushButtonBottom0")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom0)
        self.pushButtonBottom1 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom1.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom1.setObjectName("pushButtonBottom1")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom1)
        self.pushButtonBottom2 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom2.setObjectName("pushButtonBottom2")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom2)
        self.pushButtonBottom3 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom3.setObjectName("pushButtonBottom3")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom3)
        self.pushButtonBottom4 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom4.setObjectName("pushButtonBottom4")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom4)
        self.pushButtonBottom5 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom5.setObjectName("pushButtonBottom5")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom5)
        self.pushButtonBottom6 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom6.setObjectName("pushButtonBottom6")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom6)
        self.pushButtonBottom7 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom7.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom7.setObjectName("pushButtonBottom7")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom7)
        self.pushButtonBottom8 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom8.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom8.setObjectName("pushButtonBottom8")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom8)
        self.pushButtonBottom9 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom9.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom9.setObjectName("pushButtonBottom9")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom9)
        self.gridLayout.addLayout(self.horizontalLayout_8, 5, 0, 1, 5)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_2.addWidget(self.frame_numbers)
        self.tabWidget_actions = QtWidgets.QTabWidget(Form)
        self.tabWidget_actions.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_actions.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget_actions.setUsesScrollButtons(False)
        self.tabWidget_actions.setTabBarAutoHide(True)
        self.tabWidget_actions.setObjectName("tabWidget_actions")
        self.tab_arithmetic = QtWidgets.QWidget()
        self.tab_arithmetic.setObjectName("tab_arithmetic")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_arithmetic)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_divide = QtWidgets.QPushButton(self.tab_arithmetic)
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.gridLayout_2.addWidget(self.pushButton_divide, 0, 1, 1, 1)
        self.pushButton_result = QtWidgets.QPushButton(self.tab_arithmetic)
        self.pushButton_result.setObjectName("pushButton_result")
        self.gridLayout_2.addWidget(self.pushButton_result, 3, 3, 1, 1)
        self.pushButton_multiply = QtWidgets.QPushButton(self.tab_arithmetic)
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.gridLayout_2.addWidget(self.pushButton_multiply, 2, 1, 1, 1)
        self.pushButton_degree = QtWidgets.QPushButton(self.tab_arithmetic)
        self.pushButton_degree.setObjectName("pushButton_degree")
        self.gridLayout_2.addWidget(self.pushButton_degree, 3, 0, 1, 1)
        self.pushButton_percent = QtWidgets.QPushButton(self.tab_arithmetic)
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.gridLayout_2.addWidget(self.pushButton_percent, 0, 3, 1, 1)
        self.pushButton_root = QtWidgets.QPushButton(self.tab_arithmetic)
        self.pushButton_root.setObjectName("pushButton_root")
        self.gridLayout_2.addWidget(self.pushButton_root, 3, 1, 1, 1)
        self.pushButton_plus = QtWidgets.QPushButton(self.tab_arithmetic)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout_2.addWidget(self.pushButton_plus, 0, 0, 1, 1)
        self.pushButton_minus = QtWidgets.QPushButton(self.tab_arithmetic)
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.gridLayout_2.addWidget(self.pushButton_minus, 2, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_2)
        self.tabWidget_actions.addTab(self.tab_arithmetic, "")
        self.tab_engineering = QtWidgets.QWidget()
        self.tab_engineering.setObjectName("tab_engineering")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_engineering)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_3.addWidget(self.pushButton_15, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_3.addWidget(self.pushButton_18, 3, 1, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_3.addWidget(self.pushButton_17, 2, 1, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_3.addWidget(self.pushButton_10, 1, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_3.addWidget(self.pushButton_12, 3, 0, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_3.addWidget(self.pushButton_22, 1, 2, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_3.addWidget(self.pushButton_11, 2, 0, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_3.addWidget(self.pushButton_23, 2, 2, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_3.addWidget(self.pushButton_24, 3, 2, 1, 1)
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_3.addWidget(self.pushButton_21, 0, 2, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_3.addWidget(self.pushButton_16, 1, 1, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_3.addWidget(self.pushButton_27, 0, 3, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_3.addWidget(self.pushButton_30, 3, 3, 1, 1)
        self.pushButton_28 = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout_3.addWidget(self.pushButton_28, 1, 3, 1, 1)
        self.pushButton_29 = QtWidgets.QPushButton(self.tab_engineering)
        self.pushButton_29.setObjectName("pushButton_29")
        self.gridLayout_3.addWidget(self.pushButton_29, 2, 3, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_3)
        self.tabWidget_actions.addTab(self.tab_engineering, "")
        self.horizontalLayout_2.addWidget(self.tabWidget_actions)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        self.tabWidget_actions.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Калькулятор"))
        self.lineEdit_1.setPlaceholderText(_translate("Form", "0"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_cursor_right.setText(_translate("Form", "⮞"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_plus_minus.setText(_translate("Form", "±"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_clear_all.setText(_translate("Form", "CA"))
        self.pushButton_cursor_left.setText(_translate("Form", "⮜"))
        self.pushButton_clear_one.setText(_translate("Form", "⌫"))
        self.pushButton_0.setText(_translate("Form", "0"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_1.setText(_translate("Form", "1"))
        self.pushButton_comma.setText(_translate("Form", ","))
        self.pushButton_9.setText(_translate("Form", "9"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_leftBracket.setText(_translate("Form", "("))
        self.pushButton_rightBracket.setText(_translate("Form", ")"))
        self.label.setText(_translate("Form", "Надстр"))
        self.pushButtonTop0.setText(_translate("Form", "0"))
        self.pushButtonTop1.setText(_translate("Form", "1"))
        self.pushButtonTop2.setText(_translate("Form", "2"))
        self.pushButtonTop3.setText(_translate("Form", "3"))
        self.pushButtonTop4.setText(_translate("Form", "4"))
        self.pushButtonTop5.setText(_translate("Form", "5"))
        self.pushButtonTop6.setText(_translate("Form", "6"))
        self.pushButtonTop7.setText(_translate("Form", "7"))
        self.pushButtonTop8.setText(_translate("Form", "8"))
        self.pushButtonTop9.setText(_translate("Form", "9"))
        self.label_2.setText(_translate("Form", "Подстр"))
        self.pushButtonBottom0.setText(_translate("Form", "0"))
        self.pushButtonBottom1.setText(_translate("Form", "1"))
        self.pushButtonBottom2.setText(_translate("Form", "2"))
        self.pushButtonBottom3.setText(_translate("Form", "3"))
        self.pushButtonBottom4.setText(_translate("Form", "4"))
        self.pushButtonBottom5.setText(_translate("Form", "5"))
        self.pushButtonBottom6.setText(_translate("Form", "6"))
        self.pushButtonBottom7.setText(_translate("Form", "7"))
        self.pushButtonBottom8.setText(_translate("Form", "8"))
        self.pushButtonBottom9.setText(_translate("Form", "9"))
        self.pushButton_divide.setText(_translate("Form", "÷"))
        self.pushButton_result.setText(_translate("Form", "="))
        self.pushButton_multiply.setText(_translate("Form", "×"))
        self.pushButton_degree.setText(_translate("Form", "xⁿ"))
        self.pushButton_percent.setText(_translate("Form", "%"))
        self.pushButton_root.setText(_translate("Form", "ⁿ√x"))
        self.pushButton_plus.setText(_translate("Form", "+"))
        self.pushButton_minus.setText(_translate("Form", "−"))
        self.tabWidget_actions.setTabText(self.tabWidget_actions.indexOf(self.tab_arithmetic), _translate("Form", "Арифметика"))
        self.pushButton_15.setText(_translate("Form", "log"))
        self.pushButton.setText(_translate("Form", "sin"))
        self.pushButton_18.setText(_translate("Form", "PushButton"))
        self.pushButton_17.setText(_translate("Form", "1/x"))
        self.pushButton_10.setText(_translate("Form", "cos"))
        self.pushButton_12.setText(_translate("Form", "ctg"))
        self.pushButton_22.setText(_translate("Form", "PushButton"))
        self.pushButton_11.setText(_translate("Form", "tg"))
        self.pushButton_23.setText(_translate("Form", "PushButton"))
        self.pushButton_24.setText(_translate("Form", "PushButton"))
        self.pushButton_21.setText(_translate("Form", "PushButton"))
        self.pushButton_16.setText(_translate("Form", "ln"))
        self.pushButton_27.setText(_translate("Form", "PushButton"))
        self.pushButton_30.setText(_translate("Form", "PushButton"))
        self.pushButton_28.setText(_translate("Form", "PushButton"))
        self.pushButton_29.setText(_translate("Form", "PushButton"))
        self.tabWidget_actions.setTabText(self.tabWidget_actions.indexOf(self.tab_engineering), _translate("Form", "Инженерный"))
