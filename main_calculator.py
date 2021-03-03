from _decimal import setcontext
from decimal import Decimal, DivisionByZero, InvalidOperation, Context, getcontext

from PyQt5 import QtWidgets
import my_form_calculator


def calculation_processing_list(action: str, number_1: str, number_2: str):
    try:
        result = 0
        if action == '×':
            result = Decimal(number_1.replace(',', '.')) * Decimal(number_2.replace(',', '.'))
        elif action == '÷':
            result = Decimal(number_1.replace(',', '.')) / Decimal(number_2.replace(',', '.'))
        return result
    except DivisionByZero:
        QtWidgets.QMessageBox.information(window, "Ошибка ввода.", "Делить на ноль нельзя!",
                                          buttons=QtWidgets.QMessageBox.Close,
                                          defaultButton=QtWidgets.QMessageBox.Close)
    except (IndexError, InvalidOperation):
        QtWidgets.QMessageBox.information(window, "Ошибка ввода.", "Вы ощиблись при вводе!\nБудьте внимательнее!",
                                          buttons=QtWidgets.QMessageBox.Close,
                                          defaultButton=QtWidgets.QMessageBox.Close)


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

        self.my_context = Context(prec=15, flags=[], traps=[InvalidOperation, DivisionByZero])
        setcontext(self.my_context)
        print(getcontext())

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

        self.pushButton_result.clicked.connect(self.processing_list)
        # self.pushButton_clear.clicked.connect(self.clear_edit_all)

    def continuous_input(self, symbol):
        if symbol in self.actionButton or symbol in self.numberButton:
            self.edit_1.append(symbol)
            self.lineEdit_1.setText(str(''.join(self.edit_1)))
            self.full_edit = str(self.lineEdit_1.text()).split()
        elif symbol == '±':
            self.edit_1.append('-')
            self.lineEdit_1.setText(str(''.join(self.edit_1)))
            self.full_edit = str(self.lineEdit_1.text()).split()

    def processing_list(self):
        try:
            while '×' and '÷' in self.full_edit:
                for i in range(len(self.full_edit)):
                    if self.full_edit[i] == '×' or self.full_edit[i] == '÷':
                        calculation_processing_list(self.full_edit[i], self.full_edit[i - 1], self.full_edit[i + 1])
                        self.full_edit[i] = str(calculation_processing_list(self.full_edit[i], self.full_edit[i - 1],
                                                                            self.full_edit[i + 1])).replace('.', ',')
                        self.full_edit.pop(i - 1)
                        self.full_edit.pop(i)
                        print('после преобразования', self.full_edit)
        except IndexError:
            pass
        self.calculation_result()

    def calculation_result(self):
        try:
            # print(self.full_edit)
            result = Decimal(str(self.full_edit.pop(0)).replace(',', '.'))
            # print(result)
            for i in range(len(self.full_edit)):
                if i % 2 == 0:
                    step_list = self.full_edit[i: i + 2]
                    if step_list[0] == '+':
                        result += Decimal(str(step_list[1]).replace(',', '.'))
                    elif step_list[0] == '-':
                        result -= Decimal(str(step_list[1]).replace(',', '.'))
                    elif step_list[0] == '×':
                        result *= Decimal(str(step_list[1]).replace(',', '.'))
                    elif step_list[0] == '÷':
                        result /= Decimal(str(step_list[1]).replace(',', '.'))
            print(result)
            print(getcontext())
            self.lineEdit_1.insert(' = ' + str(result).replace('.', ','))
            self.clear_edit_all()
        except (IndexError, InvalidOperation):
            pass
        except DivisionByZero:
            print('Делить на ноль нельзя!!!')

    # def input_result(self, result: Decimal):
    #     self.lineEdit_result.setText(str(result).replace('.', ','))

    def full_calculation(self):
        pass

    def clear_edit_all(self):
        self.textEdit_result.append(self.lineEdit_1.text())
        self.lineEdit_1.clear()
        self.edit_1.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()  # Создаем экземпляр класса
    window.setWindowTitle("Калькулятор")
    window.setStyleSheet(open('my_style.qss', 'r').read())
    window.show()  # Отображаем окно
    sys.exit(app.exec())  # Запускаем цикл обработки событий
