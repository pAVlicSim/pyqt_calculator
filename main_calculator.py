from _decimal import setcontext
from decimal import Decimal, DivisionByZero, InvalidOperation, Context
from PyQt5 import QtWidgets, QtCore
import my_form_calculator


def calculation_degree(number: str, number_list: list):
    index_split = []
    for j in number_list:
        if j != -1:
            index_split.append(number.rfind(j))
    normal_number = number[:max(index_split) + 1]
    small_number = number[max(index_split) + 1:]
    for i in small_number:
        if i == '⁰':
            small_number = small_number.replace('⁰', '0')
        elif i == '¹':
            small_number = small_number.replace('¹', '1')
        elif i == '²':
            small_number = small_number.replace('²', '2')
        elif i == '³':
            small_number = small_number.replace('³', '3')
        elif i == '⁴':
            small_number = small_number.replace('⁴', '4')
        elif i == '⁵':
            small_number = small_number.replace('⁵', '5')
        elif i == '⁶':
            small_number = small_number.replace('⁶', '6')
        elif i == '⁷':
            small_number = small_number.replace('⁷', '7')
        elif i == '⁸':
            small_number = small_number.replace('⁸', '8')
        elif i == '⁹':
            small_number = small_number.replace('⁹', '9')
        print(normal_number, small_number)
    result = Decimal(normal_number.replace(',', '.')) ** Decimal(small_number.replace(',', '.'))
    print(result)
    return result


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


def calculation_root(numberRoot: str):
    numberRootList = numberRoot.split('√')
    print(numberRootList)
    for i in numberRootList[0]:
        if i == '⁰':
            numberRootList[0] = numberRootList[0].replace('⁰', '0')
        elif i == '¹':
            numberRootList[0] = numberRootList[0].replace('¹', '1')
        elif i == '²':
            numberRootList[0] = numberRootList[0].replace('²', '2')
        elif i == '³':
            numberRootList[0] = numberRootList[0].replace('³', '3')
        elif i == '⁴':
            numberRootList[0] = numberRootList[0].replace('⁴', '4')
        elif i == '⁵':
            numberRootList[0] = numberRootList[0].replace('⁵', '5')
        elif i == '⁶':
            numberRootList[0] = numberRootList[0].replace('⁶', '6')
        elif i == '⁷':
            numberRootList[0] = numberRootList[0].replace('⁷', '7')
        elif i == '⁸':
            numberRootList[0] = numberRootList[0].replace('⁸', '8')
        elif i == '⁹':
            numberRootList[0] = numberRootList[0].replace('⁹', '9')
    print(numberRootList)
    result = Decimal(numberRootList[1].replace(',', '.')) ** (1 / Decimal(numberRootList[0]))
    return result


