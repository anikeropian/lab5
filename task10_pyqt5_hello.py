import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout


class HelloWindow(QWidget):
    """Простое окно на PyQt5."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle('PyQt5 Hello')
        self.resize(300, 150)

        layout = QVBoxLayout()

        self.label = QLabel('Нажмите кнопку!')
        layout.addWidget(self.label)

        self.btn = QPushButton('Нажми меня')
        self.btn.clicked.connect(self.change_text)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def change_text(self):
        """Меняет текст метки при нажатии."""
        self.label.setText('Привет, PyQt5!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HelloWindow()
    window.show()
    sys.exit(app.exec_())
