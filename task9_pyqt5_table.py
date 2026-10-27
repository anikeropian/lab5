import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QTableWidget, QTableWidgetItem, QPushButton, QMessageBox
)


class TableWindow(QWidget):
    """Окно с таблицей данных на PyQt5."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Таблица студентов')
        self.resize(500, 300)

        layout = QVBoxLayout()

        # Создание таблицы: 3 строки, 3 столбца
        self.table = QTableWidget(3, 3)
        self.table.setHorizontalHeaderLabels(['Имя', 'Возраст', 'Группа'])
        layout.addWidget(self.table)

        # Заполнение данными
        data = [
            ('Ани', '20', '221141'),
            ('Иван', '19', '221142'),
            ('Мария', '21', '221143'),
        ]
        for row, (name, age, group) in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(name))
            self.table.setItem(row, 1, QTableWidgetItem(age))
            self.table.setItem(row, 2, QTableWidgetItem(group))

        # Кнопка для чтения данных
        self.btn = QPushButton('Показать данные')
        self.btn.clicked.connect(self.show_data)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def show_data(self):
        """Собирает данные из таблицы и показывает в диалоге."""
        result = []
        for row in range(self.table.rowCount()):
            row_data = []
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                row_data.append(item.text() if item else '')
            result.append(', '.join(row_data))
        QMessageBox.information(self, 'Данные', '\n'.join(result))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableWindow()
    window.show()
    sys.exit(app.exec_())
