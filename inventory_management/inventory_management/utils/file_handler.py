
class FileHandler:
    def __init__(self, table):
        self.table = table

    def save_to_txt(self):
        with open('estoque.txt', 'w') as file:
            for row in self.table.get_items():
                file.write(f"{','.join(row)}\n")

    def load_from_txt(self):
        try:
            with open('estoque.txt', 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    self.table.insert_row(data)
        except FileNotFoundError:
            pass
