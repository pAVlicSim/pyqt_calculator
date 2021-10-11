from PyQt5 import QtWidgets


class My_LineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocus()

    def keyPressEvent(self, e):
        super().keyPressEvent(e)
