
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from .table import StockTable
from .inputs import InputFields
from .buttons import ActionButtons
from .theme import ThemeManager
from utils.file_handler import FileHandler

class StockManagementMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestão de Estoque")
        self.setGeometry(200, 200, 900, 600)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.theme_manager = ThemeManager(self)
        self.stock_table = StockTable(self)
        self.input_fields = InputFields(self)
        self.action_buttons = ActionButtons(self, self.stock_table, self.input_fields)

        self.layout.addWidget(self.stock_table)
        self.layout.addWidget(self.input_fields)
        self.layout.addWidget(self.action_buttons)

        self.file_handler = FileHandler(self.stock_table)
        self.file_handler.load_from_txt()

    def closeEvent(self, event):
        self.file_handler.save_to_txt()
        event.accept()
