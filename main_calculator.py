import os
from _decimal import setcontext
from decimal import Decimal, DivisionByZero, InvalidOperation, Context
from math import sin, radians, cos, tan

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QDesktopWidget

from myForm import my_form_calculator


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


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
    result = Decimal(normal_number) ** Decimal(small_number)
    return result


def calculation_multiplication_division(sub_full_edit: list[str]):
    result = 0
    if sub_full_edit[1] == '×':
        result = Decimal(sub_full_edit[0]) * Decimal(sub_full_edit[2])
    elif sub_full_edit[1] == '÷':
        result = Decimal(sub_full_edit[0]) / Decimal(sub_full_edit[2])
    return result


def calculation_addition_subtraction(sub_full_edit: list[str]):
    result = 0
    if sub_full_edit[1] == '+':
        result = Decimal(sub_full_edit[0]) + Decimal(sub_full_edit[2])
    elif sub_full_edit[1] == '-':
        result = Decimal(sub_full_edit[0]) - Decimal(sub_full_edit[2])
    return result


def calculation_root(numberRoot: str, small_list: list[str], normal_list: list[str]):
    numberRootList = numberRoot.split('√')
    number_dict = dict(zip(small_list, normal_list))
    for i in numberRootList[0]:
        for small_number in number_dict:
            if i == small_number:
                numberRootList[0] = numberRootList[0].replace(i, number_dict[small_number])
    result = Decimal(numberRootList[1]) ** (1 / Decimal(numberRootList[0]))
    return result


def calculation_trigonometry(number_trigonometry: str):
    result = 0
    if 'sin' in number_trigonometry:
        number_trigonometry = number_trigonometry.removeprefix('sin')
        result = sin(radians(Decimal(number_trigonometry)))
    elif 'ctg' in number_trigonometry:
        number_trigonometry = number_trigonometry.removeprefix('ctg')
        result = 1 / tan(radians(Decimal(number_trigonometry)))
    elif 'cos' in number_trigonometry:
        number_trigonometry = number_trigonometry.removeprefix('cos')
        result = cos(radians(Decimal(number_trigonometry)))
    elif 'tg' in number_trigonometry:
        number_trigonometry = number_trigonometry.removeprefix('tg')
        result = tan(radians(Decimal(number_trigonometry)))
    return result


def input_bracket(bracket: str, input_line: str):
    left_bracket = '( '
    right_bracket = ' )'
    input_symbol = ''
    if bracket == left_bracket and input_line.count(left_bracket) == input_line.count(right_bracket):
        input_symbol = left_bracket + right_bracket
    elif bracket == left_bracket and input_line.count(left_bracket) < input_line.count(right_bracket):
        input_symbol = left_bracket
    elif bracket == right_bracket and input_line.count(left_bracket) > input_line.count(right_bracket):
        input_symbol = right_bracket
    elif bracket == right_bracket and input_line.count(left_bracket) <= input_line.count(right_bracket):
        input_symbol = ''
    return input_symbol


def calculation_percent(full_edit: list[str]):
    result = ''
    if full_edit[-2] == '+':
        result = str(Decimal(full_edit[-3]) + ((Decimal(full_edit[-3]) / 100) * Decimal(full_edit[-1])))
    elif full_edit[-2] == '-':
        result = str(Decimal(full_edit[-3]) - ((Decimal(full_edit[-3]) / 100) * Decimal(full_edit[-1])))
    print(result)
    return result