class MyWindow(QtWidgets.QFrame, my_form_calculator.Ui_Form):  # главный класс
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        self.setupUi(self)

        self.numberButton = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']  # лист обычных цифр
        self.actionButton = [' + ', ' - ', ' × ', ' ÷ ', '√']  # лист математических символов
        self.small_numberButton = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']  # лист надстрочных цифр
        self.full_edit = []  # лист вводимых символов в lineEdit1
        self.full_calculation_list = []  # ещё не используется
        self.lineEdit_1.setFocus(QtCore.Qt.OtherFocusReason)  # настройка фокуса, от нажатия кнопок на окне программы

        self.my_context = Context(prec=35, flags=[], traps=[InvalidOperation, DivisionByZero])  # контекст для Decimal
        setcontext(self.my_context)  # подключение контекста

        # кнопки вводят символы через функцию continuous_input
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

        #
        self.pushButtonTop0.clicked.connect(lambda: self.continuous_input('⁰'))
        self.pushButtonTop1.clicked.connect(lambda: self.continuous_input('¹'))
        self.pushButtonTop2.clicked.connect(lambda: self.continuous_input('²'))
        self.pushButtonTop3.clicked.connect(lambda: self.continuous_input('³'))
        self.pushButtonTop4.clicked.connect(lambda: self.continuous_input('⁴'))
        self.pushButtonTop5.clicked.connect(lambda: self.continuous_input('⁵'))
        self.pushButtonTop6.clicked.connect(lambda: self.continuous_input('⁶'))
        self.pushButtonTop7.clicked.connect(lambda: self.continuous_input('⁷'))
        self.pushButtonTop8.clicked.connect(lambda: self.continuous_input('⁸'))
        self.pushButtonTop9.clicked.connect(lambda: self.continuous_input('⁹'))

        #
        self.pushButton_root.clicked.connect(lambda: self.continuous_input('√'))
        self.pushButton_plus.clicked.connect(lambda: self.continuous_input(' + '))
        self.pushButton_minus.clicked.connect(lambda: self.continuous_input(' - '))
        self.pushButton_divide.clicked.connect(lambda: self.continuous_input(' ÷ '))
        self.pushButton_multiply.clicked.connect(lambda: self.continuous_input(' × '))
        self.pushButton_degree.clicked.connect(lambda: self.continuous_input(' xⁿ '))

        self.pushButton_result.clicked.connect(self.processing_list_root)  # кнопка запуска расчёта
        self.pushButton_clear_all.clicked.connect(self.clear_edit_all)  # очищает все поля
        self.pushButton_clear_one.clicked.connect(self.lineEdit_clear)  # очищает один символ за нажатие

        # кнопки перемещения курсора
        self.pushButton_cursor_left.clicked.connect(self.cursor_left)
        self.pushButton_cursor_right.clicked.connect(self.cursor_right)

    # функция вводит символы в lineEdit1
    def continuous_input(self, symbol):  # символ передаётся при нажатии соответствующей кнопки
        if symbol in self.actionButton or symbol in self.numberButton or self.small_numberButton:  # если символ входит
            # в листы цифр и действий
            self.lineEdit_1.insert(symbol)  # символ вставляется в конец строки
            self.full_edit = str(self.lineEdit_1.text()).split()  # преобразование строки в лист по пробелам
            print(self.full_edit)  #
        elif symbol == '±':  # если нажата кнопка плюс-ьинус
            self.lineEdit_1.insert('-')  # вставляется знак отрицательного цисла
            self.full_edit = str(self.lineEdit_1.text()).split()  # преобразование строки в лист по пробелам
            print(self.full_edit)  #

    def processing_list_root(self):
        self.lineEdit_1.end(False)
        try:
            while range(len(self.full_edit)):
                for i in range(len(self.full_edit)):
                    if '√' in self.full_edit[i]:
                        self.full_edit[i] = str(calculation_root(self.full_edit[i])).replace('.', ',')
                break
            print('после преобразования root', self.full_edit)
            self.processing_list_degree()
        except InvalidOperation:
            pass

    def processing_list_degree(self):
        try:
            while range(len(self.full_edit)):
                for i in range(len(self.full_edit)):
                    if self.full_edit[i][0] in self.numberButton and self.full_edit[i][-1] in self.small_numberButton:
                        self.full_edit[i] = (str(calculation_degree(self.full_edit[i], self.numberButton)).
                                             replace('.', ','))
                break
            print('после преобразования degree', self.full_edit)
            self.processing_list_multiplication_division()
        except InvalidOperation:
            pass

    def processing_list_multiplication_division(self):
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
                        print('после processing_list addition:', self.full_edit)
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

    def cursor_left(self):
        self.lineEdit_1.cursorBackward(False, 1)
        self.lineEdit_1.setFocus(QtCore.Qt.OtherFocusReason)
        print(self.lineEdit_1.cursorPosition())

    #
    def cursor_right(self):
        self.lineEdit_1.cursorForward(False, 1)
        self.lineEdit_1.setFocus(QtCore.Qt.OtherFocusReason)
        print(self.lineEdit_1.cursorPosition())

    #
    def lineEdit_clear(self):
        self.full_edit.clear()
        self.lineEdit_1.backspace()
        self.full_edit = str(self.lineEdit_1.text()).split()
        print(self.full_edit)

    #
    def clear_edit_all(self):
        self.textEdit_result.clear()
        self.lineEdit_1.clear()
        self.full_edit.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()  # Создаем экземпляр класса
    window.setWindowTitle("Калькулятор")  #
    window.setStyleSheet(open('my_style.qss', 'r').read())  #
    window.show()  # Отображаем окно
    sys.exit(app.exec())  # Запускаем цикл обработки событий
