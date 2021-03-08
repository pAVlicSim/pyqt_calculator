from _decimal import setcontext
from decimal import Decimal, DivisionByZero, InvalidOperation, Context, getcontext

from PyQt5 import QtWidgets

import my_form_calculator


def calculation_multiplication_division(action: str, number_1: str, number_2: str):
    result = 0
    if action == '×':
        result = Decimal(number_1.replace(',', '.')) * Decimal(number_2.replace(',', '.'))
    elif action == '÷':
        result = Decimal(number_1.replace(',', '.')) / Decimal(number_2.replace(',', '.'))
    return result


def calculation_addition_subtraction(action: str, number_1: str, number_2: str):
    result = 0
    if action == '+':
        result = Decimal(number_1.replace(',', '.')) + Decimal(number_2.replace(',', '.'))
    elif action == '-':
        result = Decimal(number_1.replace(',', '.')) - Decimal(number_2.replace(',', '.'))
    return result


class MyWindow(QtWidgets.QFrame, my_form_calculator.Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        self.setupUi(self)

        self.result = ''
        self.edit_1 = []
        self.numberButton = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']
        self.actionButton = [' + ', ' - ', ' × ', ' ÷ ']
        self.full_edit = []
        self.full_calculation_list = []

        self.my_context = Context(prec=35, flags=[], traps=[InvalidOperation, DivisionByZero])
        setcontext(self.my_context)

        self.pushButton_0.clicked.connect(lambda: self.continuous_input('0'))
        self.pushButton_1.clicked.connect(lambda: self.continuous_input('1'))
        self.pushButton_2.clicked.connect(lambda: self.continuous_input('2'))
        self.pushButton_3.clicked.connect(lambda: self.continuous_input('3'))
        self.pushButton_4.clicked.connect(lambda: self.continuous_input('4'))
        self.pushButton_5.clicked.connect(lambda: self.continuous_input('5'))
        self.pushButton_6.clicked.connect(lambda: self.continuous_input('6'))
        self.pushButton_7.clicked.connect(lambda: self.continuous_input('7'))
        self.pushButton_8.clicked.connect(lambda: self.continuous_input('8'))
        self.pushButton_9.clicked.connect(lambda: self.continuous_input('9'))
        self.pushButton_comma.clicked.connect(lambda: self.continuous_input(','))
        self.pushButton_plus_minus.clicked.connect(lambda: self.continuous_input('±'))

        self.pushButton_root.clicked.connect(lambda: self.continuous_input(' √ '))
        self.pushButton_plus.clicked.connect(lambda: self.continuous_input(' + '))
        self.pushButton_minus.clicked.connect(lambda: self.continuous_input(' - '))
        self.pushButton_divide.clicked.connect(lambda: self.continuous_input(' ÷ '))
        self.pushButton_multiply.clicked.connect(lambda: self.continuous_input(' × '))
        self.pushButton_degree.clicked.connect(lambda: self.continuous_input(' xⁿ '))

        self.pushButton_result.clicked.connect(self.processing_list_multiplication_division)
        self.pushButton_clear_all.clicked.connect(self.clear_edit_all)
        self.pushButton_clear_one.clicked.connect(self.lineEdit_clear)

    def continuous_input(self, symbol):
        if symbol in self.actionButton or symbol in self.numberButton:
            self.lineEdit_1.insert(symbol)
            self.full_edit = str(self.lineEdit_1.text()).split()
            print(self.full_edit)
        elif symbol == '±':
            self.lineEdit_1.insert('-')
            self.full_edit = str(self.lineEdit_1.text()).split()
            print(self.full_edit)
        elif self.lineEdit_1.isModified():
            self.full_edit = str(self.lineEdit_1.text()).split()
            print(self.full_edit)

    def processing_list_multiplication_division(self):
        self.lineEdit_1.setCursorPosition(len(self.lineEdit_1.text()))
        try:
            while '×' in self.full_edit or '÷' in self.full_edit:
                for i in range(len(self.full_edit)):
                    if self.full_edit[i] == '×' or self.full_edit[i] == '÷':
                        self.full_edit[i] = str(
                            calculation_multiplication_division(self.full_edit[i], self.full_edit[i - 1],
                                                                self.full_edit[i + 1])).replace('.', ',')
                        self.full_edit.pop(i - 1)
                        self.full_edit.pop(i)
                        print('после processing_list:', self.full_edit)
                        break
        except DivisionByZero:
            self.continuous_input(' ')
            QtWidgets.QMessageBox.information(window, "Ошибка ввода.", "Делить на ноль нельзя!",
                                              buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
        except(InvalidOperation, IndexError):
            QtWidgets.QMessageBox.information(window, "Ошибка ввода.", "Вы ощиблись при вводе!\nБудьте внимательнее!",
                                              buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            self.processing_list_addition_subtraction()

    def processing_list_addition_subtraction(self):
        try:
            while '+' in self.full_edit or '-' in self.full_edit:
                for i in range(len(self.full_edit)):
                    if self.full_edit[i] == '+' or self.full_edit[i] == '-':
                        self.full_edit[i] = str(
                            calculation_addition_subtraction(self.full_edit[i], self.full_edit[i - 1],
                                                             self.full_edit[i + 1])).replace('.', ',')
                        self.full_edit.pop(i - 1)
                        self.full_edit.pop(i)
                        print('после processing_list:', self.full_edit)
                        break
        except (IndexError, InvalidOperation):
            QtWidgets.QMessageBox.information(window, "Ошибка ввода.", "Вы ощиблись при вводе!\nБудьте внимательнее!",
                                              buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            self.calculation_result()

    def calculation_result(self):
        result = str(self.full_edit[0])
        if result != "None":
            self.lineEdit_1.insert(' = ' + str(result).replace('.', ','))
            self.textEdit_result.append(self.lineEdit_1.text())
            self.lineEdit_1.clear()
        else:
            pass

    def lineEdit_clear(self):
        self.full_edit.clear()
        self.lineEdit_1.backspace()
        self.full_edit = str(self.lineEdit_1.text()).split()
        print(self.full_edit)

    def clear_edit_all(self):
        self.textEdit_result.clear()
        self.lineEdit_1.clear()
        self.full_edit.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()  # Создаем экземпляр класса
    window.setWindowTitle("Калькулятор")
    window.setStyleSheet(open('my_style.qss', 'r').read())
    window.show()  # Отображаем окно
    sys.exit(app.exec())  # Запускаем цикл обработки событий
