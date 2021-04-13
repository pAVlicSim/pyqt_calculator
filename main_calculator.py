from _decimal import setcontext
from decimal import Decimal, DivisionByZero, InvalidOperation, Context

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QDesktopWidget

import my_form_calculator


def calculation_degree(number: str, small_number_list: list[str], number_list: list[str]):
    index_split = []
    number_dict = dict(zip(small_number_list, number_list))
    for split in number_list:
        if split != -1:
            index_split.append(number.rfind(split))
    normal_number = number[:max(index_split) + 1]
    small_number = number[max(index_split) + 1:]
    for i in small_number:
        for j in number_dict:
            if i == j:
                small_number = small_number.replace(i, number_dict[j])
    result = Decimal(normal_number.replace(',', '.')) ** Decimal(small_number.replace(',', '.'))
    return result


def calculation_multiplication_division(sub_full_edit: list[str]):
    result = 0
    if sub_full_edit[1] == '×':
        result = Decimal(sub_full_edit[0].replace(',', '.')) * Decimal(sub_full_edit[2].replace(',', '.'))
    elif sub_full_edit[1] == '÷':
        result = Decimal(sub_full_edit[0].replace(',', '.')) / Decimal(sub_full_edit[2].replace(',', '.'))
    return result


def calculation_addition_subtraction(sub_full_edit: list[str]):
    result = 0
    if sub_full_edit[1] == '+':
        result = Decimal(sub_full_edit[0].replace(',', '.')) + Decimal(sub_full_edit[2].replace(',', '.'))
    elif sub_full_edit[1] == '-':
        result = Decimal(sub_full_edit[0].replace(',', '.')) - Decimal(sub_full_edit[2].replace(',', '.'))
    return result


def calculation_root(numberRoot: str, small_list: list[str], normal_list: list[str]):
    numberRootList = numberRoot.split('√')
    number_dict = dict(zip(small_list, normal_list))
    for i in numberRootList[0]:
        for small_number in number_dict:
            if i == small_number:
                numberRootList[0] = numberRootList[0].replace(i, number_dict[small_number])
    result = Decimal(numberRootList[1].replace(',', '.')) ** (1 / Decimal(numberRootList[0]))
    return result