class MyWindow(QtWidgets.QFrame, my_form_calculator.Ui_Form):  # главный класс

    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        self.setupUi(self)

        self.number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',']  # лист обычных цифр
        self.actionButton = [' + ', ' - ', ' × ', ' ÷ ', '√', 'sin', 'cos', 'tg', 'ctg']  # лист математических символов
        self.small_number = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']  # лист надстрочных цифр
        self.cP_list = [' + ', ' - ', ' × ', ' ÷ ', 'sin', 'cos', 'tg', 'ctg', '( ', ' )', 'log', 'lg', 'ln']
        self.full_edit: list[str]  # лист вводимых символов в lineEdit1
        self.lineEdit_1.setFocus(QtCore.Qt.OtherFocusReason)  # настройка фокуса, от нажатия кнопок на окне программы
        self.prec_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '15', '20', '25']  # кортеж для comboBox
        self.prec = '000000'

        self.comboBox.addItems(self.prec_list)
        self.comboBox.setCurrentText(str(len(self.prec)))

        self.tableModel = QtGui.QStandardItemModel(0, 2)
        self.tableViewResult.setModel(self.tableModel)

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
        self.pushButton_sin.clicked.connect(lambda: self.continuous_input('sin'))
        self.pushButton_cos.clicked.connect(lambda: self.continuous_input('cos'))
        self.pushButton_tg.clicked.connect(lambda: self.continuous_input('tg'))
        self.pushButton_ctg.clicked.connect(lambda: self.continuous_input('ctg'))

        self.pushButton_result.clicked.connect(self.cursor_to_end)  # кнопка запуска расчёта
        self.pushButton_clear_all.clicked.connect(self.clear_edit_all)  # очищает все поля
        self.pushButton_clear_one.clicked.connect(self.lineEdit_clear)  # очищает один символ за нажатие
        self.pushButton_percent.clicked.connect(self.processing_percent)
        self.pushButton_reverse.clicked.connect(self.processing_reverse_number)

        # кнопки перемещения курсора
        self.pushButton_cursor_left.clicked.connect(self.cursor_left)  # кнопка передвигает курсор влево
        self.pushButton_cursor_right.clicked.connect(self.cursor_right)  # кнопка передвигает курсор вправо

        self.comboBox.activated[str].connect(self.tincture_of_prec)
        self.tableViewResult.clicked.connect(self.continuous_input)

    #
    def center(self):
        frame_geometry = self.frameGeometry()
        center_desktop = QDesktopWidget().availableGeometry().center()
        frame_geometry.moveCenter(center_desktop)
        self.move(frame_geometry.topLeft())

    #
    def tincture_of_prec(self):
        self.prec = '0' * int(self.comboBox.currentIndex() + 1)

    # функция вводит символы в lineEdit1
    def continuous_input(self, symbol):  # символ передаётся при нажатии соответствующей кнопки
        # если символ входит в листы цифр и действий
        if symbol in self.number or symbol in self.small_number or symbol in self.actionButton:
            self.lineEdit_1.insert(symbol)  # символ вставляется в конец строки
            self.full_edit = str(self.lineEdit_1.text()).split()  # преобразование строки в лист по пробелам
            for i in range(len(self.full_edit)):
                self.full_edit[i] = self.full_edit[i].replace(',', '.')
            print(self.full_edit)  #
        elif symbol == '±':  # если нажата кнопка плюс-минус
            self.lineEdit_1.insert('-')  # вставляется знак отрицательного числа
            self.full_edit = str(self.lineEdit_1.text()).split()  # преобразование строки в лист по пробелам
            print(self.full_edit)  #
        elif symbol == '( ' or symbol == ' )':
            self.lineEdit_1.insert(input_bracket(symbol, self.lineEdit_1.text()))
            if (input_bracket(symbol, self.lineEdit_1.text()) == '(  )' or
                    input_bracket(symbol, self.lineEdit_1.text()) == ' )'):
                self.lineEdit_1.cursorBackward(False, 2)
            self.full_edit = str(self.lineEdit_1.text()).split()  # преобразование строки в лист по пробелам
            print(self.full_edit)  #
        else:
            self.lineEdit_1.insert(self.tableViewResult.currentIndex().data())
            self.full_edit = str(self.lineEdit_1.text()).split()  # преобразование строки в лист по пробелам
            print(self.full_edit)  #

    def cursor_to_end(self):
        self.lineEdit_1.end(False)  # перемещает курсор в конец строки
        self.processing_list_bracket()

    # преобразует full_edit убирая скобки
    def processing_list_bracket(self):
        if len(self.lineEdit_1.text()) > 0:
            left_bracket = '('  # левая скобка
            right_bracket = ')'  # правая скобка
            # если в full_edit есть скобки
            if (left_bracket in self.full_edit or right_bracket in self.full_edit and
                    self.full_edit.count(left_bracket) == self.full_edit.count(right_bracket)):
                # цикл работает пока есть скобки
                while left_bracket in self.full_edit or right_bracket in self.full_edit:
                    for i in range(len(self.full_edit)):  # цикл обходит основной список по индексу
                        # если в срезе,между левой и правой скобок,нет скобок
                        if (left_bracket not in self.full_edit[i + 1: self.full_edit.index(right_bracket)] and
                                right_bracket not in self.full_edit[i + 1: self.full_edit.index(right_bracket)]):
                            # создаём новый список из среза
                            sub_full_edit = self.full_edit[i: self.full_edit.index(right_bracket) + 1]
                            print(sub_full_edit)
                            # удаляем срез из  основного списка
                            del self.full_edit[i: self.full_edit.index(right_bracket) + 1]
                            print(self.full_edit)
                            sub_full_edit.remove(left_bracket)  # удаляем из нового списка скобки
                            sub_full_edit.remove(right_bracket)  #
                            print(sub_full_edit)
                            print(self.full_edit)
                            self.processing_list_trigonometry(sub_full_edit)  # считаем результат в новом списке
                            self.full_edit.insert(i, sub_full_edit[0])  # вставляем результат в основной список
                            break  # возвращаемся в начало цикла for искать следующую пару скобок
                # когда все скобки убраны, запускаем расчёт основного списка
                self.processing_list_trigonometry(self.full_edit)
            else:  # если изначально в основном списке нет скобок
                self.processing_list_trigonometry(self.full_edit)  # запускаем расчёт основного списка

    def processing_list_trigonometry(self, calc_list: list):
        try:
            while range(len(calc_list)):  # цикл будет исполнятся пока не дойдёт до конца списка
                for i in range(len(calc_list)):  # цикл перебирает full_edit по индексам
                    if (('sin' in calc_list[i]) or ('cos' in calc_list[i]) or ('tg' in calc_list[i])
                            or ('ctg' in calc_list[i])):
                        calc_list[i] = str(calculation_trigonometry(calc_list[i]))
                break
            print('после преобразования trigonometry', calc_list)
        except (InvalidOperation, IndexError):
            QtWidgets.QMessageBox.information(window, "Ошибка ввода. Вы ошиблись при вводе!\nБудьте внимательнее!",
                                              buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
        else:
            self.processing_list_root(calc_list)

    # функция ищет объекты со знаком "корня" и отправляет их в метод для расчёта
    def processing_list_root(self, calc_list: list):
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

    def processing_percent(self):
        if (len(self.lineEdit_1.text()) > 0 and len(self.full_edit) == 3 and
                (self.full_edit[-2] == '+' or self.full_edit[-2] == '-')):
            result = calculation_percent(self.full_edit)
            self.full_edit.clear()
            self.full_edit.append(result)
            self.output_result()  #

    def processing_reverse_number(self):
        if len(self.lineEdit_1.text()) > 0 and len(self.full_edit) == 1 and self.full_edit[0].isdigit():
            result = str(1 / Decimal(self.full_edit[0].replace(',', '.')))
            self.full_edit[0] = result
            print(self.full_edit)
            self.output_result()

    def output_result(self):  #
        if '.' in self.full_edit[0]:
            result = str(Decimal(self.full_edit[0]).quantize(Decimal('1.' + self.prec)).normalize()).replace('.',
                                                                                                             ',')
            if result != "None":  #
                L = [QtGui.QStandardItem(self.lineEdit_1.text()), QtGui.QStandardItem('='),
                     QtGui.QStandardItem(result)]  # лист для заполнения строки
                self.tableModel.appendRow(L)  # добавляем строку в таблицу
                self.tableViewResult.resizeColumnsToContents()
                self.lineEdit_1.clear()  #
        else:
            L = [QtGui.QStandardItem(self.lineEdit_1.text()), QtGui.QStandardItem('='),
                 QtGui.QStandardItem(self.full_edit[0])]  # лист для заполнения строки
            self.tableModel.appendRow(L)  # добавляем строку в таблицу
            self.tableViewResult.resizeColumnsToContents()
            self.lineEdit_1.clear()  #

    #
    def cursor_left(self):
        cP = self.lineEdit_1.cursorPosition()
        try:
            if (self.lineEdit_1.text()[cP - 2: cP] == ' )' or self.lineEdit_1.text()[cP - 2: cP] == '( ' or
                    self.lineEdit_1.text()[cP - 2: cP] == 'lg' or self.lineEdit_1.text()[cP - 2: cP] == 'ln'):
                self.lineEdit_1.cursorBackward(False, 2)  #
            elif (self.lineEdit_1.text()[cP - 3: cP] == ' + ' or self.lineEdit_1.text()[cP - 3: cP] == ' - ' or
                  self.lineEdit_1.text()[cP - 3: cP] == ' × ' or self.lineEdit_1.text()[cP - 3: cP] == ' ÷ ' or
                  self.lineEdit_1.text()[cP - 3: cP] == 'sin' or self.lineEdit_1.text()[cP - 3: cP] == 'cos' or
                  self.lineEdit_1.text()[cP - 3: cP] == 'log'):
                self.lineEdit_1.cursorBackward(False, 3)  #
            elif self.lineEdit_1.text()[cP - 3: cP] == 'ctg' or self.lineEdit_1.text()[cP - 3: cP] == ' tg':
                if self.lineEdit_1.text()[cP - 3: cP] == 'ctg':
                    self.lineEdit_1.cursorBackward(False, 3)  #
                elif self.lineEdit_1.text()[cP - 3: cP] == ' tg':
                    self.lineEdit_1.cursorBackward(False, 2)  #
            else:
                self.lineEdit_1.cursorBackward(False, 1)  #
        except IndexError:
            pass

    #
    def cursor_right(self):
        cP = self.lineEdit_1.cursorPosition()
        try:
            if cP == len(self.lineEdit_1.text()) - 1:
                self.lineEdit_1.end(False)
            elif (self.lineEdit_1.text()[cP: cP + 2] == '( ' or self.lineEdit_1.text()[cP: cP + 2] == ' )' or
                  self.lineEdit_1.text()[cP: cP + 2] == 'tg' or self.lineEdit_1.text()[cP: cP + 2] == 'ln' or
                  self.lineEdit_1.text()[cP: cP + 2] == 'lg'):
                self.lineEdit_1.cursorForward(False, 2)  #
            elif (self.lineEdit_1.text()[cP: cP + 3] == ' + ' or self.lineEdit_1.text()[cP: cP + 3] == ' - ' or
                  self.lineEdit_1.text()[cP: cP + 3] == ' × ' or self.lineEdit_1.text()[cP: cP + 3] == ' ÷ ' or
                  self.lineEdit_1.text()[cP: cP + 3] == 'cos' or self.lineEdit_1.text()[cP: cP + 3] == 'sin' or
                  self.lineEdit_1.text()[cP: cP + 3] == 'ctg' or self.lineEdit_1.text()[cP: cP + 3] == 'log'):
                self.lineEdit_1.cursorForward(False, 3)  #
            else:
                self.lineEdit_1.cursorForward(False, 1)  #
        except IndexError:
            pass

    def lineEdit_clear(self):
        self.full_edit.clear()  #
        cP = self.lineEdit_1.cursorPosition()
        try:
            if (self.lineEdit_1.text()[cP - 2: cP] == ' )' or self.lineEdit_1.text()[cP - 2: cP] == '( ' or
                    self.lineEdit_1.text()[cP - 2: cP] == 'lg' or self.lineEdit_1.text()[cP - 2: cP] == 'ln'):
                self.lineEdit_1.setSelection(cP - 2, cP)
                self.lineEdit_1.backspace()  #
            elif (self.lineEdit_1.text()[cP - 3: cP] == ' + ' or self.lineEdit_1.text()[cP - 3: cP] == ' - ' or
                  self.lineEdit_1.text()[cP - 3: cP] == ' × ' or self.lineEdit_1.text()[cP - 3: cP] == ' ÷ ' or
                  self.lineEdit_1.text()[cP - 3: cP] == 'sin' or self.lineEdit_1.text()[cP - 3: cP] == 'cos' or
                  self.lineEdit_1.text()[cP - 3: cP] == 'log'):
                self.lineEdit_1.setSelection(cP - 3, cP)
                self.lineEdit_1.backspace()  #
            elif self.lineEdit_1.text()[cP - 3: cP] == 'ctg' or self.lineEdit_1.text()[cP - 3: cP] == ' tg':
                if self.lineEdit_1.text()[cP - 3: cP] == 'ctg':
                    self.lineEdit_1.setSelection(cP - 3, cP)
                    self.lineEdit_1.backspace()  #
                elif self.lineEdit_1.text()[cP - 3: cP] == ' tg':
                    self.lineEdit_1.setSelection(cP - 2, cP)
                    self.lineEdit_1.backspace()  #
            else:
                self.lineEdit_1.backspace()  #
        except IndexError:
            pass
        self.full_edit = str(self.lineEdit_1.text()).split()  #

    #
    def clear_edit_all(self):  #
        self.lineEdit_1.clear()  #
        self.full_edit.clear()  #
        self.tableModel.removeRows(0, self.tableModel.rowCount())


if __name__ == "__main__":  #
    import sys  #

    app = QtWidgets.QApplication(sys.argv)  #
    window = MyWindow()  # Создаем экземпляр класса
    window.setWindowTitle("Калькулятор")  # название программы
    qss_dir = resource_path('qss_file')
    icon_dir = resource_path("icon_file")
    ico = QtGui.QIcon(icon_dir + '/calculator_icon.png')  # настраиваем иконку
    window.setWindowIcon(ico)
    window.setStyleSheet(open(qss_dir + '/myStyle.qss').read())  # подключение QSS
    window.show()  # Отображаем окно
    sys.exit(app.exec())  # Запускаем цикл обработки событий
