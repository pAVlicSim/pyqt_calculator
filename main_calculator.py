from decimal import Decimal

from PyQt5 import QtWidgets, QtCore
import my_form_calculator


def enter_plus_minus(edit_list: list, line_edit: QtWidgets.QLineEdit):
    if len(edit_list) == 0:
        edit_list.append('-')
        line_edit.setText(''.join(edit_list))
    elif edit_list[0] != '-':
        edit_list.insert(0, '-')
        line_edit.setText(''.join(edit_list))
    else:
        edit_list.pop(0)
        line_edit.setText(''.join(edit_list))


class MyWindow(QtWidgets.QFrame, my_form_calculator.Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        self.setupUi(self)

        self.result = ''
        self.edit_1 = []
        self.edit_2 = []
        self.numberButton = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']
        self.actionButton = [' +', ' -', ' ×', ' ÷', ' √', ' xⁿ']
        self.full_edit = []

        self.pushButton_0.clicked.connect(lambda: self.selecting_an_input_field('0'))
        self.pushButton_1.clicked.connect(lambda: self.selecting_an_input_field('1'))
        self.pushButton_2.clicked.connect(lambda: self.selecting_an_input_field('2'))
        self.pushButton_3.clicked.connect(lambda: self.selecting_an_input_field('3'))
        self.pushButton_4.clicked.connect(lambda: self.selecting_an_input_field('4'))
        self.pushButton_5.clicked.connect(lambda: self.selecting_an_input_field('5'))
        self.pushButton_6.clicked.connect(lambda: self.selecting_an_input_field('6'))
        self.pushButton_7.clicked.connect(lambda: self.selecting_an_input_field('7'))
        self.pushButton_8.clicked.connect(lambda: self.selecting_an_input_field('8'))
        self.pushButton_9.clicked.connect(lambda: self.selecting_an_input_field('9'))
        self.pushButton_comma.clicked.connect(lambda: self.selecting_an_input_field(','))
        self.pushButton_plus_minus.clicked.connect(lambda: self.selecting_an_input_field('±'))

        self.pushButton_root.clicked.connect(lambda: self.selecting_an_input_field(' √'))
        self.pushButton_plus.clicked.connect(lambda: self.selecting_an_input_field(' +'))
        self.pushButton_minus.clicked.connect(lambda: self.selecting_an_input_field(' -'))
        self.pushButton_divide.clicked.connect(lambda: self.selecting_an_input_field(' ÷'))
        self.pushButton_multiply.clicked.connect(lambda: self.selecting_an_input_field(' ×'))
        self.pushButton_degree.clicked.connect(lambda: self.selecting_an_input_field(' xⁿ'))

        self.pushButton_result.clicked.connect(self.calculation_result)
        self.pushButton_clear.clicked.connect(self.clear_edit_all)

    def selecting_an_input_field(self, symbol):
        if ((str(self.lineEdit_1.displayText())[-1:] in self.numberButton) or
                (str(self.lineEdit_1.displayText()[-1:]) == '0') or str(self.lineEdit_1.displayText()[-1:]) == '-'):
            if symbol in self.numberButton or symbol in self.actionButton:
                self.enter_edit_1(symbol)
            elif symbol == '±':
                enter_plus_minus(self.edit_1, self.lineEdit_1)
        else:
            if symbol in self.numberButton or symbol in self.actionButton:
                self.enter_edit_2(symbol)
            elif symbol == '±':
                enter_plus_minus(self.edit_2, self.lineEdit_2)
            elif str(self.lineEdit_2.displayText())[-2:] in self.actionButton:
                pass

    def enter_edit_1(self, symbol):
        self.edit_1.append(symbol)
        self.lineEdit_1.setText(''.join(self.edit_1))

    def enter_edit_2(self, symbol):
        self.edit_2.append(symbol)
        self.lineEdit_2.setText(''.join(self.edit_2))

    def calculation_result(self):
        if str(self.lineEdit_1.text())[-2:] == ' +':
            result = (Decimal(str(self.lineEdit_1.text()).replace(',', '.')[:-1]) +
                      Decimal(str(self.lineEdit_2.text()).replace(',', '.')))
            self.lineEdit_result.setText(str(result).replace('.', ','))
        elif str(self.lineEdit_1.text())[-2:] == ' -':
            result = (Decimal(str(self.lineEdit_1.text()).replace(',', '.')[:-1]) -
                      Decimal(str(self.lineEdit_2.text()).replace(',', '.')))
            self.lineEdit_result.setText(str(result).replace('.', ','))
        elif str(self.lineEdit_1.text())[-2:] == ' ÷':
            result = (Decimal(str(self.lineEdit_1.text()).replace(',', '.')[:-1]) /
                      Decimal(str(self.lineEdit_2.text()).replace(',', '.')))
            self.lineEdit_result.setText(str(result).replace('.', ','))
        elif str(self.lineEdit_1.text())[-2:] == ' ×':
            result = (Decimal(str(self.lineEdit_1.text()).replace(',', '.')[:-1]) *
                      Decimal(str(self.lineEdit_2.text()).replace(',', '.')))
            self.lineEdit_result.setText(str(result).replace('.', ','))
        elif str(self.lineEdit_1.text())[-2:] == ' √':
            result = (Decimal(str(self.lineEdit_1.text()).replace(',', '.')[:-1]) **
                      (Decimal('1') / Decimal(str(self.lineEdit_2.text()).replace(',', '.'))))
            self.lineEdit_result.setText(str(result).replace('.', ','))
        elif str(self.lineEdit_1.text())[-3:] == ' xⁿ':
            result = pow(Decimal(str(self.lineEdit_1.text()).replace(',', '.')[:-2]),
                         Decimal(str(self.lineEdit_2.text()).replace(',', '.')))
            self.lineEdit_result.setText(str(result).replace('.', ','))

    def clear_edit_all(self):
        self.lineEdit_1.setText('0')
        self.edit_1.clear()
        self.lineEdit_2.clear()
        self.edit_2.clear()
        self.lineEdit_result.clear()
        self.result = ''


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()  # Создаем экземпляр класса
    window.setWindowTitle("Калькулятор")
    window.setStyleSheet(open('my_style.qss', 'r').read())
    window.show()  # Отображаем окно
    sys.exit(app.exec())  # Запускаем цикл обработки событий
