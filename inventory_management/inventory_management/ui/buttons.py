
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QMessageBox

class ActionButtons(QWidget):
    def __init__(self, parent, table, inputs):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)
        self.table = table
        self.inputs = inputs
        self.setup_buttons()

    def setup_buttons(self):
        buttons = [
            ("Adicionar", self.add_item),
            ("Alterar Item", self.update_item),
            ("Excluir Item", self.delete_item),
            ("Resumo Geral", self.show_summary),
            ("Limpar Tabela", self.clear_table)
        ]
        for text, action in buttons:
            self.create_button(text, action)

    def create_button(self, text, action):
        button = QPushButton(text, self)
        button.clicked.connect(action)
        button.setStyleSheet(
            "background-color: #2196f3; color: white; font-weight: bold; padding: 5px 15px; border-radius: 5px;"
            "border: none;"
        )
        button.setFixedHeight(40)
        self.layout.addWidget(button)

    def add_item(self):
        data = self.inputs.get_data()
        if all(data.values()):
            self.table.insert_row(list(data.values()))
            self.inputs.clear()
        else:
            QMessageBox.critical(self, "Erro", "Todos os campos devem ser preenchidos.")

    def update_item(self):
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Aviso", "Selecione um item para alterar.")
            return
        data = self.inputs.get_data()
        if all(data.values()):
            for col, value in enumerate(data.values()):
                self.table.setItem(selected_row, col, QTableWidgetItem(value))
            self.inputs.clear()
        else:
            QMessageBox.critical(self, "Erro", "Todos os campos devem ser preenchidos.")

    def delete_item(self):
        self.table.remove_selected_row()

    def show_summary(self):
        items = self.table.get_items()
        total_quantity = sum(int(item[3]) for item in items)
        total_price = sum(float(item[4]) for item in items)
        QMessageBox.information(
            self, "Resumo Geral",
            f"Quantidade Total: {total_quantity}\nValor Total: R$ {total_price:.2f}"
        )

    def clear_table(self):
        self.table.clearContents()
        self.table.setRowCount(0)