class MyWindow(QtWidgets.QFrame, my_form_calculator.Ui_Form):  # главный класс

    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        self.setupUi(self)

        self.number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']  # лист обычных цифр
        self.actionButton = [' + ', ' - ', ' × ', ' ÷ ', '√', '( ', ' )']  # лист математических символов
        self.small_number = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']  # лист надстрочных цифр
        self.full_edit = []  # лист вводимых символов в lineEdit1
        self.lineEdit_1.setFocus(QtCore.Qt.OtherFocusReason)  # настройка фокуса, от нажатия кнопок на окне программы
        self.prec_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '15', '20', '25']  # кортеж для comboBox
        self.prec = '000000'

        self.comboBox.addItems(self.prec_list)
        self.comboBox.setCurrentText(str(len(self.prec)))

        # контекст для Decimal
        self.my_context = Context(prec=25, flags=[], traps=[InvalidOperation, DivisionByZero])
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

        self.pushButton_root.clicked.connect(lambda: self.continuous_input('√'))
        self.pushButton_plus.clicked.connect(lambda: self.continuous_input(' + '))
        self.pushButton_minus.clicked.connect(lambda: self.continuous_input(' - '))
        self.pushButton_divide.clicked.connect(lambda: self.continuous_input(' ÷ '))
        self.pushButton_multiply.clicked.connect(lambda: self.continuous_input(' × '))
        self.pushButton_leftBracket.clicked.connect(lambda: self.continuous_input('( '))
        self.pushButton_rightBracket.clicked.connect(lambda: self.continuous_input(' )'))

        self.pushButton_result.clicked.connect(self.processing_list_bracket)  # кнопка запуска расчёта
        self.pushButton_clear_all.clicked.connect(self.clear_edit_all)  # очищает все поля
        self.pushButton_clear_one.clicked.connect(self.lineEdit_clear)  # очищает один символ за нажатие

        # кнопки перемещения курсора
        self.pushButton_cursor_left.clicked.connect(self.cursor_left)  # кнопка передвигает курсор влево
        self.pushButton_cursor_right.clicked.connect(self.cursor_right)  # кнопка передвигает курсор вправо

        self.comboBox.activated[str].connect(self.tincture_of_prec)

    def center(self):
        frame_geometry = self.frameGeometry()
        center_desktop = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_desktop)
        self.move(frame_geometry.topLeft())

    def tincture_of_prec(self):
        self.prec = '0' * int(self.comboBox.currentIndex() + 1)

    # функция вводит символы в lineEdit1
    def continuous_input(self, symbol):  # символ передаётся при нажатии соответствующей кнопки
        # если символ входит в листы цифр и действий
        if symbol in self.number or symbol in self.small_number or symbol in self.actionButton:
            self.lineEdit_1.insert(symbol)  # символ вставляется в конец строки
            self.full_edit = str(self.lineEdit_1.text()).split()  # преобразование строки в лист по пробелам
            print(self.full_edit)  #
        elif symbol == '±':  # если нажата кнопка плюс-минус
            self.lineEdit_1.insert('-')  # вставляется знак отрицательного числа
            self.full_edit = str(self.lineEdit_1.text()).split()  # преобразование строки в лист по пробелам
            print(self.full_edit)  #

    # преобразует full_edit убирая скобки
    def processing_list_bracket(self):
        left_bracket = '('  # левая скобка
        right_bracket = ')'  # правая скобка
        # если в full_edit есть скобки
        if (left_bracket in self.full_edit or right_bracket in self.full_edit and
                self.full_edit.count(left_bracket) == self.full_edit.count(right_bracket)):
            while left_bracket in self.full_edit or right_bracket in self.full_edit:  # цикл работает пока есть скобки
                for i in range(len(self.full_edit)):  # цикл обходит основной список по индексу
                    # если в срезе,между левой и правой скобок,нет скобок
                    if (left_bracket not in self.full_edit[i + 1: self.full_edit.index(right_bracket)] and
                            right_bracket not in self.full_edit[i + 1: self.full_edit.index(right_bracket)]):
                        # создаём новый список из среза
                        sub_full_edit = self.full_edit[i: self.full_edit.index(right_bracket) + 1]
                        del self.full_edit[i: self.full_edit.index(right_bracket)]  # удаляем срез из  основного списка
                        sub_full_edit.remove(left_bracket)  # удаляем из нового списка скобки
                        sub_full_edit.remove(right_bracket)  #
                        self.processing_list_root(sub_full_edit)  # считаем результат в новом списке
                        self.full_edit[i] = sub_full_edit[0]  # вставляем результат в основной список
                        break  # возвращаемся в начало цикла for искать следующую пару скобок
            self.processing_list_root(self.full_edit)  # когда все скобки убраны, запускаем расчёт основного списка
        else:  # если изначально в основном списке нет скобок
            self.processing_list_root(self.full_edit)  # запускаем расчёт основного списка

    # функция ищет объекты со знаком "корня" и отправляет их в метод для расчёта
    def processing_list_root(self, calc_list: list):
        self.lineEdit_1.end(False)  # перемещает курсор в конец строки
        try:  # перехват исключении
            while range(len(calc_list)):  # цикл будет исполнятся пока не дойдёт до конца списка
                for i in range(len(calc_list)):  # цикл перебирает full_edit по индексам
                    if '√' in calc_list[i]:  # если индекс содержит знак "корня", то
                        # меняем значение индекса на полученное в соответствующем методе
                        calc_list[i] = str(calculation_root(calc_list[i], self.small_number, self.number))
                break  # возвращаемся во в while
            print('после преобразования root', calc_list)
        except (InvalidOperation, IndexError):  # если возникает исключение показываем диалоговое окно
            QtWidgets.QMessageBox.information(window, "Ошибка ввода.", "Вы ошиблись при вводе!\nБудьте внимательнее!",
                                              buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
        else:  # если всё проходит хорошо идём дальше
            self.processing_list_degree(calc_list)

    # функция ищет объекты с возведением в степень
    def processing_list_degree(self, calc_list: list):
        try:  # перехват исключений
            while range(len(calc_list)):  # цикл исполняется пока не дойдёт до конца списка
                for i in range(len(calc_list)):  # цикл перебирает full_edit по индексам
                    # если в начале строки символ из numbersButton, а в конце символ из small_numbersButton
                    if calc_list[i][0] in self.number and calc_list[i][-1] in self.small_number:
                        # меняем значение индекса на полученное в соответствующем методе
                        calc_list[i] = str(calculation_degree(calc_list[i], self.small_number, self.number))
                break  # возвращаемся во в while
            print('после преобразования degree', calc_list)
        except (InvalidOperation, IndexError):  # если возникает исключение показываем диалоговое окно
            QtWidgets.QMessageBox.information(window, "Ошибка ввода.", "Вы ошиблись при вводе!\nБудьте внимательнее!",
                                              buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
        else:  # если всё проходит хорошо идём дальше
            self.processing_list_multiplication_division(calc_list)

    # эта функция проверяет есть ли в примере деление и умножение
    def processing_list_multiplication_division(self, calc_list: list):
        try:  # перехват исключений
            # цикл работает пока в full_edit есть '×' и '÷'
            while '×' in calc_list or '÷' in calc_list:
                for i in range(len(calc_list)):  # цикл перебирает full_edit по индексам
                    # если находит '×' или '÷'
                    if calc_list[i] == '×' or calc_list[i] == '÷':
                        # меняет значение этого индекса на вычисляемое в методе  calculation_multiplication_division
                        sub_full_edit = calc_list[i - 1: i + 2]
                        calc_list[i] = str(calculation_multiplication_division(sub_full_edit))
                        del calc_list[i + 1]
                        del calc_list[i - 1]
                        print('после processing_list:', calc_list)
                        break  # возвращаемся в начало цикла
        except DivisionByZero:  # если захочется делить на ноль
            # показываем окно об ошибке
            QtWidgets.QMessageBox.information(window, "Ошибка ввода.", "Делить на ноль нельзя!",
                                              buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
        except(InvalidOperation, IndexError):  # если ошибка синтаксиса
            # показываем окно об ошибке
            QtWidgets.QMessageBox.information(window, "Ошибка ввода.", "Вы ошиблись при вводе!\nБудьте внимательнее!",
                                              buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
        else:  # если всё проходит хорошо идём дальше
            self.processing_list_addition_subtraction(calc_list)

    # ну вот добрались до сложения и вычитания
    def processing_list_addition_subtraction(self, calc_list: list):
        try:  # перехват исключений
            # функция работает аналогично предыдущей
            while '+' in calc_list or '-' in calc_list:
                for i in range(len(calc_list)):  #
                    if calc_list[i] == '+' or calc_list[i] == '-':  #
                        sub_full_edit = calc_list[i - 1: i + 2]
                        print('1', sub_full_edit)
                        calc_list[i] = str(calculation_addition_subtraction(sub_full_edit))
                        del calc_list[i + 1]
                        del calc_list[i - 1]
                        print('после processing_list addition:', calc_list)
                        break  #
        except (IndexError, InvalidOperation):  #
            QtWidgets.QMessageBox.information(window, "Ошибка ввода.", "Вы ошиблись при вводе!\nБудьте внимательнее!",
                                              buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
        else:  # если всё хорошо
            if (len(self.full_edit) == 1) and ('(' not in self.full_edit):  #
                self.output_result()  #

    def output_result(self):  #
        if '.' in self.full_edit[0]:
            result = str(Decimal(self.full_edit[0]).quantize(Decimal('1.' + self.prec))).replace('.', ',')  #
            if result != "None":  #
                self.textEdit_exsmple.append(self.lineEdit_1.text())  #
                self.textEdit_result.append(result)
                self.lineEdit_1.clear()  #
        else:
            result = self.full_edit[0]
            self.textEdit_exsmple.append(self.lineEdit_1.text())  #
            self.textEdit_result.append(result)
            self.lineEdit_1.clear()  #

    #
    def cursor_left(self):
        self.lineEdit_1.cursorBackward(False, 1)  #
        self.lineEdit_1.setFocus(QtCore.Qt.OtherFocusReason)  #

    #
    def cursor_right(self):
        self.lineEdit_1.cursorForward(False, 1)  #
        self.lineEdit_1.setFocus(QtCore.Qt.OtherFocusReason)  #

    #
    def lineEdit_clear(self):
        self.full_edit.clear()  #
        self.lineEdit_1.backspace()  #
        self.calc_list = str(self.lineEdit_1.text()).split()  #

    #
    def clear_edit_all(self):  #
        self.textEdit_result.clear()  #
        self.lineEdit_1.clear()  #
        self.full_edit.clear()  #


if __name__ == "__main__":  #
    import sys  #

    app = QtWidgets.QApplication(sys.argv)  #
    window = MyWindow()  # Создаем экземпляр класса
    window.setWindowTitle("Калькулятор")  # название программы
    window.setStyleSheet(open('my_style.qss', 'r').read())  # подключение QSS
    window.show()  # Отображаем окно
    sys.exit(app.exec())  # Запускаем цикл обработки событий
