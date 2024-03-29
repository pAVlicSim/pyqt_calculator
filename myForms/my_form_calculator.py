# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_form_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox.setToolTipDuration(5000)
        self.comboBox.setEditable(False)
        self.comboBox.setMaxCount(20)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox.setMinimumContentsLength(4)
        self.comboBox.setFrame(True)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_6.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.pushButton_help = QtWidgets.QPushButton(Form)
        self.pushButton_help.setToolTipDuration(5000)
        self.pushButton_help.setObjectName("pushButton_help")
        self.horizontalLayout_6.addWidget(self.pushButton_help)
        self.pushButton_about = QtWidgets.QPushButton(Form)
        self.pushButton_about.setObjectName("pushButton_about")
        self.horizontalLayout_6.addWidget(self.pushButton_about)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.tableViewResult = QtWidgets.QTableView(Form)
        self.tableViewResult.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableViewResult.setToolTipDuration(5000)
        self.tableViewResult.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableViewResult.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableViewResult.setTabKeyNavigation(False)
        self.tableViewResult.setProperty("showDropIndicator", False)
        self.tableViewResult.setDragDropOverwriteMode(False)
        self.tableViewResult.setAlternatingRowColors(True)
        self.tableViewResult.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableViewResult.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableViewResult.setShowGrid(False)
        self.tableViewResult.setCornerButtonEnabled(False)
        self.tableViewResult.setObjectName("tableViewResult")
        self.tableViewResult.horizontalHeader().setVisible(False)
        self.tableViewResult.horizontalHeader().setHighlightSections(False)
        self.tableViewResult.verticalHeader().setVisible(False)
        self.tableViewResult.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.tableViewResult)
        self.lineEdit_1 = QtWidgets.QLineEdit(Form)
        self.lineEdit_1.setMouseTracking(False)
        self.lineEdit_1.setTabletTracking(False)
        self.lineEdit_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_1.setToolTipDuration(5000)
        self.lineEdit_1.setText("")
        self.lineEdit_1.setMaxLength(10000)
        self.lineEdit_1.setFrame(True)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_1.setPlaceholderText("")
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
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_5.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_8.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 6, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 4, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_9.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 3, 0, 1, 1)
        self.pushButton_clear_one = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_clear_one.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_clear_one.setToolTipDuration(5000)
        self.pushButton_clear_one.setAutoRepeat(True)
        self.pushButton_clear_one.setObjectName("pushButton_clear_one")
        self.gridLayout.addWidget(self.pushButton_clear_one, 2, 3, 1, 1)
        self.pushButton_clear_all = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_clear_all.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_clear_all.setToolTipDuration(5000)
        self.pushButton_clear_all.setObjectName("pushButton_clear_all")
        self.gridLayout.addWidget(self.pushButton_clear_all, 2, 0, 1, 1)
        self.pushButton_cursor_left = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_cursor_left.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_cursor_left.setToolTipDuration(5000)
        self.pushButton_cursor_left.setAutoRepeat(True)
        self.pushButton_cursor_left.setObjectName("pushButton_cursor_left")
        self.gridLayout.addWidget(self.pushButton_cursor_left, 2, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 2, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_1.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 6, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_7.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 3, 2, 1, 1)
        self.pushButton_cursor_right = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_cursor_right.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_cursor_right.setToolTipDuration(5000)
        self.pushButton_cursor_right.setAutoRepeat(True)
        self.pushButton_cursor_right.setObjectName("pushButton_cursor_right")
        self.gridLayout.addWidget(self.pushButton_cursor_right, 2, 2, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(self.frame_numbers)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.pushButtonTop0 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop0.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonTop0.setObjectName("pushButtonTop0")
        self.horizontalLayout_7.addWidget(self.pushButtonTop0)
        self.pushButtonTop1 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop1.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonTop1.setObjectName("pushButtonTop1")
        self.horizontalLayout_7.addWidget(self.pushButtonTop1)
        self.pushButtonTop2 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonTop2.setObjectName("pushButtonTop2")
        self.horizontalLayout_7.addWidget(self.pushButtonTop2)
        self.pushButtonTop3 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonTop3.setObjectName("pushButtonTop3")
        self.horizontalLayout_7.addWidget(self.pushButtonTop3)
        self.pushButtonTop4 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonTop4.setObjectName("pushButtonTop4")
        self.horizontalLayout_7.addWidget(self.pushButtonTop4)
        self.pushButtonTop5 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonTop5.setObjectName("pushButtonTop5")
        self.horizontalLayout_7.addWidget(self.pushButtonTop5)
        self.pushButtonTop6 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonTop6.setObjectName("pushButtonTop6")
        self.horizontalLayout_7.addWidget(self.pushButtonTop6)
        self.pushButtonTop7 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop7.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonTop7.setObjectName("pushButtonTop7")
        self.horizontalLayout_7.addWidget(self.pushButtonTop7)
        self.pushButtonTop8 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop8.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonTop8.setObjectName("pushButtonTop8")
        self.horizontalLayout_7.addWidget(self.pushButtonTop8)
        self.pushButtonTop9 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonTop9.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonTop9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonTop9.setObjectName("pushButtonTop9")
        self.horizontalLayout_7.addWidget(self.pushButtonTop9)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 6)
        self.pushButton_plus_minus = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_plus_minus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_plus_minus.setObjectName("pushButton_plus_minus")
        self.gridLayout.addWidget(self.pushButton_plus_minus, 8, 2, 1, 1)
        self.pushButton_comma = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_comma.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_comma.setObjectName("pushButton_comma")
        self.gridLayout.addWidget(self.pushButton_comma, 8, 1, 1, 1)
        self.pushButton_tg = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_tg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_tg.setObjectName("pushButton_tg")
        self.gridLayout.addWidget(self.pushButton_tg, 6, 5, 1, 1)
        self.pushButton_minus = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_minus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.gridLayout.addWidget(self.pushButton_minus, 4, 4, 1, 1)
        self.pushButton_divide = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_divide.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.gridLayout.addWidget(self.pushButton_divide, 8, 4, 1, 1)
        self.pushButton_cos = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_cos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_cos.setObjectName("pushButton_cos")
        self.gridLayout.addWidget(self.pushButton_cos, 4, 5, 1, 1)
        self.pushButton_plus = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_plus.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout.addWidget(self.pushButton_plus, 3, 4, 1, 1)
        self.pushButton_multiply = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_multiply.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.gridLayout.addWidget(self.pushButton_multiply, 6, 4, 1, 1)
        self.pushButton_ln = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_ln.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_ln.setObjectName("pushButton_ln")
        self.gridLayout.addWidget(self.pushButton_ln, 6, 6, 1, 1)
        self.pushButton_reverse = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_reverse.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_reverse.setObjectName("pushButton_reverse")
        self.gridLayout.addWidget(self.pushButton_reverse, 4, 7, 1, 1)
        self.pushButton_lg = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_lg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_lg.setObjectName("pushButton_lg")
        self.gridLayout.addWidget(self.pushButton_lg, 4, 6, 1, 1)
        self.pushButton_log = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_log.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_log.setObjectName("pushButton_log")
        self.gridLayout.addWidget(self.pushButton_log, 3, 6, 1, 1)
        self.pushButton_sin = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_sin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_sin.setObjectName("pushButton_sin")
        self.gridLayout.addWidget(self.pushButton_sin, 3, 5, 1, 1)
        self.pushButton_ctg = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_ctg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_ctg.setObjectName("pushButton_ctg")
        self.gridLayout.addWidget(self.pushButton_ctg, 8, 5, 1, 1)
        self.pushButton_result = QtWidgets.QPushButton(self.frame_numbers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_result.sizePolicy().hasHeightForWidth())
        self.pushButton_result.setSizePolicy(sizePolicy)
        self.pushButton_result.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_result.setToolTipDuration(5000)
        self.pushButton_result.setObjectName("pushButton_result")
        self.gridLayout.addWidget(self.pushButton_result, 6, 7, 3, 1)
        self.pushButton_leftBracket = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_leftBracket.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_leftBracket.setObjectName("pushButton_leftBracket")
        self.gridLayout.addWidget(self.pushButton_leftBracket, 3, 3, 1, 1)
        self.pushButton_rightBracket = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_rightBracket.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_rightBracket.setObjectName("pushButton_rightBracket")
        self.gridLayout.addWidget(self.pushButton_rightBracket, 4, 3, 1, 1)
        self.pushButton_percent = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_percent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_percent.setObjectName("pushButton_percent")
        self.gridLayout.addWidget(self.pushButton_percent, 3, 7, 1, 1)
        self.pushButton_root = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_root.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_root.setObjectName("pushButton_root")
        self.gridLayout.addWidget(self.pushButton_root, 6, 3, 1, 1)
        self.pushButton_0 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButton_0.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 8, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_2 = QtWidgets.QLabel(self.frame_numbers)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_8.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.pushButtonBottom0 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom0.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom0.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonBottom0.setObjectName("pushButtonBottom0")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom0)
        self.pushButtonBottom1 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom1.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonBottom1.setObjectName("pushButtonBottom1")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom1)
        self.pushButtonBottom2 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonBottom2.setObjectName("pushButtonBottom2")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom2)
        self.pushButtonBottom3 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonBottom3.setObjectName("pushButtonBottom3")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom3)
        self.pushButtonBottom4 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonBottom4.setObjectName("pushButtonBottom4")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom4)
        self.pushButtonBottom5 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonBottom5.setObjectName("pushButtonBottom5")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom5)
        self.pushButtonBottom6 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonBottom6.setObjectName("pushButtonBottom6")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom6)
        self.pushButtonBottom7 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom7.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonBottom7.setObjectName("pushButtonBottom7")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom7)
        self.pushButtonBottom8 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom8.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonBottom8.setObjectName("pushButtonBottom8")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom8)
        self.pushButtonBottom9 = QtWidgets.QPushButton(self.frame_numbers)
        self.pushButtonBottom9.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButtonBottom9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButtonBottom9.setObjectName("pushButtonBottom9")
        self.horizontalLayout_8.addWidget(self.pushButtonBottom9)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 6)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout_2.addWidget(self.frame_numbers)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Калькулятор"))
        Form.setAccessibleName(_translate("Form", "numButton"))
        self.label_3.setText(_translate("Form", "Количество знаков после запятой:"))
        self.comboBox.setToolTip(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                            "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style "
                                            "type=\"text/css\">\n "
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; "
                                            "font-weight:400; font-style:normal;\">\n "
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                            "text-indent:0px;\"><span style=\" font-size:16pt;\">Здесь "
                                            "настраивается</span></p>\n "
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                            "text-indent:0px;\"><span style=\" font-size:16pt;\">количество "
                                            "знаков</span></p>\n "
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                            "text-indent:0px;\"><span style=\" font-size:16pt;\">после "
                                            "запятой.</span></p>\n "
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                            "text-indent:0px;\"><span style=\" font-size:16pt;\">По умолчанию- "
                                            "четыре.</span></p>\n "
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; "
                                            "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                            "text-indent:0px;\"><span style=\" font-size:16pt;\">                     "
                                            "       </span></p></body></html>"))
        self.pushButton_help.setToolTip(_translate("Form",
                                                   "<html><head/><body><p align=\"center\"><span style=\" "
                                                   "font-size:16pt;\">Помощь по работе с</span></p><p "
                                                   "align=\"center\"><span style=\" "
                                                   "font-size:16pt;\">программой.</span></p></body></html>"))
        self.pushButton_help.setText(_translate("Form", "Помощь"))
        self.pushButton_about.setText(_translate("Form", "О программе"))
        self.tableViewResult.setToolTip(_translate("Form",
                                                   "<html><head/><body><p align=\"center\"><span style=\" "
                                                   "font-size:16pt;\">Здесь находятся примеры и результаты их "
                                                   "вычисления.</span></p><p align=\"center\"><span style=\" "
                                                   "font-size:16pt;\">При выделении результата, "
                                                   "он будет вставлен</span></p><p align=\"center\"><span style=\" "
                                                   "font-size:16pt;\">строку ввода. </span></p></body></html>"))
        self.lineEdit_1.setToolTip(_translate("Form",
                                              "<html><head/><body><p align=\"center\">Сюда вводятся данные</p><p "
                                              "align=\"center\">для расчёта.</p><p "
                                              "align=\"center\"><br/></p></body></html>"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_5.setAccessibleName(_translate("Form", "numButton"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_8.setAccessibleName(_translate("Form", "numButton"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_6.setAccessibleName(_translate("Form", "numButton"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_9.setText(_translate("Form", "9"))
        self.pushButton_clear_one.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span\n"
                                                                "style=\" font-size:14pt;\">Стирает символы в\n"
                                                                "строке ввода.</span></p></body></html>\n"))
        self.pushButton_clear_one.setText(_translate("Form", "⌫"))
        self.pushButton_clear_all.setToolTip(_translate("Form",
                                                        "<html><head/><body><p align=\"center\">Стирает все примеры и "
                                                        "</p><p align=\"center\">очищает строку ввода. "
                                                        "</p></body></html>"))
        self.pushButton_clear_all.setText(_translate("Form", "CA"))
        self.pushButton_cursor_left.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span\n"
                                                                  "style=\" font-size:14pt;\">Перемещает курсор\n"
                                                                  "на одну</span></p><p align=\"center\"><span\n"
                                                                  "style=\" font-size:14pt;\">позицию "
                                                                  "влево.</span></p></body></html>\n"))
        self.pushButton_cursor_left.setText(_translate("Form", "⮜"))
        self.pushButton_4.setAccessibleName(_translate("Form", "numButton"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_1.setText(_translate("Form", "1"))
        self.pushButton_7.setAccessibleName(_translate("Form", "numButton"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_cursor_right.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span\n"
                                                                   "style=\" font-size:14pt;\">Перемещает курсор\n"
                                                                   "на одну</span></p><p align=\"center\"><span\n"
                                                                   "style=\" font-size:14pt;\">позицию "
                                                                   "вправо.</span></p></body></html>\n"))
        self.pushButton_cursor_right.setText(_translate("Form", "⮞"))
        self.label.setText(_translate("Form", "Надстрочные цифры"))
        self.pushButtonTop0.setText(_translate("Form", "&0"))
        self.pushButtonTop1.setText(_translate("Form", "&1"))
        self.pushButtonTop2.setText(_translate("Form", "&2"))
        self.pushButtonTop3.setText(_translate("Form", "&3"))
        self.pushButtonTop4.setText(_translate("Form", "&4"))
        self.pushButtonTop5.setText(_translate("Form", "&5"))
        self.pushButtonTop6.setText(_translate("Form", "&6"))
        self.pushButtonTop7.setText(_translate("Form", "&7"))
        self.pushButtonTop8.setText(_translate("Form", "&8"))
        self.pushButtonTop9.setText(_translate("Form", "&9"))
        self.pushButton_plus_minus.setText(_translate("Form", "±"))
        self.pushButton_comma.setText(_translate("Form", ","))
        self.pushButton_tg.setText(_translate("Form", "&tg"))
        self.pushButton_minus.setText(_translate("Form", "−"))
        self.pushButton_divide.setText(_translate("Form", "÷"))
        self.pushButton_cos.setText(_translate("Form", "&cos"))
        self.pushButton_plus.setText(_translate("Form", "+"))
        self.pushButton_multiply.setText(_translate("Form", "×"))
        self.pushButton_ln.setText(_translate("Form", "l&n"))
        self.pushButton_reverse.setText(_translate("Form", "1/x"))
        self.pushButton_lg.setText(_translate("Form", "&lg"))
        self.pushButton_log.setText(_translate("Form", "l&og"))
        self.pushButton_sin.setText(_translate("Form", "&sin"))
        self.pushButton_ctg.setText(_translate("Form", "ct&g"))
        self.pushButton_result.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><span\n"
                                                             "style=\" font-size:14pt;\">Вычисляет\n"
                                                             "результат примера.</span></p></body></html>\n"))
        self.pushButton_result.setText(_translate("Form", "="))
        self.pushButton_leftBracket.setText(_translate("Form", "("))
        self.pushButton_rightBracket.setText(_translate("Form", ")"))
        self.pushButton_percent.setText(_translate("Form", "%"))
        self.pushButton_root.setText(_translate("Form", "√"))
        self.pushButton_0.setText(_translate("Form", "0"))
        self.label_2.setText(_translate("Form", "Подстрочные цифры"))
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
