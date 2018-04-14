


class symbol_table():
    
    def __init__(self):
        
        self.current_line = 0
        self.current_ram = 16

        self.table_of_symbols = {
            'R0' : 0,
            'R1' : 1,
            'R2' : 2,
            'R3' : 3,
            'R4' : 4,
            'R5' : 5,
            'R6' : 6,
            'R7' : 7,
            'R8' : 8,
            'R9' : 9,
            'R10': 10,
            'R11': 11,
            'R12': 12,
            'R13': 13,
            'R14': 14,
            'R15': 15,
            'SP' : 0,
            'LCL': 1,
            'ARG': 2,
            'THIS':3,
            'THAT':4,
            'SCREEN':16384,
            'KBD':24576 #keyboard
        }

    def get_symbol(self,name):
        return self.table_of_symbols[name]


    def is_in(self,name):
        if name in self.table_of_symbols:
            return True
        return False

    def input_item(self,name):
        self.table_of_symbols[name] = self.current_line


    def increment_current_line(self):
        self.current_line += 1


    def increment_ram_number(self):
        self.current_ram += 1


    def add_variable_to_next_free_ram(self, label):
        self.table_of_symbols[label] = self.current_ram
        self.increment_ram_number() #this behaviour could be buggy...