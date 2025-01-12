
from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem

class StockTable(QTableWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(["Código", "Nome", "Tipo", "Quantidade", "Preço"])
        self.horizontalHeader().setStyleSheet("font-weight: bold; background-color: #f0f0f0; color: black;")
        self.horizontalHeader().setStretchLastSection(True)
        self.setStyleSheet(
            "QTableWidget { border: 1px solid #ccc; font-size: 14px; } "
            "QHeaderView::section { padding: 5px; border: 1px solid #ddd; } "
            "QTableWidget::item { border: none; padding: 5px; }"
        )

    def insert_row(self, data):
        row_position = self.rowCount()
        self.insertRow(row_position)
        for col, value in enumerate(data):
            self.setItem(row_position, col, QTableWidgetItem(value))

    def remove_selected_row(self):
        selected_row = self.currentRow()
        if selected_row != -1:
            self.removeRow(selected_row)

    def get_items(self):
        items = []
        for row in range(self.rowCount()):
            row_data = [self.item(row, col).text() for col in range(self.columnCount())]
            items.append(row_data)
        return items
