
from PyQt6.QtWidgets import QPushButton, QHBoxLayout

class ThemeManager:
    def __init__(self, parent):
        self.parent = parent
        self.is_dark_mode = False
        self.setup_toggle_button()

    def setup_toggle_button(self):
        self.top_layout = QHBoxLayout()
        self.toggle_mode_button = QPushButton("🌙", self.parent)
        self.toggle_mode_button.setFixedSize(50, 50)
        self.toggle_mode_button.setStyleSheet("border-radius: 25px; background-color: #e0e0e0; font-size: 18px;")
        self.toggle_mode_button.clicked.connect(self.toggle_mode)
        self.top_layout.addWidget(self.toggle_mode_button)
        self.top_layout.addStretch()
        self.parent.layout.addLayout(self.top_layout)

    def toggle_mode(self):
        self.is_dark_mode = not self.is_dark_mode
        self.toggle_mode_button.setText("🌞" if self.is_dark_mode else "🌙")
        self.apply_theme()

    def apply_theme(self):
        if self.is_dark_mode:
            style = self.dark_mode_style()
        else:
            style = self.light_mode_style()
        self.parent.setStyleSheet(style)

    def dark_mode_style(self):
        return '''
            QMainWindow { background-color: #121212; color: white; }
            QTableWidget { background-color: #1e1e1e; color: white; gridline-color: #333; }
            QHeaderView::section { background-color: #333; color: #f0f0f0; }
            QLineEdit, QComboBox { background-color: #333; color: white; border: 1px solid #555; }
            QPushButton { background-color: #444; color: white; border: 1px solid #555; }
            QPushButton:hover { background-color: #555; }
        '''

    def light_mode_style(self):
        return '''
            QMainWindow { background-color: #f9f9f9; color: black; }
            QTableWidget { background-color: white; color: black; gridline-color: #ccc; }
            QHeaderView::section { background-color: #f1f1f1; color: black; }
            QLineEdit, QComboBox { background-color: white; color: black; border: 1px solid #ccc; }
            QPushButton { background-color: #e0e0e0; color: black; border: 1px solid #ccc; }
            QPushButton:hover { background-color: #d0d0d0; }
        '''
