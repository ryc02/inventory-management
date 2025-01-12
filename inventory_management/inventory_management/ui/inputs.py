
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QComboBox

class InputFields(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)
        self.setup_inputs()

    def setup_inputs(self):
        inputs = [
            ('Código', lambda text: ''.join(filter(str.isdigit, text))),
            ('Nome', lambda text: ''.join(filter(str.isalpha, text))),
            ('Quantidade', self.validate_numeric_input),
            ('Preço', self.validate_price_input)
        ]
        for label, validator in inputs:
            widget = QLineEdit(placeholderText=label)
            widget.textChanged.connect(lambda text, v=validator, w=widget: w.setText(v(text)))
            self.layout.addWidget(widget)
            setattr(self, f"{label.lower().replace(' ', '_')}_input", widget)
        
        self.type_input = QComboBox()
        self.type_input.addItems(["Comida", "Bebida"])
        self.layout.addWidget(self.type_input)

    def validate_numeric_input(self, text):
        return ''.join(filter(str.isdigit, text))

    def validate_price_input(self, text):
        # Allow digits, one comma or dot, but replace comma with dot for consistency
        text = ''.join(filter(lambda x: x.isdigit() or x in ',.', text))
        # Replace comma with dot to have consistent decimal separator internally
        text = text.replace(',', '.')
        # Ensure only one decimal point
        if text.count('.') > 1:
            text = text[:text.rfind('.')]
        return text

    def get_data(self):
        return {
            'code': self.code_input.text().strip(),
            'name': self.name_input.text().strip(),
            'type': self.type_input.currentText(),
            'quantity': self.quantity_input.text().strip(),
            'price': self.price_input.text().strip()
        }

    def clear(self):
        for input_field in [self.code_input, self.name_input, self.quantity_input, self.price_input]:
            input_field.clear()
